from django import template
from esn_vote_system.models.vote import Vote, VoteOption, VoteTokenUsed
from esn_vote_system.models.vote_session import VoteSession
from esn_vote_system.models.token import Token
from django.utils.formats import date_format
from django.utils import translation

register = template.Library()

@register.filter(name='get_vote_options_by_vote_id')
def get_vote_options_by_vote_id(vote_id):
    return VoteOption.objects.filter(vote_id=vote_id)

@register.filter(name='get_first_vote_option_by_vote_id')
def get_first_vote_options_by_vote_id(vote_id):
    return VoteOption.objects.filter(vote_id=vote_id).first()

@register.filter(name='get_second_vote_option_by_vote_id')
def get_second_vote_options_by_vote_id(vote_id):
    return VoteOption.objects.filter(vote_id=vote_id).all()[1]

@register.filter(name='get_third_more_vote_options_by_vote_id')
def get_third_more_vote_options_by_vote_id(vote_id):
    try:
        return VoteOption.objects.filter(vote_id=vote_id).all()[2:]
    except IndexError:
        return []
    
@register.filter(name='get_number_of_vote_options_by_vote_id')
def get_number_of_vote_options_by_vote_id(vote_id):
    return len(VoteOption.objects.filter(vote_id=vote_id))

@register.filter(name='get_vote_token_used_by_token_and_vote_id')
def get_vote_token_used_by_token_and_vote_id(vote_id,token):
    return VoteTokenUsed.does_token_vote_exist(token, Vote.objects.get(id=vote_id))

@register.filter(name='get_number_of_votes')
def get_number_of_votes(vote_id):
    return Vote.get_number_of_votes(vote_id)

@register.filter
def date_format_fr(value):
    translation.activate('fr')
    return date_format(value, "l, j F Y", use_l10n=True)

@register.filter
def get_number_of_votes(vote_id):
    return Vote.get_number_of_votes(vote_id)

@register.filter
def is_number_of_votes_gre_than_number_of_participants(vote_id):
    nb = Vote.get_number_of_votes(vote_id)
    nb_participants = VoteSession.get_active_session().number_of_participants
    print(nb, nb_participants)
    return nb >= nb_participants