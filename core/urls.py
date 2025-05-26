from django.urls import path
from . import views

urlpatterns = [
    path('',             views.login_view,  name='home'),
    path('login/',       views.login_view,  name='login'),
    path('logout/',      views.logout_view, name='logout'),
    path('dashboard/',   views.dashboard,   name='dashboard'),
    path('upload/',      views.upload,      name='upload'),
    path('search/',      views.search_docs, name='search'),
    path('reports/',     views.reports,     name='reports'),
    path('admin-users/', views.admin_users, name='admin_users'),
]
