from django.db import models

# Create your models here.


class Contact(models.Model):
    GENDER = (
        ("Pria", "Pria"),
        ("Wanita", "Wanita"),
    )

    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=225, unique=True)
    phone = models.CharField(max_length=15)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=9, choices=GENDER, null=True, blank=True
    )
    picture = models.ImageField(upload_to="picture/", null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "contact"
