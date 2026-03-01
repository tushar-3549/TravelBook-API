import pytest
from .factories import PropertyFactory, RatePlanFactory

@pytest.mark.django_db
def test_home(api_client):
    # seed a few properties
    for _ in range(3):
        p = PropertyFactory()
        RatePlanFactory(room_type__property=p)

    r = api_client.get("/api/v1/home/")
    assert r.status_code == 200
    assert "today_recommended" in r.data
    assert isinstance(r.data["today_recommended"], list)

@pytest.mark.django_db
def test_search_by_q_city_bbox_and_filters(api_client):
    p = PropertyFactory(name="Seoul Riverside")
    RatePlanFactory(room_type__property=p, nightly_price=100000, breakfast_included=True, free_cancellation=True)

    # search by q
    r = api_client.get("/api/v1/search/?q=seoul")
    assert r.status_code == 200
    assert r.data["count"] >= 1

    # bbox filters include lat/lng check
    r = api_client.get("/api/v1/search/?bbox=37.55,126.97,37.58,126.99&breakfast=1&free_cancellation=1")
    assert r.status_code == 200
    assert r.data["count"] >= 1

@pytest.mark.django_db
def test_map_tiles(api_client):
    p = PropertyFactory(lat="37.5675", lng="126.9790")
    RatePlanFactory(room_type__property=p, nightly_price=90000)
    r = api_client.get("/api/v1/search/map/?bbox=37.55,126.97,37.58,126.99")
    assert r.status_code == 200
    assert "items" in r.data and len(r.data["items"]) >= 1
