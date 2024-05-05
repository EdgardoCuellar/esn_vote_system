from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from esn_vote_system.models.token import Token
from esn_vote_system.models.vote_session import VoteSession

from django.conf import settings


class LoginAdminView(View):
    html_link = 'login_admin.html'

    def get(self, request):
        sessions = VoteSession.get_open_vote_sessions()
        return render (request, self.html_link, {'sessions': sessions})

    def post(self, request):
        key = request.POST.get('token')

        error_message = None

        if Token.check_key(key):
            request.session['admin_token'] = True
            return redirect('admin_view')
        
        error_message = 'Clé invalide !'

        return render (request, self.html_link, {'error': error_message})
    
