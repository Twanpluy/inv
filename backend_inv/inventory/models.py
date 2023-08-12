from django.db import models


# Create your models here.
class InventoryCaterogorie(models.Model):
    inverntory_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class InventorySupplier(models.Model):
    inventory_supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    adress = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class InventoryProduct(models.Model):
    inventory_product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    inverntory_category_id = models.ForeignKey(
        InventoryCaterogorie, on_delete=models.CASCADE
    )
    inventory_supplier_id = models.ForeignKey(
        "InventorySupplier", on_delete=models.CASCADE
    )
    stock = models.IntegerField(blank=False, default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0.00
    )


class Inventory_picture_url(models.Model):
    inventory_picture_url_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=False, unique=True)
    filepath = models.CharField(max_length=255, blank=False, unique=True)
    filename = models.CharField(max_length=255, blank=False, unique=True)
    size = models.IntegerField(blank=False, default=0)
    file_format = models.CharField(max_length=255, blank=False, unique=True)
    inventory_product_id = models.ForeignKey(
        "InventoryProduct", on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
