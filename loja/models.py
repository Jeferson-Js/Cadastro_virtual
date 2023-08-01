from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome