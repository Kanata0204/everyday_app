from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text='必須項目', blank=False)
    position = models.IntegerField(help_text='本の位置', default=0, blank=True)

    class Meta:
        ordering = ['position', 'pk']

    def __str__(self):
        return self.title