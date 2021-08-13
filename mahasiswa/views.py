from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import MahasiswaModel
from .forms import MahasiswaForm


@login_required(login_url='login')
def mahasiswa(request):
    data_mhs = MahasiswaModel.objects.all()
    context = {
        'title': 'Data Mahasiswa',
        'header': 'Data Mahasiswa',
        'data_mhs': data_mhs,
    }

    return render(request, 'mahasiswa/index.html', context)


@login_required(login_url='login')
def create(request):
    form_mhs = MahasiswaForm()

    if request.method == 'POST':
        form_mhs = MahasiswaForm(request.POST)
        if form_mhs.is_valid():
            form_mhs.save()

            return redirect('mahasiswa:index')

    context = {
        'title': 'Data Mahasiswa',
        'header': 'Tambah Data Mahasiswa',
        'form_mhs': form_mhs,
    }

    return render(request, 'mahasiswa/create.html', context)


@login_required(login_url='login')
def update(request, updateId):
    mhs = MahasiswaModel.objects.get(pk=updateId)
    form_mhs = MahasiswaForm(instance=mhs)

    if request.method == 'POST':
        form_mhs = MahasiswaForm(request.POST, instance=mhs)
        if form_mhs.is_valid():
            form_mhs.save()

            return redirect('mahasiswa:index')

    context = {
        'title': 'Data Mahasiswa',
        'header': 'Update Data Mahasiswa',
        'form_mhs': form_mhs,
    }

    return render(request, 'mahasiswa/create.html', context)


@login_required(login_url='login')
def delete(requset, deleteId):
    data_mhs = MahasiswaModel.objects.get(pk=deleteId)
    data_mhs.delete()

    return redirect('mahasiswa:index')
