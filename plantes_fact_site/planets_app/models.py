from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class PlanetType(models.Model):
    TERESTRIAL_PLANET = "TP"
    GAS_GIANT = "GGP"

    PLANET_TYPES_CATEGORY = [
        (TERESTRIAL_PLANET, "Terrestrial Planet"),
        (GAS_GIANT, "Gas Giant")
    ]

    planet_category = models.CharField(max_length=3, choices=PLANET_TYPES_CATEGORY)

    def __str__(self):
        # tuple to dict conversion -> example: {'TP': 'Terrestrial Planet', 'GGP': 'Gas Giant'}
        planet_category_dict = dict(self.PLANET_TYPES_CATEGORY)

        # storing value, where self.planet_category represents the key for the value I want to store
        category_full_name = planet_category_dict[self.planet_category]
        return f"{category_full_name}"


class Planet(models.Model):
    category_id = models.ForeignKey(PlanetType, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    overview = models.TextField()
    overview_source = models.URLField()
    structure = models.TextField()
    structure_source = models.URLField()
    geology = models.TextField()
    geology_source = models.URLField()
    rotation = models.CharField(max_length=50)
    revolution = models.CharField(max_length=50)
    radius = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    planet_image = models.FileField(upload_to="static/images/",
                                    validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    internal_image = models.FileField(upload_to="static/images/",
                                      validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    geology_image = models.ImageField(upload_to="static/images/")

    def __str__(self):
        return self.name
