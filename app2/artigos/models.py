from django.db import models
from django.db.models import permalink


# Create your models here.
class Agencia(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()


class Artigo(models.Model):
    titulo = models.CharField('Título: ', max_length=80)
    url = models.SlugField(
        'URL',
        max_length=200,
        help_text='URL baseada no título.',
        unique=True
    )
    pub_date = models.DateTimeField('Data de Publicação: ')
    conteudo = models.TextField('Conteúdo da Página: ')
    autores = models.ManyToManyField(Autor)
    agencia = models.ForeignKey(Agencia)

    def __str__(self):
        return self.titulo
