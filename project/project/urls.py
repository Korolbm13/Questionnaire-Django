from django.contrib import admin
from django.urls import path

from opros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('opros/', views.IndexView.as_view(), name='index'),
    path('opros/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('opros/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('opros/<int:question_id>/vote/', views.vote, name='vote'),
]
