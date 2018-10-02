from django.shortcuts import render
from .models import TopJobs, HotJobs, FeaturedJobs
from django.views.generic import View
from . import scraper


class home(View):
	template = 'Jobs/home.html'
	
	def get(self, request):
		return render(request, self.template)

class top(View):
	model = TopJobs
	template = 'Jobs/top.html'
	def get(self, request):
		return render(request, self.template, {'jobs': scraper.top_jobs, 'visibility': False})
	
	def post(self, request):
		TopJobs.objects.all().delete()
		for job in scraper.top_jobs:
			a=TopJobs(Company = job['company'], Position = job['position'])
			a.save()
		return render(request, self.template)

class toplist(View):

	model = TopJobs
	template = 'Jobs/top.html'
	def get(self, request):
		return render(request, self.template, {'jobs': scraper.top_jobs, 'visibility': True})
#		return HttpResponse('<p>Hi.</p>')

class hot(View):
	model = HotJobs
	template = 'Jobs/hot.html'
	
	def get(self, request):
		return render(request, self.template)

	def post(self, request, context):
		HotJobs.objects.all().delete()
		for job in scraper.hot_jobs:
			a=HotJobs(Company = job['company'], Position = job['position'])
			a.save()
		return render(request, self.template, {'jobs': scraper.hot_jobs})

class featured(View):
	model = FeaturedJobs
	template = 'Jobs/featured.html'
	
	def get(self, request):
		return render(request, self.template)

	def post(self, request, context):
		FeaturedJobs.objects.all().delete()
		for job in scraper.featured_jobs:
			a=HotJobs(Company = job['company'], Position = job['position'])
			a.save()
		return render(request, self.template, {'jobs': scraper.featured_jobs})