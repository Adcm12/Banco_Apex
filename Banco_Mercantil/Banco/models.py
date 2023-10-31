from django.db import models

class Conta_Corriente(models.Model):

    conta = models.CharField(max_length=9)
    tipo_conta = models.CharField(max_length=15, default = "Conta corriente")
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()


    def __str__(self):
        return f'{self.nome}'
    
class Conta_poupança(models.Model):

    conta = models.CharField(max_length=9)
    tipo_conta = models.CharField(max_length=14, default = "Conta poupança")
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()


    def __str__(self):
        return f'{self.nome}'