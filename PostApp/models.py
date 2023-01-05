from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import random  
import string 

class Post(models.Model):
    class Meta:
        verbose_name_plural = "Posts"

    
    title = models.CharField(max_length=20)
    desk = models.TextField()
    slug = models.SlugField("URL",max_length=40,primary_key=True)
    user = models.ForeignKey(get_user_model(), verbose_name="USER", on_delete=models.CASCADE)
    cat = models.ForeignKey("Category", verbose_name="CATEGORY", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def random_string_generator(self, size = 10, chars = string.ascii_lowercase + string.digits): 
        return ''.join(random.choice(chars) for _ in range(size)) 


    def unique_slug_generator(self, instance, new_slug = None): 
        if new_slug is not None: 
            slug = new_slug 
        else: 
            slug = slugify(instance.title) 
        Klass = instance.__class__ 
        qs_exists = Klass.objects.filter(slug = slug).exists() 
        if qs_exists: 
            new_slug = "{slug}-{randstr}".format( 
                slug = slug, randstr = self.random_string_generator(size = 4)) 
                
            return self.unique_slug_generator(instance, new_slug = new_slug) 
        return slug
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = self.unique_slug_generator(self)
        return super().save(*args, **kwargs)


    
    
    
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=20)
  
        
    def __str__(self):
        return self.name
    
    

