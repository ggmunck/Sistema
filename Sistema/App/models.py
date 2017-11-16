from django.db import models

# Create your models here.
class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
   
class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    #Função de retorno padrão do objeto
    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, null=True)
    #Função de retorno padrão do objeto
    def __str__(self):
        return self.nome
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, null=True)
    #Função de retorno padrão do objeto
    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    secretaria = models.ForeignKey(Secretaria, null=True)
    #Função de retorno padrão do objeto
    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length = 50)
    codigo = models.CharField(max_length = 30)
    obt_let = models.CharField(max_length = 1)
    status = models.CharField(max_length = 1)
    credito = models.ForeignKey(Credito)
    d_requisito = models.ManyToManyField('Disciplina', null=True, blank=True)
    professor = models.ForeignKey(Professor, null=True)
    #Função de retorno padrão do objeto
    def __str__(self):
        return codigo + " - " + self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    credito = models.ForeignKey(Credito)
    curso = models.ForeignKey(Curso, null = True)
    disciplinas = models.ManyToManyField('Disciplina', null=True, blank=True)
    #Função de retorno padrão do objeto
    def __str__(self):
        return self.nome