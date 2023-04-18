from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog import user_utils
from .models import Character

def random_character_detail(request):

    character = user_utils.get_character_profile_at_random()
    context = {'character': character}

    return render(request, 'character_detail.html', context)

def character_detail(request, character_name):

    try:
        character = Character.objects.get(name=character_name)
    except Character.DoesNotExist:
        raise Http404("Character dose not exist")

    context = {'character': character}

    return render(request, 'character_detail.html', context)

def notables_list(request):

    legend_list = {}
    return HttpResponse(legend_list)

def external_links(request):

    recommend_external_website = {}
    return HttpResponse(recommend_external_website)
