from django.db import models

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField(auto_now_add = True)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

# Create your models here.


      
# # Importacion de los modelos
# from polls.models import Question, Choice

# # Llamado de todos los registros de un modelo
# Question.objects.all()

# # Creacion de un nuevo registro
# q = Question(question_text="¿Cual es el mejor curso de Platzi?", pub_date=timezone.now())

# # Guardado del nuevo registro
# q.save()