from django.contrib import admin
from .models import Professor, Curso, Post  # <- adicionar Post

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'materia')
    search_fields = ('nome', 'email', 'materia')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'carga_horaria', 'professor')
    search_fields = ('nome',)
    list_filter = ('professor',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_criacao')
    search_fields = ('titulo',)
    list_filter = ('data_criacao',)
