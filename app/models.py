from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.
class Questions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ques = models.CharField(max_length=150)
    option1 = models.CharField(max_length=150)
    option2 = models.CharField(max_length=150)
    option3 = models.CharField(max_length=150)
    option4 = models.CharField(max_length=150)
    vote1 = models.IntegerField(default=0)
    vote2 = models.IntegerField(default=0)
    vote3 = models.IntegerField(default=0)
    vote4 = models.IntegerField(default=0)
    vote = models.IntegerField(default=False, verbose_name="How many object created for this questions?")
    is_closed = models.BooleanField(default=False)

    @property
    def total_votes(self):
        return self.vote1 + self.vote2 + self.vote3 + self.vote4
    
    @property
    def get_winner_option(self):
        options = [self.vote1, self.vote2, self.vote3, self.vote4]
        max_votes = max(options)
        winner_index = options.index(max_votes)
        if options.count(max_votes) > 1:
            return "It's a tie"
        else:
            if winner_index == 0:
                return self.option1
            elif winner_index == 1:
                return self.option2
            elif winner_index == 2:
                return self.option3
            elif winner_index == 3:
                return self.option4
        return

    def __str__(self) -> str:
        return self.ques
    
class Voted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_question = models.ForeignKey(Questions, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0)])



