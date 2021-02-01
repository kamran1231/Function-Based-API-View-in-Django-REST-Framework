
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.student_api),
    # path('studentapi/<int:pk>', views.student_api),
     path('studentapi/<int:pk>', views.StudentAPI.as_view()),
     path('studentapi/', views.StudentAPI.as_view()),
    # path('studentapi/', views.hello_world),
]
