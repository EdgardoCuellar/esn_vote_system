# views.py
from django.shortcuts import render, redirect
from django.views import View
from esn_vote_system.models.vote import Vote, VoteOption
from esn_vote_system.models.vote_session import VoteSession

class CreateVoteView(View):
    def get(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        sessions = VoteSession.get_open_vote_sessions()
        return render(request, 'create_vote.html', {'sessions': sessions})

    def post(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        title = request.POST.get('title')
        description = request.POST.get('description')
        max_num_choices = request.POST.get('max_num_choices')
        session_id = request.POST.get('session_id')

        vote = Vote.objects.create(title=title, description=description, max_num_choices=max_num_choices, session_id=session_id)

        option_texts = request.POST.getlist('option_text')
        for option_text in option_texts:
            VoteOption.objects.create(vote=vote, option_text=option_text)

        return redirect('admin_view')  # Replace 'vote_list' with the actual name of your URL pattern
