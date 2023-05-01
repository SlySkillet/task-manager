from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        null=True,
        related_name="projects",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

# --GANTT CHART EXPERIMENT--



# class Chart(models.Model):
#     name = models.CharField(max_length=200)
#     start_date = models.DateField()
#     responsible = models.ForeignKey(User, on_delete=models.CASCADE)
#     week_number = models.CharField(max_length=2, blank=True)
#     finish_date = models.DateField()

#     def __str__(self):
#         return str(self.name)

#     def save(self, *args, **kwargs):
#         print(self.start_date.isocalendar()[1])
#         if self.week_number == "":
#             self.week_number = self.start_date.isocalendar()[1]
#         super().save(*args, **kwargs)
