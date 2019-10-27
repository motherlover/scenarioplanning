# import models using: from api.models import Prognose
from rest_framework import viewsets
# import serializers using: from api.serializers import PrognoseSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect 
# import side functions using: from .side_functions import *

# # Example of a view function for a webpage
# def begin_page_2(request): 
#     request.session['scenario_nr'] += 1
#     if request.session['scenario_nr'] == 1:
#         # Process info from portfolio_page
#         results_form = request.POST
#         results_dict = results_form.dict()
#         perc_list = []
#         for branche, eff in results_dict.items():        
#             if 'na_' in branche[:3]: 
#                 perc_list.append(int(eff))
#         request.session['perc_list'] = perc_list       
#     branche_list = request.session['branche_list']    
#     trend_list = Trend.objects.none()
#     prog_list = Prognose.objects.none()
#     for branche in branche_list:
#         currentTrend = Trend.objects.filter(branche__icontains=branche)
#         trend_list = trend_list | currentTrend
#         currentProg = Prognose.objects.filter(branche__icontains=branche)
#         prog_list = prog_list | currentProg       
#     cur_scen = request.session['scenario_nr']
#     request.session[str(cur_scen)] = {}
#     template = loader.get_template('begin_page.html')    
#     context = {       
#         'prog_list': prog_list,
#         'trend_list': trend_list,               
#     }    
#     return HttpResponse(template.render(context, request))

# # Example of a viewset, used as a bridge between the models and serializers
# class PrognoseViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # queryset = Movies.objects.filter(title__contains="Star Wars",type=3)
#     serializer_class = PrognoseSerializer

#     def get_queryset(self):
#         sector = self.request.query_params.get('sector', '')
#         branche = self.request.query_params.get('branche', '')

#         if(sector):
#             return Prognose.objects.filter(sector__icontains=sector)
#         else:
#             return Prognose.objects.filter(branche__icontains=branche)

# Example of a view function for a webpage
def main_page(request):    
    context = {}   
    template = loader.get_template('main_page.html')          
        
    return HttpResponse(template.render(context, request))