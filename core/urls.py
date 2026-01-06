"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path

# Import all views from your app
from studos.views import (
    # Main Pages
    landing, 
    about, 
    contact, 
    
    # App / Task Functionality
    home, 
    toggle_task, 
    delete_task,
    
    # Service Pages
    service_resume,
    service_application,
    service_career,
    service_academic,
    service_skills,
    service_digital
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- MAIN SITE PAGES ---
    path('', landing, name='landing'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # --- SERVICE PAGES ---
    path('services/resume/', service_resume, name='service_resume'),
    path('services/application/', service_application, name='service_application'),
    path('services/career/', service_career, name='service_career'),
    path('services/academic/', service_academic, name='service_academic'),
    path('services/skills/', service_skills, name='service_skills'),
    path('services/digital/', service_digital, name='service_digital'),

    # --- APP / TASK FUNCTIONALITY ---
    path('app/', home, name='app'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]