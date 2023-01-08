from django.db import models

# Create your models here.
class Links(models.Model):
	link_redirecionado = models.URLField()
	link_encurtado = models.CharField(max_length=25,unique=True)

	def __str__(self) -> str:
		return self.link_encurtado