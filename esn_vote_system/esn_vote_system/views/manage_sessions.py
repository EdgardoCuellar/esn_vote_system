from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.vote import Vote
import datetime


class ManageSessionsView(View):
    template_name = 'manage_sessions.html'

    def get(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')

        sessions = VoteSession.objects.all().order_by('-date', '-id')
        open_sessions = VoteSession.get_open_vote_sessions()

        return render(request, self.template_name, {
            'sessions': sessions,
            'open_sessions': open_sessions,
        })

    def post(self, request):
        if not request.session.get('admin_token'):
            return redirect('login_admin')

        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        date_str = request.POST.get('date', '').strip()

        if not title:
            sessions = VoteSession.objects.all().order_by('-date', '-id')
            return render(request, self.template_name, {
                'sessions': sessions,
                'open_sessions': VoteSession.get_open_vote_sessions(),
                'error': 'Title is required.',
            })

        # Try to parse the date
        session_date = None
        if date_str:
            try:
                from django.utils.dateparse import parse_datetime
                session_date = parse_datetime(date_str)
                if session_date is None:
                    # Try date only (HTML5 date input)
                    from datetime import datetime as dt
                    session_date = dt.strptime(date_str, '%Y-%m-%d')
            except (ValueError, TypeError):
                session_date = datetime.datetime.now()

        VoteSession.objects.create(
            title=title,
            description=description,
            date=session_date,
        )

        return redirect('manage_sessions')


def close_session(request, session_id):
    if not request.session.get('admin_token'):
        return redirect('login_admin')

    session = get_object_or_404(VoteSession, pk=session_id)
    session.is_closed = True
    session.save()
    return redirect('manage_sessions')


def update_participants(request, session_id):
    if not request.session.get('admin_token'):
        return redirect('login_admin')

    session = get_object_or_404(VoteSession, pk=session_id)
    try:
        nb = int(request.POST.get('number_of_participants', 0))
        if nb < 0:
            nb = 0
        session.number_of_participants = nb
        session.save()
    except (ValueError, TypeError):
        pass

    return redirect('manage_sessions')