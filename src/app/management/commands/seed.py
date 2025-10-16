from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from tests.factories import SaleFactory, SaleItemFactory

class Command(BaseCommand):

    help = "Seed the database with sample sales and items."

    def add_arguments(self, parser):
        parser.add_argument(
            "-n", "--sales",
            type=int,
            default=50,
            help="Number of sales to create (default: 50).",
        )
        parser.add_argument(
            "-i", "--items",
            type=int,
            default=3,
            help="Items per sale (default: 3).",
        )

    def handle(self, *args, **options):
        sales = options["sales"]
        items = options["items"]

        if sales < 0 or items < 0:
            raise CommandError("Both --sales and --items must be non-negative integers.")

        with transaction.atomic():
            for _ in range(sales):
                sale = SaleFactory()
                for _ in range(items):
                    SaleItemFactory(sale=sale)

        self.stdout.write(self.style.SUCCESS(f"Seeded {sales} sales × {items} items each"))
