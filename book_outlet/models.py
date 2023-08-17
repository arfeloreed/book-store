from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# from django.utils.text import slugify


# Create your models here.
# model for countries
class Country(models.Model):
    country = models.CharField(max_length=70)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return self.country

    # modify the class name shown in the admin dislpay
    class Meta:
        verbose_name_plural = "Countries"


# model for all addresses
class Address(models.Model):
    street = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.city}"

    # modify the class name shown in the admin dislpay
    class Meta:
        verbose_name_plural = "Address Entries"


# model for all authors
class Author(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


# model for all books
class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        related_name="books",
    )
    is_bestseller = models.BooleanField(default=False)
    # making a slug for title ex. Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    published_countries = models.ManyToManyField(Country)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book_info", kwargs={"slug": self.slug})

    # converting the title into a slug by overiding the save method
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
