from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from difflib import SequenceMatcher
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import connection
from django.core.paginator import Paginator
from django.urls import reverse_lazy
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



# ALL USERS VIEWS
def index(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'index.html', {'judul_web' : judul_web})


# ADMIN VIEWS
def login_admin(request):
    user = None
    if request.method == 'POST':
        usn_admin = request.POST['username']
        pwd_admin = request.POST['password']
        user = authenticate(request, username=usn_admin, password=pwd_admin)

        if user is not None and user.is_admin == True:
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
    listweb = {
        'judul_web' : 'Data Pengajar | SMP Plus Rahmat', 
        'sub_title' : 'DATA PENGAJAR SMP PLUS RAHMAT', 
        'mpl' : Mapel.objects.all(), 
        'pengguna' : User.objects.filter(is_guru=True).order_by('date_joined'),
    }
    
    if request.method == 'POST':
        foto = request.FILES['foto']
        nip = request.POST['nomor_induk']
        nama = request.POST['nama_lengkap']
        email = request.POST['email']
        alamat = request.POST['alamat']
        jk = request.POST['jenis_kelamin']
        is_guru = request.POST['is_guru']
        mapel = request.POST['id_mapel']
        username = request.POST['nomor_induk']
        password = request.POST['password']
        
        User.objects.create_user(foto=foto, nomor_induk=nip, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, is_guru=is_guru, id_mapel=mapel, username=username, password=password,)
        messages.success(request, 'Akun berhasil ditambahkan!')
        return redirect('data_pengajar')
    
    return render(request, 'pg_admin/pengajar_page/data_pengajar.html', listweb)

def data_kelas(request):
    listweb = {
        'judul_web' : 'Data Kelas | SMP Plus Rahmat', 
        'kls' : Kelas.objects.all(),
    }

    if request.method == 'POST':
        foto = request.FILES['foto']
        nisn = request.POST['nomor_induk']
        nama = request.POST['nama_lengkap']
        email = request.POST['email']
        alamat = request.POST['alamat']
        jk = request.POST['jenis_kelamin']
        is_siswa = request.POST['is_siswa']
        kelas = request.POST['id_kelas']
        username = request.POST['nomor_induk']
        password = request.POST['password']

        User.objects.create_user(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, is_siswa=is_siswa, id_kelas=kelas, username=username, password=password,)
        messages.success(request, 'Akun siswa berhasil ditambahkan!')
        return redirect('data_kelas')

    return render(request, 'pg_admin/siswa_page/data_kelas.html', listweb)

def data_7a(request):
    listweb = {
        'judul_web' : 'Data Kelas 7A | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 7A SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='7A').order_by('nama_lengkap')
    }

    return render(request, 'pg_admin/siswa_page/data_7a.html', listweb)

def data_7b(request):
    listweb = {
        'judul_web' : 'Data Kelas 7B | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 7B SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='7B').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_7b.html', listweb)

def data_7c(request):
    listweb = {
        'judul_web' : 'Data Kelas 7C | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 7C SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='7C').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_7c.html', listweb)

def data_8a(request):
    listweb = {
        'judul_web' : 'Data Kelas 8A | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 8A SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='8A').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_8a.html', listweb)

def data_8b(request):
    listweb = {
        'judul_web' : 'Data Kelas 8B | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 8B SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='8B').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_8b.html', listweb)

def data_8c(request):
    listweb = {
        'judul_web' : 'Data Kelas 8C | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 8C SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='8C').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_8c.html', listweb)

def data_9a(request):
    listweb = {
        'judul_web' : 'Data Kelas 9A | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 9A SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='9A').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_9a.html', listweb)

def data_9b(request):
    listweb = {
        'judul_web' : 'Data Kelas 9B | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 9B SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='9B').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_9b.html', listweb)

def data_9c(request):
    listweb = {
        'judul_web' : 'Data Kelas 9C | SMP Plus Rahmat', 
        'sub_title' : 'DATA KELAS 9C SMP PLUS RAHMAT', 
        'siswa' : User.objects.filter(is_siswa=True, id_kelas='9C').order_by('nama_lengkap')
    }
    return render(request, 'pg_admin/siswa_page/data_9c.html', listweb)

