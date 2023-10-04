from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class FrameworkModel(models.Model):
    name = models.CharField(max_length=25, verbose_name='name', **NULLABLE)
    language = models.CharField(max_length=25, verbose_name='language', **NULLABLE)

    def __str__(self):
        return f'Name - {self.name}, language - {self.language}'

    class Meta:
        verbose_name = 'Фремворк'
        verbose_name_plural = 'Фремворки'

