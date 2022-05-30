from email import message
from email.mime import image
from lib2to3.pytree import convert
from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt

from news.models import Article

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def news_of_day(request):
    date = dt.date.today()
    image = Article.objects.all()
    return render(request,'all-news/today-news.html',{'date':date,'image':image})
    
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    # return HttpResponse(html)


# def convert_dates(dates):
    
#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)
    
    
#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    
#     #Returning the actual day of the week
#     day = days[day_number]
#     return day

def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        
    except ValueError:
        #Raise ValueError
        raise Http404()
        assert False
        
    if date == dt.date.today():
        return redirect(news_of_day)
    
    return render(request,'all-news/past-news.html',{"date": date})
    
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    # return HttpResponse(html)
    
    
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
def article(request,article_id):
    article = Article.objects.get(id = article_id)

    return render(request,"all-news/article.html", {"article":article})