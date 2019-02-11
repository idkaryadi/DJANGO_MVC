from django.db import models
from django.utils import timezone

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    no_telepon = models.CharField(max_length = 25)
    jabatan = models.CharField(max_length = 25)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    no_telepon = models.CharField(max_length = 25)
    no_absen = models.CharField(max_length = 25)
    nilai_rata_rata = models.CharField(max_length = 5)

    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length = 255)
    jadwal_dimulai = models.DateTimeField(max_length = 25)
    jadwal_berakhir = models.DateTimeField(max_length = 25)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    no_telepon = models.CharField(max_length = 25)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 255)
    banyak_soal = models.CharField(max_length = 25)
    bobot_nilai = models.CharField(max_length = 25)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length = 255)
    banyak_soal = models.CharField(max_length = 25)
    bobot_nilai = models.CharField(max_length = 25)
    tanggal_pelaksanaan = models.DateTimeField(max_length = 25)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return self.nama_live_code