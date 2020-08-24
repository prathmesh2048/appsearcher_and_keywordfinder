from django.db import models


class Url(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'URLS'


class Keywords(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name_plural = 'Keywords'

# Use "Keywords.objects.all().order_by('-id')[0].keyword" to get the value of the field keyword in the first row
# Use "Keywords.objects.all().order_by('-id')" to get the ascending order of the objects
