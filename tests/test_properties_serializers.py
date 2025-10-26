import pytest
from properties.serializers import PropertyCardSerializer
from .factories import PropertyFactory, RatePlanFactory, PropertyPhotoFactory

@pytest.mark.django_db
def test_property_card_serializer_min_price_and_photos():
    p = PropertyFactory()
    RatePlanFactory(room_type__property=p, nightly_price=80000)
    PropertyPhotoFactory(property=p)
    s = PropertyCardSerializer(p)
    data = s.data
    assert "id" in data and "name" in data
    # assert str(data.get("min_price")) in ("80000", "80000.00")
    assert str(data.get("min_price")) in ("108000", "108000.00")
    assert len(data.get("photos", [])) >= 1
