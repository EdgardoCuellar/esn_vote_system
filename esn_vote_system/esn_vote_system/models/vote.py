from django.db import models
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.token import Token

from django.db import models

class Vote(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    session = models.ForeignKey(VoteSession, on_delete=models.CASCADE)
    max_num_choices = models.IntegerField(default=1)
    vote_opened = models.BooleanField(default=False)
    datetime_vote_opened = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_options(self):
        return self.options.all()
    
     @staticmethod
    def get_vote_by_open_vote_session():
        return Vote.objects.filter(session__is_closed=False)
    
     @staticmethod
    def get_vote_opened_by_open_vote_session():
        return Vote.objects.filter(session__is_closed=False, vote_opened=True)
    
     @staticmethod
    def get_vote_opened_by_open_vote_session_sorted():
        return Vote.objects.filter(session__is_closed=False, vote_opened=True).order_by('datetime_vote_opened')
    
    @staticmethod
    def get_number_of_votes(vote_id):
        return VoteOption.objects.filter(vote_id=vote_id).aggregate(models.Sum('number_votes'))['number_votes__sum']

class VoteOption(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)
    number_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text
    
class VoteTokenUsed(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    
    @staticmethod
    def does_token_vote_exist(token_str, vote):
        token = Token.objects.get(token=token_str)
        return VoteTokenUsed.objects.filter(token=token, vote=vote).exists()
