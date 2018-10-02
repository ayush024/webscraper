from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get('https://merojob.com/')
soup = bs(r.text, 'html.parser')
categories = soup.findAll('div',{'class':'card'})

def extract(category):
	joblist = []
	jobs=category.findAll('div',{'class':'media-body'})
	
	for job in jobs:
		try:
			joblist.append({'company' : job.h2.text.strip(), 'position' : job.h3.p.a.span.text.strip()})
		except:
			joblist.append({'company' : job.a.span.text.strip(), 'position' : job.p.a.span.text.strip()})
	return joblist

for category in categories:
	#Top Jobs
	if category.div.strong.h1.strong.text=='Top Jobs':
		top_jobs = extract(category)
			
	#Hot Jobs
	elif re.search('Hot',category.div.strong.h1.strong.text):
		hot_jobs = extract(category)
				
	#Featured Jobs				
	elif category.div.strong.h1.strong.text=='Featured Jobs':
		featured_jobs=extract(category)
					
	#Others
	else:
		break

