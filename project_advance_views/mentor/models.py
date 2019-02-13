from django.db import models

# Create your models here.
class Mentor(models.Model):
    images = models.CharField(max_length = 255)
    nama_lengkap = models.CharField(max_length = 255)
    experience = models.CharField(max_length = 255)
    quotes = models.TextField()
    
    def __str__(self):
        return self.nama_lengkap