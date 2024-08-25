# from django.db import models
# # Create your models here.
# class Game(models.Model):
#     STATUS_CHOICES = [
#         ('waiting', 'Waiting'),
#         ('ongoing', 'Ongoing'),
#         ('completed', 'Completed'),
#     ]
#     name = models.CharField(max_length=100)
#     gameId = models.IntegerField();
#     playerId = models.IntegerField();
#     adminId = models.IntegerField();
#     mcqs=models.JSONField(default=dict);
#     status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
#
#     def __str__(self):
#         return self.name
from django.db import models
from mcqs.models import MCQ

STATUS_CHOICES = [
    ('waiting', 'Waiting'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
]

class Game(models.Model):
    name = models.CharField(max_length=100)
    gameId = models.IntegerField()
    playerId = models.IntegerField()
    adminId = models.IntegerField()
    mcqs = models.ManyToManyField(MCQ)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
