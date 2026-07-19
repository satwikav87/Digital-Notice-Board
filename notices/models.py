from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
class Institution(models.Model):
 name=models.CharField(max_length=180,default="CampusConnect Academy")
 tagline=models.CharField(max_length=220,default="Everything your campus needs to communicate better")
 logo=models.ImageField(upload_to="institution/",blank=True,null=True)
 address=models.TextField(blank=True)
 phone=models.CharField(max_length=30,blank=True)
 email=models.EmailField(blank=True)
 primary_color=models.CharField(max_length=20,default="#3157f6")
 def __str__(self): return self.name
class Department(models.Model):
 name=models.CharField(max_length=120,unique=True)
 short_name=models.CharField(max_length=20,blank=True)
 class Meta: ordering=["name"]
 def __str__(self): return self.short_name or self.name
class Category(models.Model):
 name=models.CharField(max_length=100,unique=True)
 icon=models.CharField(max_length=10,default="📢")
 color=models.CharField(max_length=20,default="#3157f6")
 class Meta: ordering=["name"]
 def __str__(self): return self.name
class Notice(models.Model):
 PRIORITIES=[("low","Low"),("normal","Normal"),("high","High"),("urgent","Urgent")]
 AUDIENCES=[("all","Everyone"),("students","Students"),("staff","Staff"),("parents","Parents")]
 title=models.CharField(max_length=200)
 content=models.TextField()
 category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name="notices")
 department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True,related_name="notices")
 audience=models.CharField(max_length=20,choices=AUDIENCES,default="all")
 priority=models.CharField(max_length=10,choices=PRIORITIES,default="normal")
 image=models.ImageField(upload_to="notices/images/",blank=True,null=True)
 attachment=models.FileField(upload_to="notices/files/",blank=True,null=True)
 author=models.ForeignKey(User,on_delete=models.CASCADE)
 is_published=models.BooleanField(default=True)
 is_pinned=models.BooleanField(default=False)
 publish_date=models.DateTimeField(default=timezone.now)
 expiry_date=models.DateTimeField(blank=True,null=True)
 views=models.PositiveIntegerField(default=0)
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta: ordering=["-is_pinned","-publish_date"]
 def __str__(self): return self.title
 def get_absolute_url(self): return reverse("notice_detail",args=[self.pk])
 @property
 def is_expired(self): return bool(self.expiry_date and self.expiry_date<timezone.now())
 @property
 def is_new(self): return self.publish_date>=timezone.now()-timezone.timedelta(days=3)
