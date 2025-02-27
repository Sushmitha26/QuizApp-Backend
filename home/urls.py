from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('adminpage/create/', views.create_quiz, name='create_quiz'),
    path('adminpage/list/', views.list_questions, name='list_questions'),
    path('adminpage/update/<int:question_id>/', views.update_quiz, name='update_quiz'),
    path('adminpage/delete/<int:question_id>/', views.delete_quiz, name='delete_quiz'),
]