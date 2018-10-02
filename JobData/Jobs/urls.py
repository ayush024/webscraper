from django.urls import path
from . import views

urlpatterns = [
	path('', views.home.as_view(), name='home'),
	path('topjobs/', views.top.as_view(), name='top'),
	path('topjobs/list', views.toplist.as_view(), name='toplist'),
	path('hotjobs/', views.hot.as_view(), name='hot'),
	path('featuredjobs/', views.featured.as_view(), name='featured'),
]