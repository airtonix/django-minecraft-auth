from django.db import models
from django.contrib.auth.models import User

class AuthToken(models.Model):
	user = models.OneToOneField('auth.User', unique=True)
	download_ticket = models.CharField(verbose_name=_("Ticket"), max_length=32)
	session_id = models.CharField(verbose_name=_("Session ID"), max_length=32)
	latest_version= models.CharField(verbose_name=_("Latest Version"), max_length=32)
