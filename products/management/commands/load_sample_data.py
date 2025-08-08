from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Seeds the database with sample product data'

    def handle(self, *args, **kwargs):
        sample_products = [
            {"name": "Laptop Pro 15", "price": 1500.00, "brand": "TechBrand", "is_available": True},
            {"name": "Smartphone X", "price": 900.00, "brand": "MobileMax", "is_available": True},
            {"name": "Wireless Headphones", "price": 150.00, "brand": "SoundX", "is_available": True},
            {"name": "Gaming Console", "price": 500.00, "brand": "GameStation", "is_available": True},
            {"name": "Smartwatch 3", "price": 200.00, "brand": "TimeTech", "is_available": True},
            {"name": "Tablet Air", "price": 350.00, "brand": "TechBrand", "is_available": False},
            {"name": "Bluetooth Speaker", "price": 80.00, "brand": "SoundX", "is_available": True},
            {"name": "4K TV 55\"", "price": 700.00, "brand": "ViewMax", "is_available": True},
            {"name": "Wireless Keyboard", "price": 40.00, "brand": "TypeFast", "is_available": True},
            {"name": "Wireless Mouse", "price": 25.00, "brand": "TypeFast", "is_available": True},
            {"name": "Drone Camera", "price": 1200.00, "brand": "SkyView", "is_available": True},
            {"name": "Portable Charger", "price": 30.00, "brand": "ChargeIt", "is_available": True},
            {"name": "VR Headset", "price": 300.00, "brand": "VirtualPlay", "is_available": True},
            {"name": "Smart Home Hub", "price": 100.00, "brand": "HomeEase", "is_available": False},
            {"name": "Fitness Tracker", "price": 60.00, "brand": "FitPlus", "is_available": True}
        ]

        created_count = 0
        for product in sample_products:
            obj, created = Product.objects.get_or_create(**product)
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'{created_count} sample products added successfully!'))
