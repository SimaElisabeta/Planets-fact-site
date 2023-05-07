from django.contrib import admin
from .models import Planet, PlanetType, Substance, AtmosphericComposition

# Register your models here.
admin.site.register(Planet)
admin.site.register(PlanetType)
admin.site.register(Substance)
admin.site.register(AtmosphericComposition)
