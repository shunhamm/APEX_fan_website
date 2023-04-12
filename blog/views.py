from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    photo_list = {}
    return HttpResponse(photo_list)

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
