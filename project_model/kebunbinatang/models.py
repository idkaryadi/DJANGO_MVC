from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length = 25)
    spesies = models.CharField(max_length = 25)
    berat = models.CharField(max_length = 25)
    umur = models.CharField(max_length = 25)

    def __str__(self):
        return self.nama


class Kandang(models.Model):
    nama = models.CharField(max_length = 25)
    isi_kandang  = models.CharField(max_length = 25)
    luas_kandang = models.CharField(max_length = 25)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length = 25)
    nomor_telepon = models.CharField(max_length = 25)
    jadwal_jaga = models.DateTimeField()

    def __str__(self):
        return self.nama