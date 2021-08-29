from django.db import models

class Connection(models.Model):
    founder_id = models.ForeignKey('founders.Founder', null=False, on_delete=models.CASCADE)
    investor_id = models.ForeignKey('investors.Investor', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = f'Founder {self.founder_id} <> Investor {self.investor_id}'
        super(Connection, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
