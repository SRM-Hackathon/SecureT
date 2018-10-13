from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.signup, name='signup'),
	url(r'^login/$', views.login, name='login'),
	url(r'^hello/$', views.hello, name='hello'),
]