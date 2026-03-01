from django.urls import path
from .views import QuoteView, BookingCreateView, BookingDetailView, MyBookingsView

urlpatterns = [
    path('quote/', QuoteView.as_view(), name='quote'),
    path('mine/', MyBookingsView.as_view(), name='my-bookings'), 
    path('', BookingCreateView.as_view(), name='booking-create'),
    path('<str:code>/', BookingDetailView.as_view(), name='booking-detail'),
]
