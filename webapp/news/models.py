from django.db import models
from django.contrib.auth.models import User


class Artiles(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Текст новости', default='')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)

    image = models.ImageField('Изображение', upload_to='main/image/', blank=True, null=True)

    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_articles', blank=True)
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()
    
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']
    
