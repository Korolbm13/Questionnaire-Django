from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views


from opros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', views.index, name='begin'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('opros/', views.IndexView.as_view(), name='index'),
    path('opros/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('opros/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('opros/<int:question_id>/vote/', views.vote, name='vote'),
]
