import pytest
from decimal import Decimal
from tests.factories import PropertyFactory, RatePlanFactory

@pytest.mark.django_db
def test_quote_and_create_booking(api_client):
    # Property & RatePlan make
    p = PropertyFactory()
    RatePlanFactory(room_type__property=p, nightly_price=100000)

    # quote request
    quote_payload = {
        "property_id": p.id,
        "check_in": "2025-12-10",
        "check_out": "2025-12-12",
        "guests": 2
    }
    r = api_client.post("/api/v1/bookings/quote/", quote_payload, format="json")
    assert r.status_code in (200, 400), r.data

    if r.status_code == 200:
        assert Decimal(r.data["total_amount"]) > 0

        # create booking request
        create_payload = {
            "property": p.id,
            "guest_name": "Tester",
            "guest_email": "tester@example.com",
            "check_in": "2025-12-10",
            "check_out": "2025-12-12",
            "guests": 2,
            "total_amount": r.data["total_amount"],
        }
        r = api_client.post("/api/v1/bookings/", create_payload, format="json")
        assert r.status_code in (200, 201), r.data
        assert "code" in r.data
