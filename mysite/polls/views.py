from django.shortcuts import render
from django.template import loader
from .scrape import sky_news

def index(request):
        
        if(request.GET.get('mybtn')):
                news = sky_news(5)

        elif(request.GET.get('mybtn2')):
                news = sky_news(1)
        else:
                news = sky_news(20)
                
        return render(request, 'polls/index.html', {"news":news})

