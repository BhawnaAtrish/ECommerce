from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Unique identifier for the product
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField(null=True)  # Description of the product (nullable)
    price = models.FloatField(
        null=False, default=0
    )  # Price of the product (required, default to 0)
    stock = models.PositiveIntegerField(
        null=False, default=0
    )  # Available stock quantity (required, default to 0)
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of creation
    manufacturer = models.CharField(
        max_length=255, null=True
    )  # Manufacturer of the product (nullable)
    category = models.CharField(
        max_length=100, null=False, default="other"
    )  # Product category (e.g., electronics, clothing) (required, default to "other")
    is_featured = models.BooleanField(default=False)  # Flag for featured products
    weight = models.FloatField(blank=True, null=True)  # Product weight (nullable)
    dimensions = models.CharField(
        max_length=50, blank=True, null=True
    )  # Product dimensions (nullable)
    is_available = models.BooleanField(default=True)  # Availability status
    rating = models.FloatField(blank=True, null=True)  # Product rating (nullable)
    brand = models.CharField(
        max_length=50, blank=True, null=True
    )  # Brand or manufacturer (nullable)
    is_discounted = models.BooleanField(
        default=False
    )  # Is the product currently on sale?
    discount_price = models.FloatField(
        blank=True, null=True
    )  # Discounted price (nullable)

    def __str__(self):
        return self.name  # String representation of the product (name)

    class Meta:
        db_table = "products"  # Database table name
        managed = True  # Indicates whether the table is managed by Django
