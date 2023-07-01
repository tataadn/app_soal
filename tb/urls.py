from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

# app_name = 'tb'

urlpatterns = [
    # new urls
    path('', index, name='index'),

    # URL ADMIN
    path('login-admin', login_admin, name='login_admin'),
    path('logout', logout_admin, name='logout_admin'),
    path('beranda', beranda, name='beranda'),
    # url action for guru
    path('data-pengajar', data_pengajar, name='data_pengajar'),
    path('pengajar-edt<int:id>', edit_pengajar, name='edit_pengajar'),
    path('pengajar-rmv<int:id>', hapus_pengajar, name='hapus_pengajar'),
    path('aktif-pg<int:id>', aktif_pengajar, name='aktif_pengajar'),
    path('nonaktif-pg<int:id>', nonaktif_pengajar, name='nonaktif_pengajar'),
    # show data siswa
    path('data-kelas', data_kelas, name='data_kelas'),
    path('data-7a', data_7a, name='data_7a'),
    path('data-7b', data_7b, name='data_7b'),
    path('data-7c', data_7c, name='data_7c'),
    path('data-8a', data_8a, name='data_8a'),
    path('data-8b', data_8b, name='data_8b'),
    path('data-8c', data_8c, name='data_8c'),
    path('data-9a', data_9a, name='data_9a'),
    path('data-9b', data_9b, name='data_9b'),
    path('data-9c', data_9c, name='data_9c'),
    # edit data siswa per kelas
    path('7a-<int:id>', edit_7a, name='edit_7a'),
    path('7b-<int:id>', edit_7b, name='edit_7b'),
    path('7c-<int:id>', edit_7c, name='edit_7c'),
    path('8a-<int:id>', edit_8a, name='edit_8a'),
    path('8b-<int:id>', edit_8b, name='edit_8b'),
    path('8c-<int:id>', edit_8c, name='edit_8c'),
    path('9a-<int:id>', edit_9a, name='edit_9a'),
    path('9b-<int:id>', edit_9b, name='edit_9b'),
    path('9c-<int:id>', edit_9c, name='edit_9c'),
    # hapus data per kelas
    path('hapus-7a-<int:id>', hapus_7a, name='hapus_7a'),
    path('hapus-7b-<int:id>', hapus_7b, name='hapus_7b'),
    path('hapus-7c-<int:id>', hapus_7c, name='hapus_7c'),
    path('hapus-8a-<int:id>', hapus_8a, name='hapus_8a'),
    path('hapus-8b-<int:id>', hapus_8b, name='hapus_8b'),
    path('hapus-8c-<int:id>', hapus_8c, name='hapus_8c'),
    path('hapus-9a-<int:id>', hapus_9a, name='hapus_9a'),
    path('hapus-9b-<int:id>', hapus_9b, name='hapus_9b'),
    path('hapus-9c-<int:id>', hapus_9c, name='hapus_9c'),
    # aktifkan data siswa per kelas
    path('aktif-7a-<int:id>', aktif_7a, name='aktif_7a'),
    path('aktif-7b-<int:id>', aktif_7b, name='aktif_7b'),
    path('aktif-7c-<int:id>', aktif_7c, name='aktif_7c'),
    path('aktif-8a-<int:id>', aktif_8a, name='aktif_8a'),
    path('aktif-8b-<int:id>', aktif_8b, name='aktif_8b'),
    path('aktif-8c-<int:id>', aktif_8c, name='aktif_8c'),
    path('aktif-9a-<int:id>', aktif_9a, name='aktif_9a'),
    path('aktif-9b-<int:id>', aktif_9b, name='aktif_9b'),
    path('aktif-9c-<int:id>', aktif_9c, name='aktif_9c'),
    # nonaktifkan data siswa per kelas
    path('nonaktif-7a-<int:id>', nonaktif_7a, name='nonaktif_7a'),
    path('nonaktif-7b-<int:id>', nonaktif_7b, name='nonaktif_7b'),
    path('nonaktif-7c-<int:id>', nonaktif_7c, name='nonaktif_7c'),
    path('nonaktif-8a-<int:id>', nonaktif_8a, name='nonaktif_8a'),
    path('nonaktif-8b-<int:id>', nonaktif_8b, name='nonaktif_8b'),
    path('nonaktif-8c-<int:id>', nonaktif_8c, name='nonaktif_8c'),
    path('nonaktif-9a-<int:id>', nonaktif_9a, name='nonaktif_9a'),
    path('nonaktif-9b-<int:id>', nonaktif_9b, name='nonaktif_9b'),
    path('nonaktif-9c-<int:id>', nonaktif_9c, name='nonaktif_9c'),
    # show profil admin
    path('profil', profil_admin, name='profil_admin'),




    # URL SISWA
    path('login-siswa', login_siswa, name='login_siswa'),
    path('sign-out', logout_siswa, name='logout_siswa'),
    path('index', beranda_siswa, name='index'),
    path('profil-siswa', profil_siswa, name='profil_siswa'),
    path('nilai-ujian', nilai_ujian, name='nilai_ujian'),
    path('soal-ujian', data_ujian, name='data_ujian'),
    path('soal-<int:id>', halaman_soal, name='halaman_soal'),
    path('jawaban-<int:id>', detail_jawaban, name='detail_jawaban'),




    # URL PENGAJAR
    path('login-pengajar', login_pengajar, name='login_pengajar'),
    path('signout', login_pengajar, name='login_pengajar'),
    path('dashboard', beranda_pengajar, name='dashboard'),
    path('daftar-siswa', daftarsiswa_pengajar, name='daftar_siswa'),
    path('nilai-siswa', nilai_siswa, name='nilai_siswa'),
    path('nilai-<str:kode_soal>', kd_nilai, name='kd_nilai'),
    path('profil-pengajar', profil_pengajar, name='profil_pengajar'),
    path('data-soal', data_ujian, name='data_ujian'),
    path('tambah-ujian', tambahujian, name='tambah_ujian'),
    path('edit-ujian-<int:id>', editujian, name='edit_ujian'),
    path('hapus-ujian-<int:id>', hapusujian, name='hapus_ujian'),
    path('tambah-soal', tambahsoal, name='tambah_soal'),
    path('detail-<int:id>', detail_soal, name='detail_soal'),
    path('editsoal-<int:id>', edit_soal, name='edit_soal'),
    path('hapussoal-<int:id>', hapus_soal, name='hapus_soal'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)