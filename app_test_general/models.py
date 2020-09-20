from django.db import models
from django.contrib.auth.models import User


genders = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Diverse', 'Diverse'),
)


class Customer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    user_created = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    user_created = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cluster(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    user_created = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    short_text = models.CharField(max_length=50, null=False, blank=False)
    long_text = models.TextField(max_length=500, null=False, blank=True, default="...")
    customer = models.CharField(max_length=255, null=False, blank=False)
    project = models.CharField(max_length=255, null=False, blank=False)
    cluster = models.CharField(max_length=255, null=False, blank=False)
    template = models.BooleanField(default=False)
    user_created = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.short_text


class Colorname(models.Model):
    colorname = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return 'Farbe: {}'.format(self.colorname)


class Departments(models.Model):
    department_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.department_name


class WidgetTweaksExamples(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    area = models.TextField(max_length=500, null=True, blank=True)
    date_str = models.TextField(max_length=10, null=False, blank=False, default='dd.mm.YYYY')

    def __str__(self):
        return self.name


class TextareaInput(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    user_created = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return 'Texteintrag, generiert am {} von {}'.format(self.date_created, self.user_created)


class CsvGroupModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    object_a = models.CharField(max_length=50, null=True, blank=True)
    amount_a = models.IntegerField(null=True)
    object_b = models.CharField(max_length=50, null=True, blank=True)
    amount_b = models.IntegerField(null=True)
    object_c = models.CharField(max_length=50, null=True, blank=True)
    amount_c = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class table_filter_model(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=50, null=False, blank=False, choices=genders)
    company = models.CharField(max_length=50, null=False, blank=False)
    department = models.CharField(max_length=50, null=False, blank=False)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TransportExamples(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, null=False, blank=False, choices=genders)

    def __str__(self):
        return self.name


class TimeFilteringExamples(models.Model):
    short_text = models.CharField(max_length=255, null=False, blank=False)
    date_start = models.DateField(null=False, blank=False)
    date_end = models.DateField(null=False, blank=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.short_text


PRODUCT_CHOICES = (
    ('TV', 'tv'),
    ('IPAD', 'ipad'),
    ('PLAYSTATION', 'playstation'),
)


class CsvLoad(models.Model):
    product = models.CharField(max_length=11, choices=PRODUCT_CHOICES)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.FloatField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.quantity}"

    def save(self, *args, **kwargs):
        price = None
        if self.product == 'TV':
            price = 559.99
        elif self.product == 'IPAD':
            price = 400.00
        elif self.product == 'PLAYSTATION':
            price = 464.99
        else:
            pass
        self.total = price * self.quantity
        super().save(*args, **kwargs)


class CustomerPDF(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
