import factory
from decimal import Decimal
from faker import Faker
from accounts.models import User
from locations.models import Country, City
from properties.models import Amenity, Property, RoomType, RatePlan, PropertyPhoto
from bookings.models import Booking
from payments.models import Payment

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@ex.com")
    password = factory.PostGenerationMethodCall('set_password', 'pass1234')

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    code = "KR"
    name = "South Korea"

class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City
    country = factory.SubFactory(CountryFactory)
    name = "Seoul"
    lat = Decimal("37.5665")
    lng = Decimal("126.9780")

class AmenityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Amenity
    name = factory.Iterator(["Free WiFi", "Breakfast", "Pool"])
    icon = "wifi"

class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property
    name = factory.Sequence(lambda n: f"Hotel {n}")
    category = "hotel"
    city = factory.SubFactory(CityFactory)
    address = factory.LazyFunction(lambda: fake.address().replace("\n", " "))
    lat = Decimal("37.5670")
    lng = Decimal("126.9785")
    rating = Decimal("4.3")
    review_count = 25
    base_price = Decimal("120000")
    discount_percent = 10

    @factory.post_generation
    def amenities(self, create, extracted, **kwargs):
        if not create:
            return
        a1 = AmenityFactory(name="Free WiFi", icon="wifi")
        self.amenities.add(a1)

class RoomTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RoomType
    property = factory.SubFactory(PropertyFactory)
    name = "Deluxe Room"
    max_guests = 2
    beds = "1 Queen"

class RatePlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RatePlan
    room_type = factory.SubFactory(RoomTypeFactory)
    name = "Standard"
    currency = "KRW"
    nightly_price = Decimal("100000")
    breakfast_included = True
    free_cancellation = True
    free_wifi = True

class PropertyPhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PropertyPhoto
    property = factory.SubFactory(PropertyFactory)
    image_url = factory.LazyFunction(lambda: f"https://picsum.photos/seed/{fake.uuid4()}/800/600")

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking
    code = factory.Sequence(lambda n: f"BK{1000+n}")
    property = factory.SubFactory(PropertyFactory)
    guest_name = "Alice"
    guest_email = "alice@example.com"
    check_in = "2025-12-10"
    check_out = "2025-12-12"
    guests = 2
    total_amount = Decimal("200000")
    status = "pending"

class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment
    booking = factory.SubFactory(BookingFactory)
    provider = "mock"
    currency = "KRW"
    amount = Decimal("200000")
    client_secret = factory.Faker("uuid4")
    status = "requires_confirmation"
