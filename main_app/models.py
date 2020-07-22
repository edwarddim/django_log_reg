from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def login_validate(self, postData):
        user = User.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here?
        if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
            print("password match")
        else:
            print("failed password")

    def register_validate(self, postData):
        
        pass

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)