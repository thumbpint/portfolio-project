from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    title = models.CharField(max_length=100)
    date = models.DateTimeField()

    def quicksum(self):
        return self.summary[:100]

    def pretty_date(self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.title