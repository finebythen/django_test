from django.db import models


class PdfExportModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    id_number = models.IntegerField(default=0)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
