from django.shortcuts import render
from django.views.generic import *
from difflib import SequenceMatcher
from .models import *
from django.views.generic.base import TemplateView
# Create your views here.

index_web = {
    'judul_web' : 'Halaman index',
}

cekdb_web = {
    'judul_web' : 'Halaman cek db',
}

def index_siswa(request):
    if request.method == 'POST':
        kalimat1 = request.POST['kalimat1']
        kalimat2 = request.POST['kalimat2']
        
        ratio = SequenceMatcher(None, kalimat1, kalimat2).ratio()
        hasil = "Nilai {0:.2f}".format(ratio*100)
        
        return render(request, 'pg-siswa/index.html', {'ratio': hasil, 'judul_web' : 'Halaman index'})
    return render(request, 'pg-siswa/index.html', index_web)

def soal_db(request):
    soal = Soal.objects.all()
    if request.method == 'POST':
        cekdb_web = request.POST['kunci_jawaban']
        jawaban = request.POST['jawaban']
        bobot_soal = request.POST['bobot_soal']

        ratio = SequenceMatcher(None, jawaban, cekdb_web).ratio()
        hasil = "Nilai {0:.2f}".format(ratio*int(bobot_soal))
        
        var_halaman = {'soal':soal, 'ratio':hasil, 'judul_web' : 'Hasil cek db'}

        return render(request,"pg-siswa/cek_db.html", var_halaman)
    else:
        return render(request,"pg-siswa/cek_db.html", {'soal':soal, 'judul_web' : 'Halaman cek db'})
    
# def index_guru(request):
#     return render(request, 'pg_guru/index.html', {'judul_web' : 'Halaman index guru'})
    
# def list_soal(request):
#     listsoal = Soal.objects.all()
#     return render(request, 'pg_guru/daftar_soal.html', {'judul_web' : 'Halaman list soal guru', 'listsoal':listsoal})

# ALL USERS VIEWS
def index(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'index.html', {'judul_web' : judul_web})


# ADMIN VIEWS
def login_admin(request):
    return render(request, 'pg_admin/auth/login_admin.html', {'judul_web' : 'Halaman login'})

def beranda(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'pg_admin/index.html', {'judul_web' : judul_web})

def data_pengajar(request):
    judul_web = 'Data Pengajar | SMP Plus Rahmat'
    sub_title = 'DATA PENGAJAR SMP PLUS RAHMAT'
    return render(request, 'pg_admin/data_pengajar.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def data_siswa(request):
    judul_web = 'Data Siswa | SMP Plus Rahmat'
    return render(request, 'pg_admin/data_siswa.html', {'judul_web' : judul_web})


# SISWA VIEWS
def login_siswa(request):
    return render(request, 'pg_siswa/auth/login_siswa.html', {'judul_web' : 'Halaman login'})

def beranda_siswa(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'pg_siswa/index.html', {'judul_web' : judul_web})

# PENGAJAR VIEWS
def login_pengajar(request):
    return render(request, 'pg_pengajar/auth/login_pengajar.html', {'judul_web' : 'Halaman login'})
