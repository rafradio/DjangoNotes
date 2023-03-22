from django.db import models

class Note(models.Model):
    title = models.CharField('Название', max_length=45, default='Название')
    body = models.TextField('Текст заметки')
    date = models.DateTimeField('Дата')
