from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from difflib import SequenceMatcher
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import connection
from django.core.paginator import Paginator
from django.db.models import *
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
    listweb = {
        'judul_web' : 'Beranda Admin | SMP Plus Rahmat',
        'jml_siswa' : User.objects.filter(is_siswa=True).count(),
        'jml_pengajar' : User.objects.filter(is_guru=True).count(),
    }
    return render(request, 'pg_admin/index.html', listweb)

def data_pengajar(request):
    query = """
        SELECT id, last_login, username, date_joined, nomor_induk,
        nama_lengkap, alamat, jenis_kelamin, is_guru, foto, a.id_mapel as idmapel, nama_mapel, email, is_active
        FROM tb_user a, tb_mapel b
        WHERE a.`id_mapel` = b.id_mapel
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    pengajar = []
    for row in results:
        item = {
            'id' : row[0],
            'last_login' : row[1],
            'username' : row[2],
            'date_joined' : row[3],
            'nomor_induk' : row[4],
            'nama_lengkap' : row[5],
            'alamat' : row[6],
            'jenis_kelamin' : row[7],
            'is_guru' : row[8],
            'foto' : row[9],
            'idmapel' : row[10],
            'nama_mapel' : row[11],
            'email' : row[12],
            'is_active' : row[13],
        }
        pengajar.append(item)

    listweb = {
        'judul_web' : 'Data Pengajar | SMP Plus Rahmat', 
        'sub_title' : 'DATA PENGAJAR SMP PLUS RAHMAT', 
        'mpl' : Mapel.objects.all(), 
        'pengguna' : pengajar
        # 'pengguna' : User.objects.filter(is_guru=True).order_by('date_joined'),
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

def edit_pengajar(request, id):

    if request.method == 'POST':

        if 'foto' in request.FILES:
            foto = request.FILES['foto']
            nip = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).create(foto=foto, nomor_induk=nip, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        else:
            nip = request.POST['nomor_induk']
            nama = request.POST['nama_lengkap']
            email = request.POST['email']
            alamat = request.POST['alamat']
            jk = request.POST['jenis_kelamin']
            username = request.POST['nomor_induk']
            User.objects.filter(id=id).update(nomor_induk=nip, nama_lengkap=nama, email=email, alamat=alamat, jenis_kelamin=jk, username=username)
            messages.success(request, 'Akun siswa berhasil diedit!')

        return redirect('data_pengajar')

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

def nonaktif_pengajar(request, id):
    pengajar = User.objects.get(id=id)
    pengajar.is_active = False
    pengajar.save()
    return redirect('data_pengajar')

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

def aktif_pengajar(request, id):
    pengajar = User.objects.get(id=id)
    pengajar.is_active = True
    pengajar.save()
    return redirect('data_pengajar')

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

def hapus_pengajar(request, id):
    pengajar = User.objects.get(id=id)
    pengajar.delete()
    messages.success(request, 'Akun pengajar berhasil dihapus!')
    return redirect('data_pengajar')

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

        if user is not None and user.is_siswa == True and user.is_active == True:
            login(request, user)
            return redirect('index')
        elif user.is_active == False:
            messages.error(request, 'Akun Anda Sudah Tidak Aktif! Silakan Hubungi Admin!')
            return redirect('login_siswa')
        else:
            messages.error(request, 'Username atau password anda salah!')
            return redirect('login_siswa')
    return render(request, 'pg_siswa/auth/login_siswa.html', {'judul_web' : 'Halaman login'})

def logout_siswa(request):
    logout(request)
    return redirect('login_siswa')

def beranda_siswa(request):
    id_siswa = request.user.id
    id_kelas = request.user.id_kelas

    query = """
        SELECT COUNT(DISTINCT a.`id_kdsoal`) AS count_ujian
        FROM tb_soal b
        JOIN tb_kdsoal a ON b.`id_kdsoal` = a.`id_kdsoal`
        WHERE id_kelas LIKE %s
        AND EXISTS (
        SELECT *
        FROM tb_jawaban
        WHERE tb_jawaban.`id_soal` = b.`id_soal`
        AND id_siswa = %s
        )
    """

    with connection.cursor() as cursor:
        cursor.execute(query, ['%' + id_kelas + '%', id_siswa])
        results = cursor.fetchall()

    tanggungan_ujian = []
    for row in results:
        item = {
            'count_ujian': row[0],
        }
        tanggungan_ujian.append(item)


    query2 = """
        SELECT COUNT(DISTINCT a.`id_kdsoal`) AS ujian_selesai
        FROM tb_soal b
        JOIN tb_kdsoal a ON b.`id_kdsoal` = a.`id_kdsoal`
        WHERE id_kelas LIKE %s
        AND NOT EXISTS (
        SELECT *
        FROM tb_jawaban
        WHERE tb_jawaban.`id_soal` = b.`id_soal`
        AND id_siswa = %s
        )
    """

    with connection.cursor() as cursor:
        cursor.execute(query2, ['%' + id_kelas + '%', id_siswa])
        results = cursor.fetchall()
    
    ujian_selesai = []
    for row in results:
        item = {
            'ujian_selesai': row[0],
        }
        ujian_selesai.append(item)

    listweb = {
        'judul_web' : 'Beranda | SMP Plus Rahmat',
        'tanggungan_ujian' : tanggungan_ujian,
        'ujian_selesai' : ujian_selesai,
    }
    return render(request, 'pg_siswa/index.html', listweb)

def profil_siswa(request):
    judul_web = 'Profil Saya | SMP Plus Rahmat'
    sub_title = 'PROFIL SISWA SMP PLUS RAHMAT'
    return render(request, 'pg_siswa/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def halaman_soal(request, id):
    nomorsoal = Soal.objects.filter(id_kdsoal=id)

    listweb = {
        'judul_web' : 'Soal Ujian | SMP Plus Rahmat',
        'sub_title' : 'SOAL UJIAN SISWA SMP PLUS RAHMAT',
        'nomorsoal' : nomorsoal,
    }

    if request.method == 'POST':
        id_soal_list = request.POST.getlist('id_soal[]')
        jawaban_siswa_list = request.POST.getlist('jawaban_siswa[]')
        id_siswa_list = request.POST.getlist('id_siswa[]')
        kunci_jawaban_list = request.POST.getlist('kunci_jawaban[]')
        bobot_soal_list = request.POST.getlist('bobot_soal[]')

        data_list = []
        for i in range(len(jawaban_siswa_list)):
            ratio = SequenceMatcher(None, jawaban_siswa_list[i], kunci_jawaban_list[i]).ratio()
            hasil = round(ratio * float(bobot_soal_list[i]), 2)

            data_list.append(Jawaban(
                id_soal=id_soal_list[i],
                jawaban_siswa=jawaban_siswa_list[i],
                nilai=hasil,
                id_siswa=id_siswa_list[i]
            ))
        
        Jawaban.objects.bulk_create(data_list)
        
        messages.success(request, 'Alhamdulillah! Anda telah berhasil mengerjakan soal!')
        return redirect('nilai_ujian')

    return render(request, 'pg_siswa/detail_soal.html', listweb)

def nilai_ujian(request):
    id_siswa = request.user.id

    query = """
    SELECT a.id_kdsoal AS id_kdsoal, kode_soal, nama_ujian, 
    a.`tgl_input` AS tgl_input, jumlah_soal, soal, 
    jawaban_siswa, id_siswa, c.`tgl_ujian` AS tgl_input_jawaban,
    SUM(nilai) AS nilai_siswa
    FROM tb_jawaban c, tb_soal b, tb_kdsoal a
    WHERE c.id_soal= b.`id_soal`
    AND b.`id_kdsoal` = a.`id_kdsoal`
    AND id_siswa = %s
    GROUP BY kode_soal
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [id_siswa])
        results = cursor.fetchall()

    jawaban_siswa = []
    for row in results:
        item = {
            'id_kdsoal': row[0],
            'kode_soal': row[1],
            'nama_ujian': row[2],
            'tgl_input': row[3],
            'jumlah_soal': row[4],
            'soal': row[5],
            'jawaban_siswa': row[6],
            'id_siswa': row[7],
            'tgl_input_jawaban': row[8],
            'nilai_siswa': row[9],
        }
        jawaban_siswa.append(item)

    listweb = {
        'judul_web' : 'Nilai Ujian | SMP Plus Rahmat',
        'sub_title' : 'NILAI UJIAN SISWA SMP PLUS RAHMAT',
        'jawaban_siswa': jawaban_siswa,
    }
    return render(request, 'pg_siswa/nilai_ujian.html', listweb)

