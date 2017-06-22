from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	yazar = models.ForeignKey('auth.User')
	baslik = models.CharField(max_length=200)
	yazi = models.TextField()
	olusturma_tarihi = models.DateTimeField(default=timezone.now)
	yayin_tarihi = models.DateTimeField(blank=True, null=True)

	def yayinla(self):
		self.yayin_tarihi = timezone.now()
		self.save()

	def __str__(self):
		return self.baslik

	def __unicode__(self):
		return u'{y}/{b}/{t}/{o}/{d}'.format(
			y = self.yazar,
			b = self.baslik,
			t = self.yazi,
			o = self.olusturma_tarihi,
			d = self.yayin_tarihi
			)