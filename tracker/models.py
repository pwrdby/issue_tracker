from datetime import datetime

from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Caregories for issues
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=70)


class Issue(models.Model):
    """
    Issue model.
    """
    def __str__(self):
        return self.name

    # states for issue
    CONCEPT = 'CN'
    OPEN = 'OP'
    IN_PROGRESS = 'IP'
    RESOLVED = 'RD'
    CLOSED = 'CL'
    STATE_CHOICES = (
        (CONCEPT, 'Concept'),
        (OPEN, 'Open'),
        (IN_PROGRESS, "In Progress"),
        (RESOLVED, 'Resolved'),
        (CLOSED, 'Closed')
    )
    name = models.CharField(max_length=30, default='')
    reporter = models.CharField(max_length=50)
    assignee = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=CONCEPT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_time = models.FloatField(default=0.0)
    worked_time = models.FloatField(default=0.0)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Update updated attribute
        """
        if self.updated:
            self.updated = datetime.now()
        super().save(*args, **kwargs)

    def get_state_name(self):
        """
        Return proper name of state.
        """
        return list(filter(lambda x: self.state in x, self.STATE_CHOICES))[0][1]