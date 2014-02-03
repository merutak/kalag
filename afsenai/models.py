from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	mispar_ishi = models.IntegerField()
	history = models.ManyToManyField('Item', blank=True, null=True, through='TakenItem')

	def __unicode__(self):
		return unicode(self.user)

class Item(models.Model):
	name = models.CharField(max_length=64)
	makat = models.IntegerField(null=True, blank=True)

	class Meta:
		ordering = ['name']

        def __unicode__(self):
		return unicode(self.name)

class TakenItem(models.Model):
	item = models.ForeignKey(Item)
        signer = models.ForeignKey(UserProfile)
	time = models.DateTimeField(auto_now_add=True, editable=True)
        tzadik = models.IntegerField(null=True, blank=True)
	count = models.IntegerField(default=1)

	def __unicode__(self):
		return u'%s took %s %s at %s'%(self.signer, self.count, self.item, self.time,)

class Hatima(): # models.Model
	signer = models.ForeignKey(UserProfile, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	#updated = models.DateTimeField(auto_now_update=True)
	history = models.ManyToManyField(Item, blank=True, null=True, through=TakenItem)
	#history = models.ManyToManyField(TakenItem, blank=True, null=True)

	def __unicode__(self):
		return u'%s took stuff'%(self.signer, )
