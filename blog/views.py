from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):

    photo_path_list = ["./blog/images/Bloodhound.webp", "blog/images/Pathfinder.webp", "blog/images/Wraith.webp"]
    photo_path = photo_path_list[random.randint(0, 2)]
    return HttpResponse(photo_path)

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
