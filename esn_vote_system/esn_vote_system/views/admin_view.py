from django.shortcuts import render, redirect
from django.views import View
from esn_vote_system.models.token import Token
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.vote import Vote, VoteOption

class AdminView(View):

    def get(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        
        session = VoteSession.get_active_session()
        votes = Vote.objects.all()

        return render(request, 'admin_view.html', {'session': session, 'votes': votes})
