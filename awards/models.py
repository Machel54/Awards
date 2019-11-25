from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
   
    def __str__(self):
        return self.user_name 

    def save_user(self):
        self.save()
     
class UserProfile(models.Model):
    user = models.ForeignKey(User)
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
