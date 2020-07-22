from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    error = {}
    def login_validate(self, postData):
        user = User.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here?
        if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
            pass
        else:
            error["password"] = "Invalid Credentials"

    def register_validate(self, postData):
        error = {}
        #VALIDATE FIRST AND LAST NAME
        if len(postData['first_name']) < 3:
            error['first_name'] = 'Your first name must be longer than 3 characters'
        if len(postData['last_name']) < 1:
            error['last_name'] = 'Your last name must be longer than 3 characters'
        
        #VALIDATE WITH EMAIL REGEX AND CHECK FOR DUPES
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = 'Your email must be in valid format'
        if User.objects.filter(email=postData['email']):
            error['emaildupe'] = 'Your email is already registered'
        
        #VALIDATE PASSWORD AND CONFIRM THAT PASSWORD AND C_PASSWORD MATCHES
        if len(postData['password']) < 8:
            error['password'] = 'Your password must be longer than 8 characters'
        if postData['password'] != postData['confirmPassword']:
            error['passwordmatch'] = 'Your password and confirm passowrd does not match'
        return error

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)