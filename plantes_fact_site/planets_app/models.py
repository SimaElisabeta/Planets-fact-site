from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator


# Create your models here.
class PlanetType(models.Model):
    TERRESTRIAL_PLANET = "TP"
    GAS_GIANT = "GGP"

    PLANET_TYPES_CATEGORY = [
        (TERRESTRIAL_PLANET, "Terrestrial Planet"),
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
    YES = "Y"
    NO = "N"
    Y_N_CHOICES = [
        (YES, "Yes"),
        (NO, "No")
    ]

    mass = models.CharField(max_length=50, default='add a value')
    gravity = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    distance_sun = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    moons_num = models.IntegerField(default=0)
    rings = models.CharField(max_length=1, choices=Y_N_CHOICES, default=YES)

    category_id = models.ForeignKey(PlanetType, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    overview = models.TextField()
    overview_source = models.URLField()
    structure = models.TextField()
    structure_source = models.URLField()
    geology = models.TextField()
    geology_source = models.URLField()
    rotation = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    revolution = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    radius = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    temperature = models.FloatField(default=0.0)
    planet_image = models.FileField(upload_to="static/images/",
                                    validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    internal_image = models.FileField(upload_to="static/images/",
                                      validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    geology_image = models.ImageField(upload_to="static/images/")

    def __str__(self):
        return self.name


class Substance(models.Model):
    HYDROGEN = "H"
    HELIUM = "HE"
    METHANE = "CH4"
    CARBON_DIOXIDE = "CO2"
    NITROGEN = "N"
    ARGON = "AR"
    OXYGEN = "O"
    SULFUR_DIOXIDE = "SO2"
    SODIUM = "NA"
    POTASSIUM = "K"

    SUBSTANCES_CHOICES = [
        (HYDROGEN, "Hydrogen"),
        (HELIUM, "Helium"),
        (METHANE, "Methane"),
        (CARBON_DIOXIDE, "Carbon Dioxide"),
        (NITROGEN, "Nitrogen"),
        (ARGON, "Argon"),
        (OXYGEN, "Oxygen"),
        (SULFUR_DIOXIDE, "Sulfur Dioxide"),
        (SODIUM, "Sodium"),
        (POTASSIUM, "Potassium")
    ]

    substance = models.CharField(max_length=3, choices=SUBSTANCES_CHOICES, unique=True, default=HYDROGEN)

    def __str__(self):
        substance_dict = dict(self.SUBSTANCES_CHOICES)
        substance_full_name = substance_dict[self.substance]
        return f"{substance_full_name}"


class AtmosphericComposition(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, default=1)
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE, default=1)
    percent = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    def __str__(self):
        return f"{self.planet.name} | {self.substance} | {self.percent}%"