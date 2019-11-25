from django.db import models
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.
# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
   
#     def __str__(self):
#         return self.user_name 
#     class Meta:
#         ordering = ['user_name']
#     def save_user(self):
#         self.save()
     
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_photos',null=True,blank=True)
    bio = HTMLField()
    contact=models.CharField(max_length=12)
    linkedIn =  URLOrRelativeURLField()
    projects = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    def __str__(self):
        return self.user.username
    
class Project(models.Model):
    project_title = models.CharField(max_length=40)
    project_description = HTMLField()
    landing_page = models.ImageField(upload_to='landing_pages')
    live_site = URLOrRelativeURLField()
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.project_title