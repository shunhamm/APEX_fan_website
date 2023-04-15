from django.shortcuts import render
from django.http import HttpResponse
from blog import user_utils

def index(request):

    character = user_utils.get_character_profile_at_random()
    context = {'character': character}

    return render(request, 'character_detail.html', context)

def rules(request):
    
    game_rule = ""
    return HttpResponse(game_rule)

def notables_detail(request):

    legend_list = {}    
    return HttpResponse(legend_list)

def notables_list(request):

    legend_list = {}
    return HttpResponse(legend_list)

def external_links(request):

    recommend_external_website = {}
    return HttpResponse(recommend_external_website)
