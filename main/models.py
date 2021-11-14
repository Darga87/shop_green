from django.db import models

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование')
    email = models.EmailField(blank=True, verbose_name='e-mail')
    playlist = models.URLField('ссылка на плей лист')
    qty = models.PositiveIntegerField(default=1000)
    comment = models.TextField('коментарий')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', default=0.20)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена', default=0)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email) + str(self.id)
        
    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


