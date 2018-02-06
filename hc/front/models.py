from django.db import models

# The FAQs model
class Faq(models.Model):
    """
    This model operates the FAQ table and instance objects
    """
    question = models.CharField(max_length=150, blank=False)
    answer = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        """
        Object string representation
        """
        return self.question
# The Tutorial model
class Tutorial(models.Model):
    """
    This model operates the FAQ table and instance objects
    """
    title = models.CharField(max_length=150, blank=False)
    content = models.TextField(max_length=2000, blank=True)
    video_link = models.CharField(max_length=150, blank=True)

    def __str__(self):
        """
        Object string representation
        """
        return self.title
