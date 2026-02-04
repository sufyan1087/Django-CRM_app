from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.register, name='register' ),
    path('login',views.login, name='login' ),
    path('dashboard',views.dashboard, name='dashboard' ),
    path('logout',views.logout, name='logout' ),
    
    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('create_record', views.create_record, name="create_record"),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('record/<int:pk>', views.singular_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    
]