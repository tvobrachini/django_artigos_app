from django.contrib import admin
from .models import Agencia
from .models import Autor
from .models import Artigo


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')


class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
    search_fields = ('nome', 'site')


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'agencia',  'url', 'pub_date')
    search_fields = ('titulo', 'agencia')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('titulo', 'url', 'pub_date', 'autores', 'agencia', 'conteudo')
    prepopulated_fields = {'url': ('titulo',)}


admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
