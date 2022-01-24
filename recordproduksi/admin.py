from django.contrib import admin
from .models import Barang, RencanaProduksi, HasilProduksi

admin.site.register(Barang)
admin.site.register(RencanaProduksi)
admin.site.register(HasilProduksi)