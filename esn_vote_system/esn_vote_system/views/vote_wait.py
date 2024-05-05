from django.shortcuts import render, redirect
from django.views import View
from esn_vote_system.models.token import Token
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.vote import Vote, VoteOption

class VoteWaitView(View):

    def get(self, request, session_id):
        session = VoteSession.get_vote_session_by_id(session_id)
        votes = Vote.get_vote_opened_by_open_vote_session(session_id)
        token = request.session.get('token')
        return render(request, 'vote_wait.html', {'session': session, 'votes': votes, 'token': token})
