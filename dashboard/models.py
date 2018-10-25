from django.db import models


class KhaneKiCheez(models.Model):

	name = models.CharField(verbose_name='Kya kha raha hai?', max_length=100, null=True, blank=True)
	price = models.IntegerField(verbose_name='Kitne ka hai?')

	def __str__(self):
		return '{s.name}: {s.price}'.format(s=self)