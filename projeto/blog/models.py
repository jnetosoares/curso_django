from django.db import models

# Create your models here.

from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titutlo = models.CharField(max_length=200)
    texto = models.TextField()
    criacao_data = models.DateTimeField(
            default=timezone.now)
    publicacao_data = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.publicacao_data = timezone.now()
        self.save()

    def __str__(self):
        return self.titutlo
