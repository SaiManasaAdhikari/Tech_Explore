from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User)
    full_name=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=12)

    class Meta:
        abstract = True

class Institution(Profile):
    institution_name=models.CharField(max_length=50)
    institution_website=models.URLField()



class Subscriber(Profile):
    stream=models.CharField(max_length=40)
    course=models.CharField(max_length=40)
    
    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}".format(self.full_name,self.email_id,self.phone_no,self.stream,self.course)
#Profile=models.ForeignKey('Profile')

#def __str__(self):
#    return self.Institution_name
 
class Cities(models.Model):
    city_name = models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.city_name

class States(models.Model):
    state = models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return self.state

class Categories(models.Model):
    category = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.category

class Streams(models.Model):
    stream = models.CharField(max_length=40,primary_key=True)

    def __str__(self):
        return self.stream
            
class Courses(models.Model):
    course = models.CharField(max_length=40,primary_key=True)
   
    def __str__(self):
        return self.course   
        
class Event_Details(models.Model):#Event details by the institution
      event_name = models.CharField(max_length = 100) 
      first_date = models.DateField()
      last_date = models.DateField()
      regd_last_date = models.DateField()
#      duration = models.DurationField()
      description = models.TextField(blank = True,null = True)
      category = models.ForeignKey(Categories)
      city = models.ForeignKey(Cities)
      state = models.ForeignKey(States)
      stream = models.ForeignKey(Streams)
      course = models.ForeignKey(Courses)
  
      def __str__(self):
          return "{0}-{1}-{2}-{3}-{4}".format(self.event_name,self.city,self.state,self.stream,self.course)
          
          
          
        #  return "{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}_{8}-{9}".format(self.event_name,self.first_date,self.last_date,self.regd_last_date,self.city,self.state,self.stream,self.course,self.description,self.category)
#Profile=models.ForeignKey('Profile')

  
class Regd_Students(models.Model):#Registered students details
      
      student = models.OneToOneField(Subscriber,related_name='full_name')
      student = models.OneToOneField(Subscriber,related_name='email_id')
      student = models.OneToOneField(Subscriber,related_name='phone_no')
      student = models.OneToOneField(Subscriber,related_name='stream')
      student = models.OneToOneField(Subscriber,related_name='year')
      #email_id=models.ForeignKey(Subscriber)
      #phone_no=models.ForeignKey(Subscriber) 
      #stream = models.ForeignKey(Subscriber) 
      #course = models.ForeignKey(Subscriber) 
      event_id = models.OneToOneField(Event_Details)       
      regd_date=models.DateTimeField(default=datetime.now,blank=True)
      
      def __str__(self):
          return self.student
class Comment(models.Model):
    author=models.OneToOneField(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    #approved_comment=models.BooleanField(default=False)
     
    def __str__(self):
        return self.text
