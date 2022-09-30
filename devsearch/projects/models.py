from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
# Create your models here.

#model.name: Project
class Project(models.Model):
    # Set character field with maximum size/length of 200 to title - Text field for smaller purpose
    title = models.CharField(max_length=200)
    # Set null for allowing to create null in db and blank is allowing to submit the post request of form even it is blank
    # Textfield for larger purpose
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)

    #creating many to many relationships
    tags=models.ManyToManyField('Tag',blank=True)

    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio =models.IntegerField(default=0,null=True,blank=True)

    # Pass automatically current sys time (generate the timestamp)
    created = models.DateTimeField(auto_now_add=True)

    # Inbuild field to specific for id and it should unique, pk and non-editable
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    #owner
    VOTE_TYPE=(
        ('up','Up Vote'),
        ('down','Down Vote'),
    )

    #Establishing one to many relationships
    project=models.ForeignKey(Project,on_delete=models.CASCADE)

    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name=models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name
