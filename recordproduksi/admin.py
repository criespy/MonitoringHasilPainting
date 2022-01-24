from django.contrib import admin
from .models import Barang, RencanaProduksi, HasilProduksi, RencanaProduksiDetail, HasilProduksiDetail

class RencanaBarangInLine(admin.TabularInline):
    model = RencanaProduksiDetail

class RencanaProduksiAdmin(admin.ModelAdmin):
    inlines = [
        RencanaBarangInLine,
    ]

class HasilBarangInLine(admin.TabularInline):
    model = HasilProduksiDetail

class HasilProduksiAdmin(admin.ModelAdmin):
    inlines = [
        HasilBarangInLine,
    ]

admin.site.register(Barang)
admin.site.register(RencanaProduksi, RencanaProduksiAdmin)
admin.site.register(HasilProduksi, HasilProduksiAdmin)