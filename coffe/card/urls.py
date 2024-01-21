from django.urls import path
from . import views

urlpatterns = [
    path("cards/", views.CardListCreateView.as_view(), name="card-list-create"),
    path(
        "cards/<int:pk>/",
        views.CardRetrieveUpdateDestroyView.as_view(),
        name="card-retrieve-update-destroy",
    ),
    path(
        "categories/",
        views.CategoryListCreateView.as_view(),
        name="category-list-create",
    ),
    path(
        "categories/<int:pk>/",
        views.CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-retrieve-update-destroy",
    ),
]
