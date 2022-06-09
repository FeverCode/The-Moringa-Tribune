from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.news_today, name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name='pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('new/article', views.new_article, name='new-article'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ajax/newsletter/', views.newsletter, name='newsletter'),
    path('api/merch/', views.MerchList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/merch/merch-id/<int:pk>/', views.MerchDescription.as_view()),
    
]
