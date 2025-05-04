from django.db import models

    class Meta:
        verbose_name = 'Катана'
        verbose_name_plural = 'Катаны'
class Katana(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='katanas/', verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание')
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, 
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг в звёздах'
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Катана'
        verbose_name_plural = 'Катаны'

class Order(models.Model):
    katana = models.ForeignKey(Katana, on_delete=models.CASCADE, related_name='orders', verbose_name='Катана')
    customer_name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    email = models.EmailField(verbose_name='Email покупателя')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f'Заказ от {self.customer_name} на {self.katana.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_ordered']