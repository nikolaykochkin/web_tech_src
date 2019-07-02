from django.urls import path
from . import views


app_name = 'qa'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.test, name='test'),
    path('signup/', views.test, name='test'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.test, name='test'),
]