import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Book(BaseModel):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = models.TextField(default="")
    
    class Meta:
        verbose_name_plural = "Book"
        app_label = "core"
    
    def __str__(self):
        return "{}".format(self.author)


