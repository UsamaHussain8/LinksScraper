from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return f'{self.name} ----> {self.address}'
