from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    materia = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nome

# Novo modelo Post
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
