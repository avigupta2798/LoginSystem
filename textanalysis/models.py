from django.db import models

# Create your models here.

class WordCountUrl(models.Model):
    url = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return "%s" % self.url