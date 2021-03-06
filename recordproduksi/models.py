from django.db import models
from django.utils.translation import gettext_lazy as _

class Barang(models.Model):
    part_number = models.CharField(max_length=18, unique=True)
    description = models.CharField(max_length=32)
    color_code = models.CharField(max_length=6, blank=True)

    def __str__(self):
        judul_barang = self.part_number + " --- " + self.description
        return judul_barang

class RencanaProduksi(models.Model):
    tanggal = models.DateTimeField()
    class StatusRencana(models.TextChoices):
        ACTIVE = 'A', _('Active')
        CANCELED = 'C', _('Canceled')

    status = models.CharField(max_length=1, choices=StatusRencana.choices, default=StatusRencana.ACTIVE)

    def __str__(self):
        judul = "Rencana Produksi" + " " + str(self.tanggal)
        return judul

class RencanaProduksiDetail(models.Model):
    line_number = models.IntegerField()
    rencana_produksi = models.ForeignKey(RencanaProduksi, on_delete=models.CASCADE, related_name='details')
    part_number = models.ForeignKey(Barang, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        judul = str(self.line_number) + " " + self.part_number.part_number
        return judul

class HasilProduksi(models.Model):
    rencana_produksi = models.ForeignKey(RencanaProduksi, on_delete=models.CASCADE)
    timestamp = models.TimeField()

    def __str__(self):
        judul = "Hasil Produksi " + str(self.rencana_produksi.tanggal)
        return judul

class HasilProduksiDetail(models.Model):
    hasil_produksi = models.ForeignKey(HasilProduksi, on_delete=models.CASCADE, related_name='details')
    part_number = models.ForeignKey(Barang, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class StatusOutput(models.TextChoices):
        OK_DIRECT = 'OKD', _('OK Direct')
        OK_BUFF_BINTIK = 'OKB1', _('OK Buffing Bintik')
        OK_BUFF_OP = 'OKB2', _('OK Buffing OP')
        OK_BUFF_DIRTY = 'OKB3', _('OK Buffing Dirty')
        OK_BUFF_DENT = 'OKB4', _('OK Buffing Dent')
        OK_BUFF_SCRATCH = 'OKB5', _('OK Buffing Scratch')
        NG_BARRY = 'NG1', _('NG Barry')
        NG_SAGGING = 'NG2', _('NG Sagging')
        NG_CRATER = 'NG3', _('NG Crater')
        NG_TIPIS = 'NG4', _('NG Tipis')
        NG_SERAT = 'NG5', _('NG Serat')
        NG_POP = 'NG6', _('NG Pop')

    status = models.CharField(max_length=4, choices=StatusOutput.choices, default=StatusOutput.OK_DIRECT)