# from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from datetime import datetime, date


class Variable(models.Model):
    class Meta:
        verbose_name = "Zmienna"
        verbose_name_plural = "Zmienne"

    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagi"
        ordering = ['name']

    name = models.CharField(max_length=20, primary_key=True)

class Author(models.Model):
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default="")
    date = models.DateField(auto_now_add=True, blank=True)
    profile_image = models.ImageField(upload_to='static/upload/profile_images/')

    ROLES = (('normal', 'Normal'), ('admin', 'Admin'))
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='normal'
    )

    def __str__(self) -> str:
        return f"{self.nickname}, {self.date}"


class Article(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"
        ordering = ['-date']
    
    title = models.CharField(max_length=50, default="Tytuł nowego posta")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField(blank=True, null=True, default="")
    image = models.ImageField(upload_to='static/upload/article_images/', default="static/upload/article_images/default.jpg")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"Autor: {self.author.nickname}, {self.date}, tekst: {self.text[:20]}..."

    @property
    def date_dmy(self):
        return self.date.strftime("%d.%m.%Y")
    
    @property
    def thumbnail_title(self):
        title = self.title if len(self.title) < 30 else self.title[:30] + "..."
        return title

    @property
    def thumbnail_text(self):
        words = self.text.split(' ')
        for i in range(len(words)):
            if len(' '.join(words[:i])) > 100 - 2 * len(self.title):
                return ' '.join(words[:i-1])[:50]+'...'
        return self.thumbnail_text2
    
    @property
    def thumbnail_text2(self):
        text = self.text if len(self.text) < 20 else self.text[:20] + "..."
        return text

    @property
    def parsed_text(self):
        return '\n'.join([f"<p>{t}</p>" for t in self.text.split('\n')])
    
class Comment(models.Model):
    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True, default="")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def date_dmy(self):
        return self.date.strftime("%d.%m.%Y")