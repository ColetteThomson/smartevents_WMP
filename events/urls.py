from django.urls import path
from . import views

urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()'

    # path converter if matched to return a string, if not a 404 message

    # urls paths for 'calendar'
    path('project_calendar', views.project_calendar, name='project_calendar'),
    path('<int:year>/<str:month>/', views.project_calendar, name='project_calendar'),
    
    # urls paths for 'PROJECT'
    path('all_projects', views.all_projects, name='all_projects'),
    path('add_project', views.add_project, name='add_project'),
    path('show_project/<int:project_id>/', views.show_project, name='show_project'),
    path('update_project/<int:project_id>/', views.update_project, name='update_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    
    # urls paths for 'PEOPLE'
    path('add_people', views.add_people, name='add_people'),
    path('add_tech_support', views.add_tech_support, name='add_tech_support'),
    path('all_people', views.all_people, name='all_people'),
    path('show_people/<int:people_id>/', views.show_people, name='show_people'),
    path('update_people/<int:people_id>/', views.update_people, name='update_people'),
    path('delete_people/<int:people_id>/', views.delete_people, name='delete_people'),

    # urls paths for SEARCH: 'people' and 'projects'
    path('search_people', views.search_people, name='search_people'),
    path('search_projects', views.search_projects, name='search_projects'),
    ]
