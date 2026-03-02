import pytest
from rest_framework import status
from tests.factories import PropertyFactory, BookingFactory, UserFactory
from reviews.models import Review

@pytest.mark.django_db
class TestStandardMethods:

    def test_me_view_methods(self, auth_client, user):
        # PATCH
        r = auth_client.patch('/api/v1/me/', {'phone': '123456'}, format='json')
        assert r.status_code == status.HTTP_200_OK
        assert r.data['phone'] == '123456'

        # PUT
        payload = {
            'username': user.username,
            'email': user.email,
            'phone': '654321',
            'language': 'en',
            'currency': 'USD'
        }
        r = auth_client.put('/api/v1/me/', payload, format='json')
        assert r.status_code == status.HTTP_200_OK
        assert r.data['phone'] == '654321'

        # DELETE (deactivate)
        r = auth_client.delete('/api/v1/me/')
        assert r.status_code == status.HTTP_204_NO_CONTENT
        user.refresh_from_db()
        assert user.is_active is False

    def test_property_detail_methods(self, auth_client):
        prop = PropertyFactory()
        url = f'/api/v1/accommodations/{prop.id}/'

        # PATCH
        r = auth_client.patch(url, {'name': 'Updated Name'}, format='json')
        assert r.status_code == status.HTTP_200_OK
        assert r.data['name'] == 'Updated Name'

        # PUT
        payload = {
            'name': 'Fully Updated Hotel',
            'category': 'resort',
            'address': prop.address,
            'city_id': prop.city.id,
            'lat': str(prop.lat),
            'lng': str(prop.lng),
            'base_price': '150000.00'
        }
        r = auth_client.put(url, payload, format='json')
        assert r.status_code == status.HTTP_200_OK
        assert r.data['name'] == 'Fully Updated Hotel'
        
        # DELETE
        r = auth_client.delete(url)
        assert r.status_code == status.HTTP_204_NO_CONTENT
        from properties.models import Property
        assert not Property.objects.filter(id=prop.id).exists()

    def test_booking_detail_methods(self, auth_client):
        booking = BookingFactory(user=auth_client.handler._force_user if hasattr(auth_client.handler, '_force_user') else None)
        # Using factory might not auto-link auth_client user, but BookingDetailView doesn't check owner currently
        url = f'/api/v1/bookings/{booking.code}/'

        # PATCH
        r = auth_client.patch(url, {'status': 'confirmed'}, format='json')
        assert r.status_code == status.HTTP_200_OK
        assert r.data['status'] == 'confirmed'

        # DELETE
        r = auth_client.delete(url)
        assert r.status_code == status.HTTP_204_NO_CONTENT
        from bookings.models import Booking
        assert not Booking.objects.filter(code=booking.code).exists()

    def test_review_methods(self, auth_client, user):
        prop = PropertyFactory()
        review = Review.objects.create(property=prop, user=user, rating=5, content="Great!")
        url = f'/api/v1/reviews/review/{review.id}/'

        # GET
        r = auth_client.get(url)
        assert r.status_code == status.HTTP_200_OK
        assert r.data['content'] == "Great!"

        # PATCH
        r = auth_client.patch(url, {'content': 'Updated Review'}, format='json')
        assert r.status_code == status.HTTP_200_OK
        assert r.data['content'] == 'Updated Review'

        # DELETE
        r = auth_client.delete(url)
        assert r.status_code == status.HTTP_204_NO_CONTENT
        assert not Review.objects.filter(id=review.id).exists()
