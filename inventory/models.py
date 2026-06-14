from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    asset_code = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    serial_number = models.CharField(
        max_length=100,
        unique=True
    )

    quantity = models.PositiveIntegerField()

    unit_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        default="Available"
    )

    purchase_date = models.DateField()

    supplier = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.name


class StockTransaction(models.Model):

    TRANSACTION_TYPES = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    )

    item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    quantity = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    transaction_date = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.item.name} - {self.transaction_type}"


class AssetAssignment(models.Model):

    item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE
    )

    assigned_to = models.CharField(
        max_length=100
    )

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    assigned_date = models.DateTimeField(
        auto_now_add=True
    )

    return_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='Assigned'
    )

    condition = models.CharField(
        max_length=50,
        default='Good'
    )

    department = models.CharField(
        max_length=100,
        default='CGI Artist'
    )

    purpose = models.TextField()



    def __str__(self):
        return self.assigned_to


class AuditLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=100
    )

    description = models.TextField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.action