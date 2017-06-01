from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.users_login),
    url(r'^register/$',views.users_register),
    url(r'^user_post/$', views.users_login_info),
    url(r'^user_name/$' ,views.user_name_ver),
    url(r'^user_passwd/$', views.user_passwd_ver),
    url(r'^check_user/$', views.users_register_ver),
    url(r'^commit/$', views.users_register_commit),
]