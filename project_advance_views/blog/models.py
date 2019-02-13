from django.db import models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length = 255)
    images = models.CharField(max_length = 255)
    tanggal_post = models.CharField(max_length = 50)
    jumlah_komen = models.CharField(max_length = 50)
    konten = models.TextField()
    
    def __str__(self):
        return self.judul