from django.db import models

# Create your models here.


class GeneralInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField()
    about_me = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)



class Experience(models.Model):
    position = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    started_at = models.DateField()
    ended_at = models.DateField()
    description = models.TextField()



class Education(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    graduation_date = models.DateField()
    description = models.TextField()



class Resume(models.Model):
    general = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE)
    experience = models.ManyToManyField(Experience, blank=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)