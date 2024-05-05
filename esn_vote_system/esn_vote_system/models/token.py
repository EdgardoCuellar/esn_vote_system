from django.db import models
from esn_vote_system.models.vote_session import VoteSession
import secrets
import string

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    vote_session = models.ForeignKey(VoteSession, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    @staticmethod
    def check_key(check_key):
        key_file_path = 'private/register_token.txt'
        key = ""
        with open(key_file_path, 'r') as f:
            key = f.read()

        return key.strip() == check_key.strip()
    
    @staticmethod
    def generate_token(length=16):
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    @staticmethod
    def create_register_token(session_id):
        session = VoteSession.objects.get(id=session_id)
        return Token.objects.create(
            token=Token.generate_token(24),
            vote_session=session
        )

    @staticmethod
    def get_register_token_by_token(token):
        return Token.objects.get(token=token)

    @staticmethod
    def is_token_valid(token):
        try:
            tmp_token = Token.objects.get(token=token)
            if tmp_token.vote_session.is_closed:
                return False
            return True
        except:
            return False
            
    @staticmethod
    def is_token_valid_and_not_used(token):
        try:
            token = Token.objects.get(token=token)
            if token.user is not None:
                return False
            return True
        except:
            return False

    @staticmethod
    def get_token_by_token(token):
        return Token.objects.get(token=token)

    
