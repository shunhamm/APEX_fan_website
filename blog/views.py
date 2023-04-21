from django.shortcuts import render, redirect
from urllib.parse import urljoin
from django.http import Http404
from blog import utils
from .models import Character, ExternalLink

def random_character_detail(request):

    character = utils.get_character_profile_at_random()
    context = {'character': character}

    return render(request, 'character_detail.html', context)

def character_detail(request, character_name):

    try:
        character = Character.objects.get(name=character_name)
    except Character.DoesNotExist:
        raise Http404("Character dose not exist")

    context = {'character': character}

    return render(request, 'character_detail.html', context)

def character_list(request):

    try:
        characters = Character.objects.all()
        print(type(characters))
    except:
        raise Http404("Character dose not exist")
    
    context = {'items': characters}

    return render(request, 'item_list.html', context)

def external_links(request):
    
    try:
        external_links = ExternalLink.objects.all()
    except:
        raise Http404("External Link dose not exist")

    external_links = utils.add_image_url(external_links)
    context = {'items': external_links}

    return render(request, 'item_list.html', context)
