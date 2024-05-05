from django.shortcuts import render, redirect, get_object_or_404
from esn_vote_system.models.vote import VoteOption, Vote
from django.views import View
from esn_vote_system.models.vote_session import VoteSession

class VoteUpdateView(View):
    def get(self, request, vote_id):
        vote = get_object_or_404(Vote, pk=vote_id)
        sessions = VoteSession.get_open_vote_sessions()
        return render(request, 'update_vote.html', {'vote': vote, 'sessions': sessions, 'options': vote.options.all()})

    def post(self, request, vote_id):
        vote = get_object_or_404(Vote, pk=vote_id)
        vote.title = request.POST.get('title')
        vote.description = request.POST.get('description')
        vote.max_num_choices = request.POST.get('max_num_choices')
        vote.save()

        option_texts = request.POST.getlist('option_text')
        for option in vote.options.all():
            option.option_text = option_texts.pop(0)
            option.save()

        return redirect('admin_view')  # Replace 'vote_list' with the actual name of your URL pattern

def publish_vote(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    vote.vote_opened = True
    vote.save()
    return redirect('admin_view')  # Replace 'vote_list' with the actual name of your URL pattern