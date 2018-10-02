from django.urls import path
from . import views

urlpatterns = [
	path('', views.home.as_view(), name='home'),
	path('topjobs/', views.top.as_view(), name='top'),
	path('topjobs/list', views.toplist.as_view(), name='toplist'),
	path('topjobs/emptylist', views.topempty.as_view(), name='topemptylist'),
	path('hotjobs/', views.hot.as_view(), name='hot'),	
	path('hotjobs/list', views.hotlist.as_view(), name='hotlist'),
	path('hotjobs/emptylist', views.hotempty.as_view(), name='hotemptylist'),
	path('featuredjobs/', views.featured.as_view(), name='featured'),
	path('featuredjobs/list', views.featuredlist.as_view(), name='featuredlist'),
	path('featuredjobs/emptylist', views.featuredempty.as_view(), name='featuredemptylist'),
]