from django.db import models


class Zakas(models.Model):
    ism_sharif = models.CharField(max_length=200)
    firma_nomi = models.CharField(max_length=200)
    zakas_dona = models.IntegerField()
    kontrakt_vaqt = models.DateTimeField(auto_now_add=True)
    summa = models.CharField(max_length=200)
    izoh = models.TextField()

    def __str__(self):
        return self.firma_nomi

    class Meta:
        verbose_name = "Zakas"
        verbose_name_plural = "Zakaslar"
