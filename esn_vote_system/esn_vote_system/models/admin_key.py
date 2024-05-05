from django.db import models

class AdminKey(models.Model):
    secret_key = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.secret_key

    @staticmethod
    def get_key():
        return AdminKey.objects.first().secret_key