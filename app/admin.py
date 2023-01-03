from django.contrib import admin

# Register your models here.


from .models import Buyurtma, Import, Export, Mijoz

class ImportAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi','format','import_vaqt','summa']
    list_filter = ('mahsulot_nomi','format','import_vaqt','summa')
    list_per_page = 10
    search_fields = ['mahsulot_nomi','format','import_vaqt','summa']

    class Meta:
        model = Import
admin.site.register(Import, ImportAdmin)




class ExportAdmin(admin.ModelAdmin):
    list_display = ['mahsulot_nomi','format','export_vaqt','summa']
    list_filter = ('mahsulot_nomi','format','export_vaqt','summa')
    list_per_page = 10
    search_fields = ['mahsulot_nomi','format','export_vaqt','summa']

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
    list_filter = ('format','buyurtma_sana','summa')
    list_display = ['mijoz','format','buyurtma_sana','summa']
    list_per_page = 10
    search_fields = ['mijoz','format','buyurtma_sana','summa']

    class Meta:
        model = Buyurtma
admin.site.register(Buyurtma, BuyurtmaAdmin)