from django.shortcuts import render, redirect
from django.views import View
from Rentizy.models.user import User
from Rentizy.models.forgot_password import ForgotPassword
from django.contrib.auth.hashers import make_password

class ResetPasswordView(View):

    html_link = 'reset_password.html'

    def get(self, request, token):
        if ForgotPassword.get_forgot_password_by_token(token):
            forgot_password = ForgotPassword.get_forgot_password_by_token(token)
            return render(request, self.html_link, {"token": token})
        
        return redirect('login')

    def post(self, request, token):
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm: # ajouter check password
            forgot_password = ForgotPassword.get_forgot_password_by_token(token)
            user = User.get_user_by_id(forgot_password.user.id)
            user.password = make_password(password)
            user.save()
            forgot_password.delete()
            return redirect('login')
        
        error = "Les mots de passe ne correspondent pas."
        return render(request, self.html_link, {"error": error, "token": token})
