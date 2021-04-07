from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # models.Model indicates that the Post object is an Django object, so Django knows that it
                          # should be saved in the database.
    # In the section below we defined the properties (attributes of the object Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # models.ForeignKey is a link to another
                                                                                   # model.
    title = models.CharField(max_length=200)# models.CharField defines text with a limited number of characters
    text = models.TextField() # This is for long text without a limit.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title