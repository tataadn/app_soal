from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('siswa', index_siswa, name='index_siswa'),
    path('siswa-soal', soal_db, name='soal_db'),
    path('guru', index_guru, name='index_guru'),
    path('guru-datasoal', list_soal, name='list_soal'),
    path('beranda', beranda, name='beranda'),
    path('login-siswa', login_siswa, name='login_siswa'),
    path('login-pengajar', login_pengajar, name='login_pengajar'),
    path('login-admin', login_admin, name='login_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)