def edit_7a(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_7a')
    
def edit_7b(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_7b')

def edit_7c(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_7c')
    
def edit_8a(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_8a')
    
def edit_8b(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_8b')
    
def edit_8c(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_8c')
    
def edit_9a(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_9a')
    
def edit_9b(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_9b')

def edit_9c(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nisn = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nisn, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_9c')

def nonaktif_7a(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_7a')

def nonaktif_7b(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_7b')

def nonaktif_7c(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_7c')

def nonaktif_8a(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_8a')

def nonaktif_8b(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_8b')

def nonaktif_8c(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_8c')

def nonaktif_9a(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_9a')

def nonaktif_9b(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_9b')

def nonaktif_9c(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = False
    siswa.save()
    return redirect('data_9c')

def aktif_7a(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_7a')

def aktif_7b(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_7b')

def aktif_7c(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_7c')

def aktif_8a(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_8a')

def aktif_8b(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_8b')

def aktif_8c(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_8c')

def aktif_9a(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_9a')

def aktif_9b(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_9b')

def aktif_9c(request, id):
    siswa = User.objects.get(id=id)
    siswa.is_active = True
    siswa.save()
    return redirect('data_9c')

def hapus_7a(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_7a')

def hapus_7b(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_7b')

def hapus_7c(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_7c')

def hapus_8a(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_8a')

def hapus_8b(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_8b')

def hapus_8c(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_8c')

def hapus_9a(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_9a')

def hapus_9b(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_9b')

def hapus_9c(request, id):
    siswa = User.objects.get(id=id)
    siswa.delete()
    messages.success(request, 'Akun siswa berhasil dihapus!')
    return redirect('data_9c')

def profil_admin(request):
    judul_web = 'Profil Admin | SMP Plus Rahmat'
    sub_title = 'PROFIL ADMIN SMP PLUS RAHMAT'
    return render(request, 'pg_admin/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})




# SISWA VIEWS
def login_siswa(request):
    user = None
    if request.method == 'POST':
        usn_siswa = request.POST['username']
        pwd_siswa = request.POST['password']
        user = authenticate(request, username=usn_siswa, password=pwd_siswa)

        if user is not None and user.is_siswa == True:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username atau password anda salah!')
            return redirect('login_siswa')
    return render(request, 'pg_siswa/auth/login_siswa.html', {'judul_web' : 'Halaman login'})

def logout_siswa(request):
    logout(request)
    return redirect('login_siswa')

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
    user_id_kelas = request.user.id_kelas
    
    query = """
    SELECT a.`id_soal` AS id, b.nama_kelas AS kelas, a.`kode_soal`, c.`nama_mapel`,
           GROUP_CONCAT(a.soal SEPARATOR ',') AS banyak_soal,
           (LENGTH(GROUP_CONCAT(a.soal SEPARATOR ',')) - LENGTH(REPLACE(GROUP_CONCAT(a.soal SEPARATOR ','), ',', '')) + 1) AS jumlah_soal
    FROM tb_soal a, tb_kelas b, tb_mapel c
    WHERE b.id_kelas = a.id_kelas
    AND a.`id_mapel` = c.`id_mapel`
    AND b.`id_kelas` = %s
    GROUP BY a.`kode_soal`, b.id_kelas
    ORDER BY b.id_kelas
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [user_id_kelas])
        results = cursor.fetchall()

    datasoal = []
    for row in results:
        item = {
            'id_soal': row[0],
            'nama_kelas': row[1],
            'kode_soal': row[2],
            'mapel': row[3],
            'banyak_soal': row[4],
            'jumlah_soal': row[5],
        }
        datasoal.append(item)

    listweb = {
        'judul_web' : 'Soal Ujian | SMP Plus Rahmat',
        'sub_title' : 'SOAL UJIAN SISWA SMP PLUS RAHMAT',
        'datasoal' : datasoal,
    }
    return render(request, 'pg_siswa/soal_ujian.html', listweb)

def halaman_soal(request, kode_soal):
    id_kelas = request.user.id_kelas
    nomorsoal = Soal.objects.filter(kode_soal=kode_soal, id_kelas=id_kelas)
    paginator = Paginator(nomorsoal, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    listweb = {
        'judul_web' : 'Soal Ujian | SMP Plus Rahmat',
        'sub_title' : 'SOAL UJIAN SISWA SMP PLUS RAHMAT',
        'nomorsoal' : nomorsoal,
        'page_obj' : page_obj,
    }

    return render(request, 'pg_siswa/detail_soal.html', listweb)



# PENGAJAR VIEWS
def login_pengajar(request):
    user = None
    if request.method == 'POST':
        usn_pengajar = request.POST['username']
        pwd_pengajar = request.POST['password']
        user = authenticate(request, username=usn_pengajar, password=pwd_pengajar)

        if user is not None and user.is_guru == True:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username atau password anda salah!')
            return redirect('login_pengajar')
    return render(request, 'pg_pengajar/auth/login_pengajar.html', {'judul_web' : 'Halaman login'})

def logout_pengajar(request):
    logout(request)
    return redirect('login_pengajar')

def beranda_pengajar(request):
    judul_web = 'SMP Plus Rahmat'
    return render(request, 'pg_pengajar/index.html', {'judul_web' : judul_web})

def daftarsiswa_pengajar(request):
    listweb = {
        'judul_web' : 'Halaman Data Siswa | SMP Plus Rahmat', 
        'sub_title' : 'DATA SISWA SMP PLUS RAHMAT',
        'kls7a' : User.objects.filter(is_siswa=True, id_kelas='7A').order_by('nama_lengkap'),
        'kls7b' : User.objects.filter(is_siswa=True, id_kelas='7B').order_by('nama_lengkap'),
        'kls7c' : User.objects.filter(is_siswa=True, id_kelas='7C').order_by('nama_lengkap'),
        'kls8a' : User.objects.filter(is_siswa=True, id_kelas='8A').order_by('nama_lengkap'),
        'kls8b' : User.objects.filter(is_siswa=True, id_kelas='8B').order_by('nama_lengkap'),
        'kls8c' : User.objects.filter(is_siswa=True, id_kelas='8C').order_by('nama_lengkap'),
        'kls9a' : User.objects.filter(is_siswa=True, id_kelas='9A').order_by('nama_lengkap'),
        'kls9b' : User.objects.filter(is_siswa=True, id_kelas='9B').order_by('nama_lengkap'),
        'kls9c' : User.objects.filter(is_siswa=True, id_kelas='9C').order_by('nama_lengkap')
    }
    return render(request, 'pg_pengajar/daftar_siswa.html', listweb)

def profil_pengajar(request):
    judul_web = 'Profil Saya | SMP Plus Rahmat'
    sub_title = 'PROFIL PENGAJAR SMP PLUS RAHMAT'
    return render(request, 'pg_pengajar/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def data_soal(request):
    query = """
    SELECT b.nama_kelas AS kelas, a.kode_soal AS kodesoal, c.nama_mapel AS mapel,
           GROUP_CONCAT(a.soal SEPARATOR ',') AS banyak_soal,
           (LENGTH(GROUP_CONCAT(a.soal SEPARATOR ',')) - LENGTH(REPLACE(GROUP_CONCAT(a.soal SEPARATOR ','), ',', '')) + 1) AS jumlah_soal
    FROM tb_soal a, tb_kelas b, tb_mapel c
    WHERE b.id_kelas = a.id_kelas
    AND a.id_mapel = c.id_mapel
    GROUP BY a.kode_soal, b.id_kelas
    ORDER BY b.id_kelas
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    datasoal = []
    for row in results:
        item = {
            'nama_kelas': row[0],
            'kode_soal': row[1],
            'mapel': row[2],
            'banyak_soal': row[3],
            'jumlah_soal': row[4],
        }
        datasoal.append(item)

    listweb = {
        'judul_web' : 'Data Soal | SMP Plus Rahmat',
        'sub_title' : 'DAFTAR SOAL MAPEL SMP PLUS RAHMAT',
        'datasoal' : datasoal,
    }

    return render(request, 'pg_pengajar/data_soal.html', listweb)

def tambahsoal(request):
    listweb = {
        'judul_web' : 'Halaman Tambah Soal | SMP Plus Rahmat', 
        'sub_title' : 'SOAL UJIAN SMP PLUS RAHMAT',
        'kls' : Kelas.objects.all(), 
    }
    if request.method == 'POST':
        id_kelas_list = request.POST.getlist('id_kelas[]')
        id_mapel_list = request.POST.getlist('id_mapel[]')
        kode_soal_list = request.POST.getlist('kode_soal[]')
        soal_list = request.POST.getlist('soal[]')
        kunci_jawaban_list = request.POST.getlist('kunci_jawaban[]')
        bobot_soal_list = request.POST.getlist('bobot_soal[]')
        id_user_list = request.POST.getlist('id_user[]')

        for i in range(len(soal_list)):

            question = Soal(
                id_kelas=id_kelas_list[i],
                id_mapel=id_mapel_list[i],
                kode_soal=kode_soal_list[i],
                soal=soal_list[i],
                kunci_jawaban=kunci_jawaban_list[i],
                bobot_soal=bobot_soal_list[i],
                id_user=id_user_list[i]
            )
            question.save()
    
        messages.success(request, 'Data saved successfully.')
        return redirect('tambah_soal')

    return render(request, 'pg_pengajar/tambah_soal.html', listweb)