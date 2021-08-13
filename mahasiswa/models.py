from django.db import models

# Create your models here.


class MahasiswaModel(models.Model):
    nama = models.CharField(max_length=250)
    nim = models.IntegerField()
    kelas = models.CharField(max_length=250)
    shift = models.CharField(
        max_length=250,
        choices=(
            ('Reguler A', 'Reg A'),
            ('Reguler B', 'Reg B'),
            ('Reguler C', 'Reg C'),
        ),
        default='Reg A',
    )
    jurusan = models.CharField(
        max_length=250,
        choices=(
            ('Akutansi', 'Akutansi'),
            ('Biologi', 'Biologi'),
            ('Fisika', 'Fisika'),
            ('Ekonomi', 'Ekonomi'),
            ('Hukum', 'Hukum'),
            ('Ilmu Komputer', 'Ilmu Komputer'),
            ('Politik', 'Politik'),
        ),
        default='Akutansi'
    )

    def __str__(self):
        return self.nama
