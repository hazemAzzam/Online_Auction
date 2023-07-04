from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    under = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.under:
            return f"{self.under} -> {self.name}"
        return f"{self.name}"
    
    def __repr__(self):
        return f"Category({self.__str__()})"