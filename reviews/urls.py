from django.urls import path
from .views import PropertyReviewsView, CreateReviewView, ReviewDetailView
urlpatterns=[
    path('<int:property_id>/', PropertyReviewsView.as_view()),
    path('<int:property_id>/create/', CreateReviewView.as_view()),
    path('review/<int:pk>/', ReviewDetailView.as_view()),
]
