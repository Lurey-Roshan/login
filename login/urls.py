from django.urls import path, include
from login import views

urlpatterns=[
	path('login',views.login_view, name='login'),
	path('signup',views.register_view, name='register'),
	path('logout',views.logout_view, name='logout')
	]