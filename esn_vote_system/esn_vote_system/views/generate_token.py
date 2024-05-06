from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from esn_vote_system.models.token import Token
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.vote import Vote, VoteOption

from django.conf import settings


class GenerateToken(View):
    html_link = 'generate_token.html'

    def get(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        sessions = VoteSession.get_open_vote_sessions()
        return render (request, self.html_link, {'sessions': sessions})

    def post(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        session_id = request.POST.get ('session_id')
        
        error_message = None
        
        if session_id:
            token = Token.create_register_token(session_id)
            return render (request, self.html_link, {'token': token, 'sessions': VoteSession.get_open_vote_sessions()})

        error_message = 'Clé invalide !'

        return render (request, self.html_link, {'error': error_message, 'sessions': VoteSession.get_open_vote_sessions()})
    
