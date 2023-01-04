from django.db import models
import math
format = [
    ('kg','Kilogram'),
    ('dona','Dona'),
]

class Import(models.Model):
    mahsulot_nomi = models.CharField(max_length=200)
    format = models.CharField(choices=format, max_length=10)
    miqdor = models.IntegerField()
    narx = models.IntegerField()
    import_vaqt = models.DateTimeField()
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def summa(self):
        self.summa = (self.miqdor * self.narx)
        
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} | {self.import_vaqt} | {self.summa}"
    
    class Meta:
        verbose_name = 'Import'
        verbose_name_plural = 'Import'
        
        
class Export(models.Model):
    mahsulot_nomi = models.CharField(max_length=200)
    format = models.CharField(choices=format, max_length=10)
    miqdor = models.IntegerField()
    narx = models.IntegerField()
    export_vaqt = models.DateTimeField()
    
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def summa(self):
        self.summa = (self.miqdor * self.narx)
    
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format} |{self.narx} | {self.import_vaqt} | {self.summa}"
    
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
    format = models.CharField(choices=format, max_length=10, null=True,blank=True)
    narx = models.IntegerField()
    miqdor = models.IntegerField()
    buyurtma_sana = models.DateTimeField()
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def summa(self):
        self.summa = (self.miqdor * self.narx)
        
    
    def __str__(self):
        return f"{self.mijoz} | {self.format} {self.miqdor} | {self.narx} | {self.buyurtma_sana} | {self.summa}"
    
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
        
        
class Ombor(models.Model):
    mahsulot_nomi = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    format = models.CharField(choices=format, max_length=10)
    narx = models.IntegerField()
    miqdor = models.IntegerField()
    izoh = models.TextField(null=True,blank=True)
    
    @property
    def summa(self):
        self.summa = (self.miqdor * self.narx)
        
    def __str__(self):
        return f"{self.mahsulot_nomi} | {self.format}"
    
    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborxona'
    
    
class Hodim(models.Model):
    ism_sharif = models.CharField(max_length=200)
    lavozim = models.CharField(max_length=100)
    stavka = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.ism_sharif} | {self.lavozim} | {self.stavka}"
    
    class Meta:
        verbose_name = 'Hodim'
        verbose_name_plural = 'Hodimlar'