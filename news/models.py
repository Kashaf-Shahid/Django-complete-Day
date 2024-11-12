from django.db import models

# Create your models here.

class Reporter(models.Model):
    fullname=models.CharField(max_length=70)

    def __str__(self):
        return self.fullname
    
    
class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    Reporter= models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    

class Person(models.Model):
    people=models.Manager()

class BlogComment(models.Model):
    name=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)

    def __str__(self):
        return self.name+" "+self.comment