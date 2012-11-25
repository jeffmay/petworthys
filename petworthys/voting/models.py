from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name


class Participant(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name


class Entry(models.Model):
	votes = models.IntegerField()
	category = models.ForeignKey(Category)
	participant = models.ForeignKey(Participant)

	def __unicode__(self):
		output = 'Entry For {0} in Category {1}'.format(self.participant, self.category)
		return output

