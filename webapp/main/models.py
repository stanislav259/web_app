from django.db import models


class ContactMessage(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Тема', max_length=200)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} - {self.subject}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'