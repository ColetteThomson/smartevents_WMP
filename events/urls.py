from django.urls import path, re_path
from . import views

urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()'
    # path('', views.PostList.as_view(), name='home'),
    # path converter if matched to return a string, if not a 404 message

    # capture url and pass to calendar view
    path('calendar', views.calendar, name='calendar'),
    
    # path('<int:year>/<str:month>/', views.calendar, name='calendar'),

    # regex comment...p96...
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/',
            views.calendar, name='calendar'),
]
