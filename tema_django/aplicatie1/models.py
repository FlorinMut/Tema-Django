from django.db import models


class Companies(models.Model):
    company_choices = (('SRL', 'S.R.L.'),
                       ('SA', 'S.A.'))

    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=5, choices=company_choices)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.website} {self.company_type}"

