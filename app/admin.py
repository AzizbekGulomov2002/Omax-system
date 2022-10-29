from django.contrib import admin

# Register your models here.


from .models import Zakas
class ZakasAdmin(admin.ModelAdmin):
    list_display = ['firma_nomi','ism_sharif','zakas_dona','kontrakt_vaqt','summa']
    list_per_page = 10
    search_fields = ['firma_nomi','ism_sharif','zakas_dona','kontrakt_vaqt','summa']

    class Meta:
        model = Zakas
admin.site.register(Zakas, ZakasAdmin)