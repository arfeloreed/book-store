from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    author = models.CharField(null=True, max_length=70)
    is_bestseller = models.BooleanField(default=False)
    # making a slug for title ex. Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book_info", kwargs={"slug": self.slug})

    # converting the title into a slug by overiding the save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
