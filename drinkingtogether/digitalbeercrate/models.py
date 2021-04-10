from django.db import models

class BeerCrate(models.Model):
    time = models.DateTimeField(auto_now=True)
    lastCount = models.IntegerField(default=0)

    def __str__(self):
        return "%s (%s)" %(self.lastCount, self.time.strftime("%d.%m.%Y - %H:%M:%S"))

class DonationGoal(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    account = models.TextField(verbose_name="Donation Account")
    website = models.CharField(max_length=255, verbose_name="Website")
    image = models.CharField(max_length=255, verbose_name="Image URL")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name
