from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Soal(models.Model):
    id_soal = models.CharField(primary_key=True, max_length=50)
    id_kelas = models.CharField(max_length=10, null=False)
    id_mapel = models.CharField(max_length=10, null=False)
    kode_soal = models.CharField(max_length=50, null=False)
    soal = models.TextField(null=False)
    kunci_jawaban = models.TextField(null=False)
    bobot_soal = models.IntegerField(null=False)

class User(AbstractUser):
    nomor_induk = models.CharField(max_length=200, null=False)
    nama_lengkap = models.CharField(max_length=255, null=False)
    alamat = models.TextField(null=False)
    jenis_kelamin = models.CharField(max_length=10, null=False)
    is_siswa = models.BooleanField('Is siswa',default=False)
    is_guru = models.BooleanField('Is guru',default=False)
    is_admin = models.BooleanField('Is admin',default=False)
    foto = models.ImageField(upload_to='foto/', null=True)
    id_mapel = models.CharField(max_length=10)
    id_kelas = models.CharField(max_length=10)

class Mapel(models.Model):
    id_mapel = models.CharField(primary_key=True, max_length=50)
    nama_mapel = models.CharField(max_length=100, null=False)

class Kelas(models.Model):
    id_kelas = models.CharField(primary_key=True, max_length=50)
    nama_kelas = models.CharField(max_length=50, null=False)

class Jawaban(models.Model):
    id_jawaban = models.AutoField(primary_key=True)
    id_soal = models.CharField(max_length=50, null=False)
    kode_soal = models.CharField(max_length=50, null=False)
    jawaban = models.TextField(null=False)
    nilai = models.IntegerField(null=False)

# class Siswa(models.Model):
#     nis_siswa = models.CharField(max_length=50, null=False)
#     nama_siswa = models.TextField(null=False)
#     jk_siswa = models.CharField(max_length=10, null=False)
#     alamat_siswa = models.TextField(null=False)
#     foto_siswa = models.ImageField(upload_to='foto_siswa', null=True)
#     id_kelas = models.CharField(max_length=10, null=False)

# class Guru(models.Model):
#     nip_guru = models.CharField(max_length=50, null=False)
#     nama_guru = models.TextField(null=False)
#     jk_guru = models.CharField(max_length=10, null=False)
#     alamat_guru = models.TextField(null=False)
#     foto_guru = models.ImageField(upload_to='foto_guru', null=True)
#     id_mapel = models.CharField(max_length=10, null=False)
    
    class Meta:
        managed = False
        db_table = "tb_soal"
        
    def __str__(self):
        return self.soal
    
    def __str__(self):
        return self.title
    
    