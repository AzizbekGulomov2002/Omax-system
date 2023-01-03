from django.db import models

format = [
    ('kg','Kilogram'),
    ('dona','Dona'),
]

class Import(models.Model):
    mahsulot_nomi = models.CharField(max_length=200)
    format = models.CharField(choices=format, max_length=10)
    miqdor = models.IntegerField()
    import_vaqt = models.DateTimeField()
    summa = models.CharField(max_length=200)
    izoh = models.TextField()
    
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} | {self.import_vaqt} | {self.summa}"
    
    class Meta:
        verbose_name = 'Import'
        verbose_name_plural = 'Import'
        
        
class Export(models.Model):
    mahsulot_nomi = models.CharField(max_length=200)
    format = models.CharField(choices=format, max_length=10)
    miqdor = models.IntegerField()
    export_vaqt = models.DateTimeField()
    summa = models.CharField(max_length=200)
    izoh = models.TextField()
    
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} | {self.import_vaqt} | {self.summa}"
    
    class Meta:
        verbose_name = 'Export'
        verbose_name_plural = 'Export'
    
class Mijoz(models.Model):
    nomi = models.CharField(max_length=200)
    ism_sharif = models.CharField(max_length=200)
    telefon = models.IntegerField()
    manzil = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nomi} | {self.ism_sharif} | {self.telefon} | {self.manzil}"
    
    
    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'
    
class Buyurtma(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    format = models.CharField(choices=format, max_length=10)
    buyurtma_sana = models.DateTimeField()
    summa = models.CharField(max_length=200)
    izoh = models.TextField()
    
    def __str__(self):
        return f"{self.mijoz} | {self.format} | {self.buyurtma_sana} | {self.summa}"
    
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
    
    