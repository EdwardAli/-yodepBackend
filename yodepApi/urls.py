from django import views
from django.urls import path
from . import views
from .views import index
from rest_framework.authtoken import views


from knox import views as knox_views

from yodepApi.views import *

urlpatterns = [

    path('', index),

    path('yodepApi_register/', RegisterAPI.as_view(), name='register'),
    path('yodepApi_login/', LoginAPI.as_view(), name='login'),
    path('yodepApi_logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('yodepApi_logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    #1 for testimonial
    path('testimonial_create/', TestimonialCreate.as_view()),
    path('testimonial_list/', TestimonialList.as_view()),
    path('testimonial/<int:pk>', TestimonialDetail.as_view()),

    #2 for programs
    path('project_create/', ProjectCreate.as_view()),
    path('project_list/', ProjectList.as_view()),
    path('project/<int:pk>', ProjectDetail.as_view()),

    #3 for Career
    path('career_create/', CareerCreate.as_view()),
    path('career_list/', CareerList.as_view()),
    path('career/<int:pk>', CareerDetail.as_view()),

    #4 for gallary
    path('image_create/', ImageCreate.as_view()),
    path('image_list/', ImageList.as_view()),
    path('image/<int:pk>', ImageDetail.as_view()),

    #5 news and insights
    path('news_create/', NewsCreate.as_view()),
    path('news_list/', NewsList.as_view()),
    path('news/<int:pk>', NewsDetail.as_view()),

    #6 events and campaigns
    path('event_create/', EventCreate.as_view()),
    path('events_list/', EventsList.as_view()),
    path('event/<int:pk>', EventDetail.as_view()),

    #7 for blog 
    path('blog_create/', BlogCreate.as_view()),
    path('blog_list/', BlogList.as_view()),
    path('blog/<int:pk>', BlogDetail.as_view()),

    #8 for comment 
    path('comment_create/', CommentCreate.as_view()),
    path('comment_list/', CommentList.as_view()),
    path('comment/<int:pk>', CommentDetail.as_view()),

    #9 for partner 
    path('partner_create/', PartnerCreate.as_view()),
    path('partner_list/', PartnerList.as_view()),
    path('partner/<int:pk>', PartnerDetail.as_view()),

    #9 for vacancy 
    path('vacancy_create/', VacancyCreate.as_view()),
    path('vacancy_list/', VacancyList.as_view()),
    path('vacancy/<int:pk>', VacancyDetail.as_view())
]


