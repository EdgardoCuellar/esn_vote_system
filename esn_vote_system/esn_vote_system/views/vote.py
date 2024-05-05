from django.shortcuts import render, redirect
from django.views import View
from esn_vote_system.models.vote import Vote, VoteOption, VoteTokenUsed
from esn_vote_system.models.token import Token

class VoteView(View):
    def get(self, request, vote_id):
        if not request.session.get('token'):
            return redirect('index')
        if VoteTokenUsed.does_token_vote_exist(request.session.get('token'), vote_id):
            return redirect('vote_wait', session_id=Vote.objects.get(id=vote_id).session_id)
        vote = Vote.objects.get(id=vote_id)
        return render(request, 'vote.html', {'vote': vote})

    def post(self, request, vote_id):
        if not request.session.get('token'):
            return redirect('index')
            
        if VoteTokenUsed.does_token_vote_exist(request.session.get('token'), vote_id):
            return redirect('vote_wait', session_id=Vote.objects.get(id=vote_id).session_id)
        
        vote = Vote.objects.get(id=vote_id)
        
        token_str = request.session.get('token')
        token = Token.get_token_by_token(token_str)

        if vote.max_num_choices == 1:
            option_id = request.POST.get('option')
            option = VoteOption.objects.get(id=option_id)
            option.number_votes += 1
            option.save()
            VoteTokenUsed.objects.create(token=token, vote_id=vote_id)
        else:
            option_ids = request.POST.getlist('option')
            for option_id in option_ids:
                option = VoteOption.objects.get(id=option_id)
                option.number_votes += 1
                option.save()
            VoteTokenUsed.objects.create(token=token, vote_id=vote_id)

        return redirect('vote_wait', session_id=vote.session_id)
