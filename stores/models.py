from django.core.validators import RegexValidator
from django.db import models


class Pizzeria(models.Model):
    """ Модель пицерии """

    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\1?\d{9,10}$')],
                                    max_length=10,
                                    blank=True)
    description = models.TextField(blank=True)
    logo_image = models.ImageField(upload_to='pizzeria_images',
                                   blank=True,
                                   default="pizzeria_images/pizza_logo.png")
    email = models.EmailField(max_length=245, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}, {}".format(self.pizzeria_name, self.city)
