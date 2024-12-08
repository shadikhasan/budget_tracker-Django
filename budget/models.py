from django.db import models

class Entry(models.Model):
    date = models.DateField()
    month = models.CharField(max_length=20, editable=False)  # Derived from date
    description = models.TextField()
    category = models.CharField(max_length=50)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    debits = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Auto-set month on save
        self.month = self.date.strftime("%B %Y")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.description}"
