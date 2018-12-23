import requests
from bs4 import BeautifulSoup
import sys

def sky_news(num):
	news_list = []
	page = requests.get("https://news.sky.com/world")  

	soup = BeautifulSoup(page.text, 'html.parser')
	sat = soup.find_all("h3", attrs={"class","sdc-site-tile__headline"})

	for x in range(int(num)):
			
		news_list.append(sat[x].a.span.text)

	return news_list

