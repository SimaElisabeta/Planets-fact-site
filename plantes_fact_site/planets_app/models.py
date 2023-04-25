from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Planet(models.Model):
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
