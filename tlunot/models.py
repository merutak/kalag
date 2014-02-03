from django.db import models
from django.contrib.auth.models import User

class Tluna(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=256)
    guilty = models.BooleanField()

    def __unicode__(self):
        return '%s was charged with %s, guilty=%s'%(self.user, self.text, self.guilty, )
