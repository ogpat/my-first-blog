from django.db import models
from django.utils import timezone


#defines the model -- models.Model tells django to save it in DB
class Post(models.Model):
    #each Post will have these attributes
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    #method of a post
    def publish(self):
        self.publish_date = timezone.now
        self.save()

    def __str__(self):
        return self.title