def data_ujian(request):
    user_id_kelas = request.user.id_kelas
    user_id = request.user.id

    query = """
        SELECT a.`id_kdsoal` AS id_kdsoal, kode_soal, nama_ujian,
        jumlah_soal, id_kelas, a.`tgl_input` AS tgl_input
        FROM tb_soal b, tb_kdsoal a
        WHERE b.`id_kdsoal` = a.`id_kdsoal`
        AND id_kelas LIKE %s
        AND NOT EXISTS (
            SELECT *
            FROM tb_jawaban
            WHERE tb_jawaban.`id_soal` = b.`id_soal`
            AND id_siswa = %s
        )
        GROUP BY kode_soal
        ORDER BY b.`tgl_input` DESC
    """

    with connection.cursor() as cursor:
        cursor.execute(query, ['%' + user_id_kelas + '%', user_id])
        results = cursor.fetchall()

    datasoal = []
    for row in results:
        item = {
            'id_kdsoal': row[0],
            'kode_soal': row[1],
            'nama_ujian': row[2],
            'jumlah_soal': row[3],
            'id_kelas': row[4],
            'tgl_input': row[5],
        }
        datasoal.append(item)

    listweb = {
        'judul_web' : 'Soal Ujian | SMP Plus Rahmat',
        'sub_title' : 'SOAL UJIAN SISWA SMP PLUS RAHMAT',
        'datasoal' : datasoal,
    }
    return render(request, 'pg_siswa/data_ujian.html', listweb)

