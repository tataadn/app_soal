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
    path('beranda', beranda, name='beranda'),
    path('data-siswa', data_siswa, name='data_siswa'),
    path('data-pengajar', data_pengajar, name='data_pengajar'),

    # URL SISWA
    path('login-siswa', login_siswa, name='login_siswa'),

    # URL PENGAJAR
    path('login-pengajar', login_pengajar, name='login_pengajar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)