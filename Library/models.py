from django.db import models
from account.models import Customuser
from datetime import datetime
# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=25,default='')

    class Meta:
        db_table = 'book_genre'

    def __str__(self):
        return self.name
class Authors(models.Model):
    user = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    bio = models.TextField()
    date_of_birth=models.DateField()
    isnt_dead=models.BooleanField(default=datetime.now)
    date_of_death=models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='author/')
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    country = models.CharField(default='', max_length=25)

    def __str__(self):
        return self.user.first_name
    class Meta:
        db_table = 'Author'

class Books(models.Model):
    name = models.CharField(max_length=25,default='')
    image = models.ImageField(upload_to='book/')
    price = models.FloatField(default=0)
    pages = models.PositiveSmallIntegerField(default=5)
    year = models.PositiveSmallIntegerField(default=1900)
    author = models.ForeignKey(Authors,on_delete=models.SET_NULL,null=True)
    genre= models.ForeignKey(Genres,on_delete=models.SET_NULL,null=True)
    desc=models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table ='Book'