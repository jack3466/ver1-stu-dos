from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100, default="General")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

from django.db import models

class AssistanceRequest(models.Model):
    SERVICE_CHOICES = [
        ('resume', 'Resume Writing'),
        ('career', 'Career Support'),
        ('academic', 'Academic Help'),
        ('skill', 'Skill Support'),
        ('digital', 'Digital Support'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='other')
    
    # --- ADD THIS LINE ---
    message = models.TextField(blank=True, null=True) 
    
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

