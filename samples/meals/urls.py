from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.MealListView.as_view()),
    path('meals', views.MealListView.as_view(), name='meals'),
    path('meal/<int:pk>', views.MealDetailView.as_view(), name='meal_detail'),
    path('meal/create', 
        views.MealCreateView.as_view(success_url=reverse_lazy('meals')), name='meal_create'),
    path('meal/<int:pk>/update', 
        views.MealUpdateView.as_view(success_url=reverse_lazy('meals')), name='meal_update'),
    path('meal/<int:pk>/delete', 
        views.MealDeleteView.as_view(success_url=reverse_lazy('meals')), name='meal_delete'),
]

