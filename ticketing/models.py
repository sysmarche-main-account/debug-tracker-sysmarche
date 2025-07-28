from django.db import models

# Create your models here.

class Ticket(models.Model):
    STATUS_LIST = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved')
    ]

    website_name = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    image_url = models.ImageField(upload_to='ticketing/', blank=True, null=True)
    email_address = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_LIST, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.website_name} {self.title}"

