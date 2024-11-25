from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    little_description = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    time_posted = models.DateTimeField(auto_now_add=timezone.now(), null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default='post_img.webp', upload_to='post_pics')
    post_category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-time_posted']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    about_author = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        '''img = Image.open(self.image.path)
        if img.height > 160 or img.width > 150:
            output_size = (160, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)'''

