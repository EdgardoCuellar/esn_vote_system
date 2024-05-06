from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from esn_vote_system.views.index import IndexView, logout
from esn_vote_system.views.generate_token import GenerateToken
from esn_vote_system.views.vote_wait import VoteWaitView
from esn_vote_system.views.create_vote import CreateVoteView
from esn_vote_system.views.login_admin import LoginAdminView
from esn_vote_system.views.admin_view import AdminView
from esn_vote_system.views.vote_update import VoteUpdateView, publish_vote, delete_vote
from esn_vote_system.views.vote_results import VoteResultsView
from esn_vote_system.views.vote import VoteView

# Define urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name=''),
    path('generate_token/', GenerateToken.as_view(), name='generate_token'),
    path('vote_wait/<int:session_id>/', VoteWaitView.as_view(), name='vote_wait'),
    path('admin_view/', AdminView.as_view(), name='admin_view'),
    path('logout/', logout, name='logout'),
    path('create_vote/', CreateVoteView.as_view(), name='create_vote'),
    path('login_admin/', LoginAdminView.as_view(), name='login_admin'),
    path('vote_update/<int:vote_id>/', VoteUpdateView.as_view(), name='vote_update'),
    path('publish_vote/<int:vote_id>/', publish_vote, name='publish_vote'),
    path('vote_results/<int:vote_id>/', VoteResultsView.as_view(), name='vote_results'),
    path('vote/<int:vote_id>/', VoteView.as_view(), name='vote'),
    path('delete_vote/<int:vote_id>/', delete_vote, name='delete_vote'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
