from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class EmailAccount(models.Model):
	owner = models.ForeignKey(Employee, models.CASCADE)
	name = models.CharField(max_length=30, blank=True)
	email = models.EmailField()
	password = models.CharField(max_length=30)

	def fillName(self, email: str):
		return email.split("@")[0].capitalize()
     
	def save(self, *args, **kwargs):
		if not self.name:
			self.name = self.fillName(self.email)
		super(EmailAccount, self).save(*args, **kwargs)
	
	def __str__(self) -> str:
		return self.name