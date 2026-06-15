from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

    def ready(self):
        try:
            from inventory.models import Category, InventoryItem
            from decimal import Decimal
            from datetime import date

            if InventoryItem.objects.count() == 0:

                categories = {}

                for name in [
                    "Laptops",
                    "Desktops",
                    "Printers",
                    "Networking Devices",
                    "Monitors",
                    "UPS",
                    "Projectors",
                    "Accessories"
                ]:
                    categories[name], _ = Category.objects.get_or_create(name=name)

                items = [
                    ("LAP001", "HP EliteBook 840 G8", "Laptops", 12, 850000),
                    ("LAP002", "Dell Latitude 5420", "Laptops", 10, 900000),
                    ("LAP003", "Lenovo ThinkPad T14", "Laptops", 8, 920000),
                    ("LAP004", "MacBook Pro M2", "Laptops", 5, 1800000),
                    ("LAP005", "ASUS VivoBook 15", "Laptops", 15, 650000),

                    ("DES001", "HP ProDesk 600", "Desktops", 10, 700000),
                    ("DES002", "Dell OptiPlex 7090", "Desktops", 8, 750000),
                    ("DES003", "Lenovo ThinkCentre M70", "Desktops", 7, 730000),

                    ("PRN001", "HP LaserJet Pro M404", "Printers", 8, 280000),
                    ("PRN002", "Canon ImageRunner 2425", "Printers", 4, 450000),

                    ("NET001", "Cisco Catalyst 2960 Switch", "Networking Devices", 10, 550000),
                    ("NET002", "Cisco ISR Router", "Networking Devices", 5, 800000),
                    ("NET003", "TP-Link Archer AX55", "Networking Devices", 15, 95000),

                    ("MON001", "Dell 24-inch Monitor", "Monitors", 20, 180000),
                    ("MON002", "HP EliteDisplay 24", "Monitors", 15, 175000),

                    ("UPS001", "APC Smart UPS 1500VA", "UPS", 10, 250000),
                    ("UPS002", "Mercury Elite 2000VA", "UPS", 15, 180000),

                    ("PRO001", "Epson EB-X06", "Projectors", 4, 480000),
                    ("PRO002", "BenQ MX560", "Projectors", 3, 520000),

                    ("ACC001", "Wireless Mouse", "Accessories", 50, 12000),
                    ("ACC002", "USB Keyboard", "Accessories", 40, 15000),
                    ("ACC003", "HDMI Cable", "Accessories", 60, 5000),
                    ("ACC004", "USB Flash Drive 32GB", "Accessories", 80, 7000),
                    ("ACC005", "External Hard Drive 1TB", "Accessories", 15, 45000),
                ]

                for code, name, category, qty, cost in items:
                    InventoryItem.objects.get_or_create(
                        asset_code=code,
                        defaults={
                            "category": categories[category],
                            "name": name,
                            "description": f"{name} for organizational use",
                            "serial_number": f"SN-{code}",
                            "quantity": qty,
                            "unit_cost": Decimal(cost),
                            "status": "Available",
                            "purchase_date": date.today(),
                            "supplier": "Tech Solutions Nigeria Ltd"
                        }
                    )

        except Exception:
            pass