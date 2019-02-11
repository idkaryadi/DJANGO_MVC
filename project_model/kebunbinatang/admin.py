from django.contrib import admin
from .models import Hewan, Kandang, Penjaga

# Register your models here.
my_model = [Hewan, Kandang, Penjaga]
admin.site.register(my_model)