from django.db import models
from django.utils.text import slugify

# auth in django
from django.contrib.auth.models import User
# Create your models here.

'''
django model fields
  - html widget
  -validations
  -db size
'''

#table as class
class Job(models.Model):  
    #choices
    JOB_TYPE = (
        ('FULL TIME','FULL TIME') ,
        ('PART TIME','PART TIME') ,
    )
    title = models.CharField(max_length=100)  #column
    # location 
    owner = models.ForeignKey(User , on_delete=models.CASCADE )
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    # we but Category in '' cuz the model Category comes after Job model 
    # if Category model before Job model write like < category = models.ForeignKey(Category , ) > without ''
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)

    image = models.ImageField(upload_to='jobs/')
    

    slug = models.SlugField(blank=True , null=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Job , self).save(*args , **kwargs)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    


class Apply(models.Model): 
    job = models.ForeignKey(Job , related_name='apply_job' , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name