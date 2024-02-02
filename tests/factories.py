from datetime import timezone, timedelta
import factory
from faker import providers
from client.models import Client
from faker import Faker

from mailing.models import Mailing

fake = Faker('ru_RU')


class PhoneNumberProvider(providers.BaseProvider):
    def russian_phone_number(self):
        return '7' + fake.random_int(min=1000000000, max=9999999999).__str__()[1:]


factory.Faker.add_provider(PhoneNumberProvider)


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    phone_number = factory.Faker('russian_phone_number')
    mobile_operator_code = factory.Faker('random_int', min=100, max=999)
    tag = factory.Faker('word')
    timezone = factory.Faker('timezone')


class ClientFilterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    mobile_operator_code = factory.Faker('random_int', min=100, max=999)
    tag = factory.Faker('word')


class MailingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mailing

    start_datetime = factory.Faker('date_time_this_decade', tzinfo=timezone.utc)
    end_datetime = factory.LazyAttribute(lambda o: o.start_datetime + timedelta(days=1))
    message_text = factory.Faker('text')
    client_filter = factory.Dict({
        "mobile_code": factory.Faker('random_int', min=100, max=999),
        "tag": factory.Faker('word')
    })
    time_interval = factory.LazyAttribute(
        lambda o: f"{(o.start_datetime + timedelta(hours=1)).strftime('%H:%M')}-{(o.end_datetime - timedelta(hours=1)).strftime('%H:%M')}"
    )
