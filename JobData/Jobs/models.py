from django.db import models

#TopJobs
class TopJobs(models.Model):
	Company = models.CharField(max_length = 100)
	Position = models.CharField(max_length = 75)

	def __str__(self):
		return self.Position

#HotJobs
class HotJobs(models.Model):
	Company = models.CharField(max_length = 100)
	Position = models.CharField(max_length = 75)

	def __str__(self):
		return self.Position

#FeaturedJobs
class FeaturedJobs(models.Model):
	Company = models.CharField(max_length = 100)
	Position = models.CharField(max_length = 75)

	def __str__(self):
		return self.Position