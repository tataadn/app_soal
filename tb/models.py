from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Soal(models.Model):
    id_soal = models.CharField(primary_key=True, max_length=50)
    id_kelas = models.CharField(max_length=10, null=False)
    id_mapel = models.CharField(max_length=10, null=False)
    kode_soal = models.CharField(max_length=50, null=False)
    soal = models.TextField(null=False)
    kunci_jawaban = models.TextField(null=False)
    bobot_soal = models.IntegerField(null=False)
    id_user = models.BigIntegerField(null=False, default=1)
    tgl_input = models.DateTimeField(default=timezone.now)

class User(AbstractUser):
    nomor_induk = models.CharField(max_length=200, null=False)
    nama_lengkap = models.CharField(max_length=255, null=False)
    alamat = models.TextField(null=False)
    jenis_kelamin = models.CharField(max_length=10, null=False)
    is_siswa = models.BooleanField('Is siswa',default=False)
    is_guru = models.BooleanField('Is guru',default=False)
    is_admin = models.BooleanField('Is admin',default=False)
    foto = models.ImageField(upload_to='foto/', null=True)
    id_mapel = models.CharField(max_length=50, null=True)
    id_kelas = models.CharField(max_length=10, null=True)

class Mapel(models.Model):
    id_mapel = models.CharField(primary_key=True, max_length=50)
    nama_mapel = models.CharField(max_length=100, null=False)

class Kelas(models.Model):
    id_kelas = models.CharField(primary_key=True, max_length=50)
    nama_kelas = models.CharField(max_length=50, null=False)

class Jawaban(models.Model):
    id_jawaban = models.CharField(primary_key=True, max_length=11)
    id_soal = models.CharField(max_length=50, null=False)
    jawaban_siswa = models.TextField(null=False)
    nilai = models.IntegerField(null=False)
    id_siswa = models.BigIntegerField(null=False)
    tgl_ujian = models.DateTimeField(default=timezone.now)

class Kdsoal(models.Model):
    kode_soal = models.CharField(primary_key=True, max_length=50)
    nama_ujian = models.CharField(max_length=255, null=False)
    jumlah_soal = models.IntegerField(null=False)
    id_mapel = models.CharField(max_length=50, null=False)
    id_kelas = models.CharField(max_length=10, null=False, default=0)
    