def detail_jawaban(request, id):
    id_siswa = request.user.id

    query = """
        SELECT id_kdsoal, soal, jawaban_siswa, nilai
        FROM tb_soal b, tb_jawaban c
        WHERE b.`id_soal` = c.id_soal
        AND id_siswa = %s
        AND id_kdsoal = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [id_siswa, id])
        results = cursor.fetchall()

    detail_jawaban = []
    for row in results:
        item = {
            'id_kdsoal': row[0],
            'soal': row[1],
            'jawaban_siswa': row[2],
            'nilai': row[3],
        }
        detail_jawaban.append(item)

    listweb ={
        'judul_web' : 'Detail Jawaban Siswa | SMP Plus Rahmat',
        'sub_title' : 'DETAIL JAWABAN SISWA SMP PLUS RAHMAT',
        'detail_jawaban': detail_jawaban,
    }
    return render(request, 'pg_siswa/detail_jawaban.html', listweb)




# PENGAJAR VIEWS
def login_pengajar(request):
    user = None
    if request.method == 'POST':
        usn_pengajar = request.POST['username']
        pwd_pengajar = request.POST['password']
        user = authenticate(request, username=usn_pengajar, password=pwd_pengajar)

        if user is not None and user.is_guru == True and user.is_active == True:
            login(request, user)
            return redirect('dashboard')
        elif user.is_active == False:
            messages.error(request, 'Akun Anda Sudah Tidak Aktif! Silakan Hubungi Admin!')
            return redirect('login_pengajar')
        else:
            messages.error(request, 'Username atau password anda salah!')
            return redirect('login_pengajar')
    return render(request, 'pg_pengajar/auth/login_pengajar.html', {'judul_web' : 'Halaman login'})

def logout_pengajar(request):
    logout(request)
    return redirect('login_pengajar')

def beranda_pengajar(request):
    iduser = request.user.id

    query = """
        SELECT soal, kunci_jawaban, id_user
        FROM tb_kdsoal a, tb_soal b
        WHERE a.`id_kdsoal` = b.`id_kdsoal`
        AND id_user = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [iduser])
        results = cursor.fetchall()

    total_soal = []
    for row in results:
        item = {
            'soal': row[0],
            'kunci_jawaban': row[1],
            'id_user': row[2]
        }
        total_soal.append(item)

    listweb = {
        'judul_web' : 'SMP Plus Rahmat',
        'jml_siswa' : User.objects.filter(is_siswa=True).count(),
        'jml_ujian' : Kdsoal.objects.filter(id_user=iduser).count(),
        'jml_soal' : len(total_soal),
    }
    return render(request, 'pg_pengajar/index.html', listweb)

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
    return render(request, 'pg_pengajar/data_siswa/daftar_siswa.html', listweb)

def nilai_siswa(request):
    listweb = {
        'judul_web' : 'Halaman Nilai Siswa | SMP Plus Rahmat',
        'sub_title' : 'NILAI SISWA SMP PLUS RAHMAT',
        'datasoal' : Kdsoal.objects.all(),
    }
    return render(request, 'pg_pengajar/data_siswa/data_kd_nilai.html', listweb)

