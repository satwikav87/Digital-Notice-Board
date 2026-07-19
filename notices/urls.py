from django.urls import path
from . import views
urlpatterns=[path("",views.home,name="home"),path("notice/<int:pk>/",views.notice_detail,name="notice_detail"),path("dashboard/",views.dashboard,name="dashboard"),path("dashboard/notices/",views.manage,name="manage"),path("dashboard/settings/",views.settings_view,name="settings"),path("notice/create/",views.notice_create,name="notice_create"),path("notice/<int:pk>/edit/",views.notice_update,name="notice_update"),path("notice/<int:pk>/delete/",views.notice_delete,name="notice_delete")]
