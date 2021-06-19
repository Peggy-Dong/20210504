from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class 食材(models.Model):
	name = models.CharField(max_length=10)
	g = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.name

class 食譜(models.Model):
	name = models.CharField(max_length=10)
	食材 = models.ForeignKey(食材, on_delete=models.CASCADE)
	g = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.name




# Create your models here.
