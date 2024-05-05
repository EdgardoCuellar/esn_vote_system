from django.shortcuts import render, redirect
from django.views import View
from esn_vote_system.models.token import Token
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.vote import Vote, VoteOption, VoteTokenUsed

class VoteResultsView(View):

    def get(self, request, vote_id):
        vote = Vote.objects.get(id=vote_id)
        options = VoteOption.objects.filter(vote_id=vote_id)
        return render(request, 'vote_results.html', {'vote': vote, 'options': options})
