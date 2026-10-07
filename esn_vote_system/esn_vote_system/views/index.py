from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from esn_vote_system.models.token import Token


class IndexView(View):

    def get(self, request, token=None):
        # If a token is provided in the URL (from QR code scan), auto-login
        if token:
            if Token.is_token_valid(token):
                try:
                    token_obj = Token.get_register_token_by_token(token)
                    request.session['token'] = token
                    return redirect('vote_wait', session_id=token_obj.vote_session.id)
                except Token.DoesNotExist:
                    return render(request, 'index.html', {'error': 'Invalid or expired key.'})
            else:
                return render(request, 'index.html', {'error': 'Invalid or expired key.'})
        return render(request, 'index.html')
    
    def post(self, request):
        if Token.is_token_valid(request.POST.get('token')):
            session_id = Token.get_register_token_by_token(request.POST.get('token')).vote_session.id
            # create a request.session['token'] = request.POST.get('token')
            request.session['token'] = request.POST.get('token')
            return redirect('vote_wait', session_id=session_id)
        return render(request, 'index.html', {'error': 'Clé invalide'})

def logout(request):
    request.session['token'] = None
    return redirect('index')