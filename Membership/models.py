from django.db import models

# Create your models here.

class Application(models.Model):
    
    male = 'male'
    female = 'female'
    
    Gender = [
        ( male,'male'),  
         ( female,'female'),
            
    ]
   
    Biginner = 'Biginner'
    moderate = 'moderate'
    professional = 'professional'
    
    stage = [
        ( Biginner,'Biginner'), 
        (moderate,'moderate') ,
        ( professional,' professional'),
        
            
    ]
    Height = models.FloatField()
    Weight = models.FloatField()
    Age = models.FloatField()
    sex = models.CharField(max_length = 250, choices=Gender,
        default=male,)
    Level = models.CharField(max_length = 250, choices=stage,
        default=Biginner,)
    
    