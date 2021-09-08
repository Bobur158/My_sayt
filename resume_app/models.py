from django.db import models
from django.db.models.aggregates import Max

class Html(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Jquery(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Bootstrap(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Css(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Python(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class C(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Mysql(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class JavaScript(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class English(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Uzbek(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Tadjik(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Russian(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Turkish(models.Model):
    name = models.CharField(max_length=100,null=1)
    percent = models.IntegerField(null=True)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=100,null=1)

    def __str__(self):
        return self.name