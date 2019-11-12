from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    time = models.IntegerField()
    def __str__(self):
        return self.name

class Hour(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    def __str__(self):
        return "inicio:"+str(self.start)+"/ fim:" + str(self.end)
        

class Room(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Session(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    def __str__(self):
        return "Filme:"+self.movie.name + " / "+self.room.name+" / hora: inicio:"+ str(self.hour.start) +" fim:"+str(self.hour.end)

class  Client(models.Model):
    name = models.CharField(max_length=50)
    idade = models.IntegerField()
    session = models.ManyToManyField(Session)
    def __str__(self):
        return self.name


    
    

