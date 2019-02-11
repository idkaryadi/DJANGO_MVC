from django.contrib import admin
from .models import Direksi, Mentee, Mentor, MataPelajaran, Challenge, LiveCode

# Register your models here.
my_model = [Direksi, Mentee, Mentor, MataPelajaran, Challenge, LiveCode]
admin.site.register(my_model)
