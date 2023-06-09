from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('siswa', index_siswa, name='index_siswa'),
    path('siswa-soal', soal_db, name='soal_db'),

    # path('guru', index_guru, name='index_guru'),
    # path('guru-datasoal', list_soal, name='list_soal'),
    

    # new urls

    # URL ADMIN
    path('login-admin', login_admin, name='login_admin'),
    path('logout', logout_admin, name='logout_admin'),
    path('beranda', beranda, name='beranda'),
    path('data-siswa', data_siswa, name='data_siswa'),
    path('data-7a', data_7a, name='data_7a'),
    path('data-7b', data_7b, name='data_7b'),
    path('data-7c', data_7c, name='data_7c'),
    path('data-8a', data_8a, name='data_8a'),
    path('data-8b', data_8b, name='data_8b'),
    path('data-8c', data_8c, name='data_8c'),
    path('data-9a', data_9a, name='data_9a'),
    path('data-9b', data_9b, name='data_9b'),
    path('data-9c', data_9c, name='data_9c'),
    path('data-pengajar', data_pengajar, name='data_pengajar'),
    path('profil', profil_admin, name='profil_admin'),

    # URL SISWA
    path('login-siswa', login_siswa, name='login_siswa'),
    path('sign-out', logout_siswa, name='logout_siswa'),
    path('index', beranda_siswa, name='index'),
    path('profil-siswa', profil_siswa, name='profil_siswa'),
    path('nilai-ujian', nilai_ujian, name='nilai_ujian'),
    path('soal-ujian', soal_ujian, name='soal_ujian'),

    # URL PENGAJAR
    path('login-pengajar', login_pengajar, name='login_pengajar'),
    path('signout', login_pengajar, name='login_pengajar'),
    path('dashboard', beranda_pengajar, name='dashboard'),
    path('profil-pengajar', profil_pengajar, name='profil_pengajar'),
    path('data-soal', data_soal, name='data_soal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)