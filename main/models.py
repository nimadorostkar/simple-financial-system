from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=80)
    descriptions = models.CharField(default=" Project descriptions... ", max_length=250)

    def __str__(self):
        return self.project_name


class Finance(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    purchased_item = models.CharField(default=" items & descriptions... ", max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField()


    def __str__(self):
        return self.purchased_item
