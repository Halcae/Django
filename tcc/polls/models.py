from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1)
    pontos = models.IntegerField(default=0)
    experiencia = models.IntegerField(default=0)
    avatar = models.FileField(upload_to='usuarios')
    def __str__(self):
        return self.nome

class Curso(models.Model):
	nome = models.CharField(max_length=200)
	pontos_curso = models.IntegerField(default=0)
	experiencia_curso = models.IntegerField(default=0)
	dificuldade = models.CharField(max_length=80)
	def __str__(self):
		return self.nome

class Medalha(models.Model):
	nome = models.CharField(max_length=200)
	icone = models.FileField(upload_to='medalhas')
	def __str__(self):
		return self.nome

class Usuario_Curso(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	data_conclusao = models.DateTimeField('Data de Conclusao')
	def __str__(self):
		return self.usuario, self.curso

class Usuario_Medalha(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	medalha = models.ForeignKey(Medalha, on_delete=models.CASCADE)

class Curso_Medalha(models.Model):
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	medalha = models.ForeignKey(Medalha, on_delete=models.CASCADE)
	def __str__(self):
		return self.curso, self.medalha
