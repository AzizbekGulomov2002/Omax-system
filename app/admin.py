from django.contrib import admin

# Register your models here.


from .models import Buyurtma, Import, Export, Mijoz, Ombor, Hodim

class ImportAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi','format','import_vaqt','miqdor','narx','summa']
    list_filter = ('mahsulot_nomi','format','import_vaqt','miqdor','narx')
    list_per_page = 10
    search_fields = ['mahsulot_nomi','format','import_vaqt','miqdor','narx']

    class Meta:
        model = Import
admin.site.register(Import, ImportAdmin)




class ExportAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi','format','export_vaqt','miqdor','narx','summa']
    list_filter = ('mahsulot_nomi','format','export_vaqt','miqdor','narx')
    list_per_page = 10
    search_fields = ['mahsulot_nomi','format','export_vaqt','miqdor','narx']

    class Meta:
        model = Export
admin.site.register(Export, ExportAdmin)



class MijozAdmin(admin.ModelAdmin):
    list_filter = ('ism_sharif','telefon',)
    list_display = ['nomi','ism_sharif','telefon','manzil']
    list_per_page = 10
    search_fields = ['nomi','ism_sharif','telefon','manzil']

    class Meta:
        model = Mijoz
admin.site.register(Mijoz, MijozAdmin)


class BuyurtmaAdmin(admin.ModelAdmin):
    list_filter = ('format','buyurtma_sana','miqdor','narx')
    list_display = ['mijoz','format','buyurtma_sana','miqdor','narx','summa']
    list_per_page = 10
    search_fields = ['mijoz','format','buyurtma_sana','summa']

    class Meta:
        model = Buyurtma
admin.site.register(Buyurtma, BuyurtmaAdmin)



class OmborAdmin(admin.ModelAdmin):
    list_filter = ('mahsulot_nomi','format','miqdor','narx')
    list_display = ['mahsulot_nomi','format','miqdor','narx']
    list_per_page = 10
    search_fields = ['mahsulot_nomi','format']

    class Meta:
        model = Ombor
admin.site.register(Ombor, OmborAdmin)


class HodimAdmin(admin.ModelAdmin):
    list_filter = ('ism_sharif','lavozim','stavka')
    list_display = ['ism_sharif','lavozim','stavka']
    list_per_page = 10
    search_fields = ['ism_sharif','lavozim','stavka']

    class Meta:
        model = Hodim
admin.site.register(Hodim, HodimAdmin)