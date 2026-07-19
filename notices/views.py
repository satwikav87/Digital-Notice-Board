from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Count,F,Q,Sum
from django.shortcuts import get_object_or_404,redirect,render
from django.utils import timezone
from .forms import InstitutionForm,NoticeForm
from .models import Category,Department,Institution,Notice
def staff(u): return u.is_authenticated and u.is_staff
def active_notices():
 now=timezone.now()
 return Notice.objects.select_related("category","department","author").filter(is_published=True,publish_date__lte=now).filter(Q(expiry_date__isnull=True)|Q(expiry_date__gte=now))
def home(request):
 qs=active_notices(); q=request.GET.get("q",""); cat=request.GET.get("category",""); dep=request.GET.get("department","")
 if q: qs=qs.filter(Q(title__icontains=q)|Q(content__icontains=q))
 if cat: qs=qs.filter(category_id=cat)
 if dep: qs=qs.filter(department_id=dep)
 return render(request,"notices/home.html",{"notices":qs,"featured":active_notices().filter(is_pinned=True)[:3],"categories":Category.objects.annotate(total=Count("notices")),"departments":Department.objects.all(),"notice_count":active_notices().count(),"department_count":Department.objects.count(),"total_views":Notice.objects.aggregate(v=Sum("views"))["v"] or 0,"q":q,"selected_category":cat,"selected_department":dep})
def notice_detail(request,pk):
 n=get_object_or_404(Notice,pk=pk); Notice.objects.filter(pk=pk).update(views=F("views")+1); n.refresh_from_db(); return render(request,"notices/detail.html",{"notice":n})
@login_required
@user_passes_test(staff)
def dashboard(request):
 qs=Notice.objects.select_related("category","department"); stats=Category.objects.annotate(total=Count("notices")).filter(total__gt=0)[:6]
 return render(request,"notices/dashboard.html",{"notices":qs[:8],"total":qs.count(),"published":qs.filter(is_published=True).count(),"views":qs.aggregate(v=Sum("views"))["v"] or 0,"departments":Department.objects.count(),"stats":stats,"max_stat":max([x.total for x in stats],default=1)})
@login_required
@user_passes_test(staff)
def manage(request): return render(request,"notices/manage.html",{"notices":Notice.objects.select_related("category","department")})
@login_required
@user_passes_test(staff)
def notice_create(request):
 form=NoticeForm(request.POST or None,request.FILES or None)
 if request.method=="POST" and form.is_valid():
  obj=form.save(commit=False); obj.author=request.user; obj.save(); messages.success(request,"Notice published successfully."); return redirect("dashboard")
 return render(request,"notices/form.html",{"form":form,"title":"Create Notice"})
@login_required
@user_passes_test(staff)
def notice_update(request,pk):
 obj=get_object_or_404(Notice,pk=pk); form=NoticeForm(request.POST or None,request.FILES or None,instance=obj)
 if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Notice updated."); return redirect("manage")
 return render(request,"notices/form.html",{"form":form,"title":"Edit Notice"})
@login_required
@user_passes_test(staff)
def notice_delete(request,pk):
 obj=get_object_or_404(Notice,pk=pk)
 if request.method=="POST": obj.delete(); return redirect("manage")
 return render(request,"notices/delete.html",{"notice":obj})
@login_required
@user_passes_test(staff)
def settings_view(request):
 obj,_=Institution.objects.get_or_create(pk=1); form=InstitutionForm(request.POST or None,request.FILES or None,instance=obj)
 if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Branding updated."); return redirect("settings")
 return render(request,"notices/settings.html",{"form":form})
