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
    # code = "KR"
    # name = "South Korea"
    code = factory.Sequence(lambda n: f"KR{n}")  # unique codes
    name = factory.Sequence(lambda n: f"South Korea {n}")

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

# class BookingFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Booking
#     code = factory.Sequence(lambda n: f"BK{1000+n}")
#     property = factory.SubFactory(PropertyFactory)
#     guest_name = "Alice"
#     guest_email = "alice@example.com"
#     check_in = "2025-12-10"
#     check_out = "2025-12-12"
#     guests = 2
#     total_amount = Decimal("200000")
#     status = "pending"


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    code = factory.Sequence(lambda n: f"BK{1000+n}")
    property = factory.SubFactory(PropertyFactory)
    check_in = "2025-12-10"
    check_out = "2025-12-12"
    status = "pending"

    @factory.post_generation
    def guest_name(self, create, extracted, **kwargs):
        # যদি model-এ guest_name না থাকে, কিছুই করো না
        if hasattr(self, "guest_name") and extracted:
            self.guest_name = extracted
        elif hasattr(self, "guest_name") and not extracted:
            self.guest_name = "Alice"

    @factory.post_generation
    def guest_email(self, create, extracted, **kwargs):
        if hasattr(self, "guest_email") and extracted:
            self.guest_email = extracted
        elif hasattr(self, "guest_email"):
            self.guest_email = "alice@example.com"

    @factory.post_generation
    def total_amount(self, create, extracted, **kwargs):
        if hasattr(self, "total_amount") and extracted:
            self.total_amount = extracted
        elif hasattr(self, "total_amount"):
            self.total_amount = Decimal("200000")

    @factory.post_generation
    def guests(self, create, extracted, **kwargs):
        if hasattr(self, "guests") and extracted:
            self.guests = extracted
        elif hasattr(self, "guests"):
            self.guests = 2



class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment
    booking = factory.SubFactory(BookingFactory)
    provider = "mock"
    currency = "KRW"
    amount = Decimal("200000")
    client_secret = factory.Faker("uuid4")
    status = "requires_confirmation"

