from django.db import models
import datetime

class VoteSession(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default='', blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    number_of_participants = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_active_session():
        return VoteSession.objects.filter(is_closed=False).first()
    
    @staticmethod
    def get_vote_session_by_id(session_id):
        return VoteSession.objects.get(id=session_id)
    
    @staticmethod
    def get_open_vote_sessions():
        return VoteSession.objects.filter(is_closed=False)