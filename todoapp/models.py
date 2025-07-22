from django.db import models



class Todo(models.Model):  # Class name should be capitalized
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:  # Meta class name should be capitalized
        ordering = ('-created_at',)

    def __str__(self):
        return self.text  # Return the text field, not self

  
