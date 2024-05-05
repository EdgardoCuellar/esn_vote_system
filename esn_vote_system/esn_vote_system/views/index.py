from django.shortcuts import render, redirect
from django.views import View
from esn_vote_system.models.token import Token

class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        if Token.is_token_valid(request.POST.get('token')):
            session_id = Token.get_register_token_by_token(request.POST.get('token')).vote_session.id
            # create a request.session['token'] = request.POST.get('token')
            request.session['token'] = request.POST.get('token')
            return redirect('vote_wait', session_id=session_id)
        return render(request, 'index.html', {'error': 'Token invalid'})

def logout(request):
    request.session['token'] = None
    return redirect('index')