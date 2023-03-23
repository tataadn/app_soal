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
    
def index_guru(request):
    return render(request, 'pg_guru/index.html', {'judul_web' : 'Halaman index guru'})
    
def list_soal(request):
    listsoal = Soal.objects.all()
    return render(request, 'pg_guru/daftar_soal.html', {'judul_web' : 'Halaman list soal guru', 'listsoal':listsoal})

def index(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'index.html', {'judul_web' : judul_web})

def beranda(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'pg_admin/index.html', {'judul_web' : judul_web})

def login_siswa(request):
    return render(request, 'auth/login_siswa.html', {'judul_web' : 'Halaman login'})

def login_pengajar(request):
    return render(request, 'auth/login_pengajar.html', {'judul_web' : 'Halaman login'})

def login_admin(request):
    return render(request, 'auth/login_admin.html', {'judul_web' : 'Halaman login'})