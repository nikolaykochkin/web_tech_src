from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'qa'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.test, name='test'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.test, name='test'),
    path('logout/', auth_views.LogoutView.as_view(next_page='qa:index'), name='logout'),
]
