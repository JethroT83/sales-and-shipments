import factory
from orders.models import Customer, Sale, SaleItem

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta: model = Customer
    email = factory.Faker("email")

class SaleFactory(factory.django.DjangoModelFactory):
    class Meta: model = Sale
    customer = factory.SubFactory(CustomerFactory)
    status = factory.Faker("random_element", elements=["new", "processing", "paid", "failed", "cancelled"])
    total = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)

class SaleItemFactory(factory.django.DjangoModelFactory):
    class Meta: model = SaleItem
    sale = factory.SubFactory(SaleFactory)
    sku = factory.Faker("bothify", text="YOGA-###-??")
    qty = factory.Faker("pydecimal", left_digits=3, right_digits=0, positive=True)
    unit_price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
