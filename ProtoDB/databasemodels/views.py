from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll database.")
    
def details(request, protocol_id):
    return HttpResponse("You're looking at the details for protocol %s." % protocol_id)

def procedure(request, protocol_id):
    return HttpResponse("You're looking at the procedure for protocol %s." % protocol_id)

def rating(request, protocol_id):
    return HttpResponse("You're rating protocol %s." % protocol_id)
    
def favorite(request, protocol_id):
    return HttpResponse("You're favoriting protocol %s." % protocol_id)
