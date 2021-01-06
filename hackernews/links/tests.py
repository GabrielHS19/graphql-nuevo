from django.test import TestCase

# Create your tests here.
class Link(models.Model):
    url=models.URLField()
    description = models.TextField(blank=true)
