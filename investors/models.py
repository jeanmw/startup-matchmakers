from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    group_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