def kd_nilai(request):
    listweb = {
        'judul_web' : 'Halaman Nilai Siswa | SMP Plus Rahmat',
        'sub_title' : 'NILAI SISWA SMP PLUS RAHMAT',
        'datasoal' : Kdsoal.objects.all(),
    }
    return render(request, 'pg_pengajar/data_siswa/index_kd_nilai.html', listweb)

def profil_pengajar(request):
    judul_web = 'Profil Saya | SMP Plus Rahmat'
    sub_title = 'PROFIL PENGAJAR SMP PLUS RAHMAT'
    return render(request, 'pg_pengajar/profil.html', {'judul_web' : judul_web, 'sub_title' : sub_title})

def data_ujian(request):
    iduser = request.user.id

    listweb = {
        'judul_web' : 'Data Soal | SMP Plus Rahmat',
        'sub_title' : 'DAFTAR SOAL SMP PLUS RAHMAT',
        # 'datasoal' : datasoal,
        'datasoal' : Kdsoal.objects.filter(id_user=iduser).order_by('-tgl_input'),
        'kls' : Kelas.objects.all(), 
    }

    return render(request, 'pg_pengajar/data_soal/data_ujian.html', listweb)

def tambahujian(request):
    if request.method == 'POST':
        kode_soal = request.POST['kode_soal']
        nama_ujian = request.POST['nama_ujian']
        jumlah_soal = request.POST['jumlah_soal']
        id_kelas = request.POST.getlist('id_kelas[]')
        id_mapel = request.POST['id_mapel']
        id_user = request.POST['id_user']

        id_kelas_str = ', '.join(id_kelas)

        Kdsoal.objects.create(kode_soal=kode_soal, nama_ujian=nama_ujian, jumlah_soal=jumlah_soal, id_kelas=id_kelas_str, id_mapel=id_mapel, id_user=id_user)
        
        return redirect('data_soal')

def editujian(request, id):
    if request.method == 'POST':
        kode_soal = request.POST['kode_soal']
        nama_ujian = request.POST['nama_ujian']
        jumlah_soal = request.POST['jumlah_soal']
        id_kelas = request.POST.getlist('id_kelas[]')

        id_kelas_str = ', '.join(id_kelas)

        Kdsoal.objects.filter(id_kdsoal=id).update(kode_soal=kode_soal, nama_ujian=nama_ujian, jumlah_soal=jumlah_soal, id_kelas=id_kelas_str)
        return redirect('data_soal')

def hapusujian(request, id):
    kdsoal = Kdsoal.objects.get(id_kdsoal=id)
    kdsoal.delete()
    return redirect('data_soal')

def detail_soal(request, id):
    listweb = {
        'judul_web' : 'Halaman Detail Soal | SMP Plus Rahmat', 
        'sub_title' : 'DETAIL SOAL SMP PLUS RAHMAT',
        'listsoal' : Soal.objects.filter(id_kdsoal=id),
        'listkode' : Kdsoal.objects.filter(id_kdsoal=id),
        'jumlahsoal' : Soal.objects.filter(id_kdsoal=id).count(),
    }
    return render(request, 'pg_pengajar/data_soal/detail_soal.html', listweb)

def tambahsoal(request):
    if request.method == 'POST':
        id_kdsoal = request.POST['id_kdsoal']
        soal = request.POST['soal']
        kunci_jawaban = request.POST['kunci_jawaban']
        bobot_soal = request.POST['bobot_soal']

        Soal.objects.create(id_kdsoal=id_kdsoal, soal=soal, kunci_jawaban=kunci_jawaban, bobot_soal=bobot_soal)
        messages.success(request, 'Berhasil menambah soal!')
        return redirect('detail_soal', id=id_kdsoal)

def edit_soal(request, id):
    if request.method == 'POST':
        id_kdsoal = request.POST['id_kdsoal']
        soal = request.POST['soal']
        kunci_jawaban = request.POST['kunci_jawaban']
        bobot_soal = request.POST['bobot_soal']

        Soal.objects.filter(id_soal=id).update(soal=soal, kunci_jawaban=kunci_jawaban, bobot_soal=bobot_soal)
        messages.success(request, 'Berhasil mengedit soal!')
        return redirect('detail_soal', id=id_kdsoal)

def hapus_soal(request, id):
    soal = Soal.objects.get(id_soal=id)
    id_kdsoal = soal.id_kdsoal
    soal.delete()
    messages.success(request, 'Berhasil menghapus soal!')
    return redirect('detail_soal', id=id_kdsoal)