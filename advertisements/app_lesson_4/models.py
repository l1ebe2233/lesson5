from django.db import models
from django.db import migrations
from django.utils.html import format_html
from django.contrib import admin

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте , если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color:green; front-weight: bold;">Сегодня {}</span',created_time)
        return self.created_at.strftime('%d.%m.%Y в  %H:%M:%S')


    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f'<Advertisement:Advertisement({self.id}, {self.title}, {self.price})>'
