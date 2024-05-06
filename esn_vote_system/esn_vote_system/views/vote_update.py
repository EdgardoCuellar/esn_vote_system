from django.shortcuts import render, redirect, get_object_or_404
from esn_vote_system.models.vote import VoteOption, Vote
from django.views import View
from esn_vote_system.models.vote_session import VoteSession

class VoteUpdateView(View):
    def get(self, request, vote_id):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        vote = get_object_or_404(Vote, pk=vote_id)
        sessions = VoteSession.get_open_vote_sessions()
        return render(request, 'update_vote.html', {'vote': vote, 'sessions': sessions, 'options': vote.options.all()})

    def post(self, request, vote_id):
        if not request.session.get('admin_token'):
            return redirect('login_admin')
        vote = get_object_or_404(Vote, pk=vote_id)
        vote.delete()

        title = request.POST.get('title')
        description = request.POST.get('description')
        max_num_choices = request.POST.get('max_num_choices')
        session_id = request.POST.get('session_id')

        vote = Vote.objects.create(title=title, description=description, max_num_choices=max_num_choices, session_id=session_id)

        option_texts = request.POST.getlist('option_text')
        for option_text in option_texts:
            VoteOption.objects.create(vote=vote, option_text=option_text)

def publish_vote(request, vote_id):
    if not request.session.get('admin_token'):
        return redirect('login_admin')
    vote = get_object_or_404(Vote, pk=vote_id)
    vote.vote_opened = True
    vote.save()
    return redirect('admin_view') 

def delete_vote(request, vote_id):
    if not request.session.get('admin_token'):
        return redirect('login_admin')
    vote = get_object_or_404(Vote, pk=vote_id)
    if vote.vote_opened:
        return redirect('admin_view')
    vote.delete()
    return redirect('admin_view')