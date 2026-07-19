from django.contrib import admin
from .models import Institution,Department,Category,Notice
admin.site.register(Institution)
admin.site.register(Department)
admin.site.register(Category)
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
 list_display=("title","category","department","priority","is_published","publish_date")
 list_filter=("priority","category","department","is_published","is_pinned")
 search_fields=("title","content")
 def save_model(self,request,obj,form,change):
  if not obj.pk: obj.author=request.user
  super().save_model(request,obj,form,change)
