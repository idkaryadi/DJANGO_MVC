from django.db import models
from django.utils import timezone

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    bidang = models.CharField(max_length = 255)
    jadwal_praktik = models.DateTimeField()

    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    alamat = models.TextField(max_length = 255)
    keluhan = models.TextField(max_length = 255)

    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length = 255)
    total_harga = models.CharField(max_length = 25)
    kumpulan_obat = models.TextField(max_length = 255)
    
    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length = 255)
    kandungan = models.TextField(max_length = 255)
    khasiat = models.TextField(max_length = 255)

    def __str__(self):
        return self.nama