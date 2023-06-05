from django.shortcuts import render, redirect
from django.views.generic import *
from difflib import SequenceMatcher
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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

def login_admin(request):
    user = None
    if request.method == 'POST':
        usn_admin = request.POST['username']
        pwd_admin = request.POST['password']
        user = authenticate(request, username=usn_admin, password=pwd_admin)

        if user is not None:
            login(request, user)
            return redirect('beranda')
        else:
            messages.error(request, 'Username atau password anda salah!')
            return redirect('login_admin')
    return render(request, 'pg_admin/auth/login_admin.html', {'judul_web' : 'Halaman login'})

def logout_admin(request):
    logout(request)
    return redirect('login_admin')

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

def profil_admin(request):
    judul_web = 'Profil Admin | SMP Plus Rahmat'
    sub_title = 'PROFIL ADMIN SMP PLUS RAHMAT'
    return render(request, 'pg_admin/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

# SISWA VIEWS
def login_siswa(request):
    return render(request, 'pg_siswa/auth/login_siswa.html', {'judul_web' : 'Halaman login'})

def beranda_siswa(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'pg_siswa/index.html', {'judul_web' : judul_web})

def profil_siswa(request):
    judul_web = 'Profil Saya | SMP Plus Rahmat'
    sub_title = 'PROFIL SISWA SMP PLUS RAHMAT'
    return render(request, 'pg_siswa/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def nilai_ujian(request):
    judul_web = 'Nilai Ujian | SMP Plus Rahmat'
    sub_title = 'NILAI UJIAN SISWA SMP PLUS RAHMAT'
    return render(request, 'pg_siswa/nilai_ujian.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def soal_ujian(request):
    judul_web = 'Soal Ujian | SMP Plus Rahmat'
    sub_title = 'SOAL UJIAN SISWA SMP PLUS RAHMAT'
    return render(request, 'pg_siswa/soal_ujian.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

# PENGAJAR VIEWS
def login_pengajar(request):
    return render(request, 'pg_pengajar/auth/login_pengajar.html', {'judul_web' : 'Halaman login'})

def beranda_pengajar(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'pg_pengajar/index.html', {'judul_web' : judul_web})

def profil_pengajar(request):
    judul_web = 'Profil Saya | SMP Plus Rahmat'
    sub_title = 'PROFIL PENGAJAR SMP PLUS RAHMAT'
    return render(request, 'pg_pengajar/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def data_soal(request):
    judul_web = 'Data Soal | SMP Plus Rahmat'
    sub_title = 'DAFTAR SOAL MAPEL SMP PLUS RAHMAT'
    return render(request, 'pg_pengajar/data_soal.html', {'judul_web' : judul_web, 'sub_title' : sub_title})