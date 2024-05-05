from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

from esn_vote_system.models.vote import VoteOption, Vote, VoteTokenUsed
from esn_vote_system.models.token import Token
from esn_vote_system.models.vote_session import VoteSession


admin.site.register(VoteOption)
admin.site.register(Vote)
admin.site.register(Token)
admin.site.register(VoteSession)
admin.site.register(VoteTokenUsed)
