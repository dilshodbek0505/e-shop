from django.db import models
from django.core.validators import MinValueValidator



class Product(models.Model):
    CATEGORY = (
        ("gold", "gold"),
        ("silver", "silver"),
        ("bronza", "bronza"),
    )


    name = models.CharField(
        max_length=255,
        help_text="Maxsulot nomi",
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY,
        help_text="Maxsulot kategoriyasi!"
    )
    price = models.FloatField(
        default=0.0,
        help_text="Maxsulot narxi",
        validators=[MinValueValidator(0.0, "Narx manfiy son bo'lishi mumkin emas")]
    )
    description = models.TextField( help_text="Maxsulot uchun tarif")
    image = models.ImageField(
        upload_to="product/images/",
        help_text="Maxsulot rasmi"
    )
    
    @property
    def product_name(self):
        return f"{self.name}-{self.category}"

    
    def __str__(self) -> str:
        return self.product_name
