from api.models import Prognose, Trend, Info, PrognoseEffect, TrendEffect
from rest_framework import viewsets
from api.serializers import PrognoseSerializer, TrendSerializer, InfoSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.template import loader
import numpy as np
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .side_functions import *


def begin_page(request, sector):    
    info_list = []    
    info_list = Info.objects.filter(sector__icontains=sector)
    if info_list == []:
        info_list = Info.objects.filter(branche__icontains=sector)  
    prog_list = []    
    prog_list = Prognose.objects.filter(sector__icontains=sector)
    if prog_list == []:
        prog_list = Prognose.objects.filter(branche__icontains=sector)
    trend_list = []    
    trend_list = Trend.objects.filter(sector__icontains=sector)
    if trend_list == []:
        trend_list = Trend.objects.filter(branche__icontains=sector)       
    template = loader.get_template('begin_page.html')        
    context = {         
        'info_list': info_list,
        'prog_list': prog_list,
        'trend_list': trend_list,       
    }    

    return HttpResponse(template.render(context, request))
  
def grading(request):    
    template = loader.get_template('grading.html')
    # Get dictionary from form
    grading_form = request.POST    
    grading_dict = grading_form.dict()
    # Get the id's of the selected trend and prognose
    ids_selected= []
    for ids, on in grading_dict.items():        
        if on == 'on':
            ids_selected.append(ids)
    trend_list = Trend.objects.none()
    prog_list = Prognose.objects.none()
    trend_id_list = []
    prog_id_list = []
    for ids in ids_selected:
        if 't' in ids:
            trend_id = ids[2:]
            trend_id_list.append(trend_id)
            currentTrend = Trend.objects.filter(trend_id=trend_id)
            trend_list = trend_list | currentTrend                        
        if 'p' in ids:
            prog_id = ids[2:] 
            prog_id_list.append(prog_id)
            currentProg = Prognose.objects.filter(prog_id=prog_id)  
            prog_list = prog_list | currentProg 
    # Determine current scenario
    cur_scen = request.session['scenario_nr']      
     
    # Save prog and trend id's to session              
    request.session[str(cur_scen)]['trend_id_list'] = trend_id_list
    request.session[str(cur_scen)]['prog_id_list'] = prog_id_list
    nr_of_prog_trend = len(prog_list) + len(trend_list)
    request.session[str(cur_scen)]['nr_of_prog_trend'] = nr_of_prog_trend 
    request.session.modified = True 
      
    context = {
        'prog_list': prog_list,
        'trend_list': trend_list,
        'buttons' : np.arange(0,5),
        'branche_list': request.session['branche_list'],
    }
    
    return HttpResponse(template.render(context, request))

def show_occs(request):
    grading_form = request.POST    
    grading_dict = grading_form.dict()
    # Get the id's of the selected trend and prognose
    ids_selected= []
    for ids, on in grading_dict.items():        
        if on == 'on':
            ids_selected.append(ids)
    trend_list = Trend.objects.none()
    prog_list = Prognose.objects.none()
    for ids in ids_selected:
        if 't' in ids:
            trend_id = ids[2:]
            currentTrend = Trend.objects.filter(trend_id=trend_id)
            trend_list = trend_list | currentTrend
        if 'p' in ids:
            prog_id = ids[2:] 
            currentProg = Prognose.objects.filter(prog_id=prog_id)  
            prog_list = prog_list | currentProg
    search_list = ['bouwmaterialenindustrie']
    context_list = [['staal' , 'metaal']]
    title_list = [['OR Tata Steel vreest nog meer dan 4000 ontslagen door fusie', 'Nieuwe eigenaar aluminiumfabriek Aldel investeert 30 miljoen euro' ]]    
    url_list = [['https://www.rtlz.nl/beurs/bedrijven/or-tata-steel-vreest-nog-meer-dan-4000-ontslagen-door-fusie','https://www.rtlz.nl/algemeen/binnenland/nieuwe-eigenaar-aluminiumfabriek-aldel-investeert-30-miljoen-euro']]  
    if search_list == []: 
        context = {}   
    else: 
        context = {
            'search_list': search_list,
            'title_list': title_list,             
            'url_list': url_list,
            'number_list': np.arange(0,len(search_list)),
            'context_list': context_list            
        }        
    template = loader.get_template('show_occs.html')
    return HttpResponse(template.render(context, request))

def sector_index(request): 
    sector_list = []
    branche_list = []  
    request.session['scenario_nr'] = 0    
    sectors = Info.objects.raw('select * from info_table where info_id in (select min(info_id) from info_table group by sector)') 
    for sector in sectors:
        current_sector = []
        sector_list.append(sector.sector)        
        current_sector_lines = Info.objects.filter(sector__icontains=sector.sector)
        for line in current_sector_lines:
            current_sector.append(line.branche)
        branche_list.append(current_sector)  
    template = loader.get_template('sector_index.html')
    context = {
        'sector_list': sector_list,
        'branche_list': branche_list,
    }    
    return HttpResponse(template.render(context, request))

def begin_page_2(request): 
    # Process info from sector_index    
    if request.session['scenario_nr'] == 0:
        branche_form = (request.POST)
        branche_dict = branche_form.dict()
        branche_list = []
        for branche, on in branche_dict.items():        
            if on == 'on':
                branche_list.append(branche)    
        request.session['branche_list'] = branche_list 
    # Make layout of session info
    request.session['scenario_nr'] += 1
    # Retrieve the trends and prognoses from the db       
    branche_list = request.session['branche_list']    
    trend_list = Trend.objects.none()
    prog_list = Prognose.objects.none()    
    for branche in branche_list:
        currentTrend = Trend.objects.filter(branche__icontains=branche)
        trend_list = trend_list | currentTrend
        currentProg = Prognose.objects.filter(branche__icontains=branche)
        prog_list = prog_list | currentProg       
    cur_scen = request.session['scenario_nr']
    # Create a new empty dictionary for this scenario
    request.session[str(cur_scen)] = {}
    template = loader.get_template('begin_page.html')    
    context = {       
        'prog_list': prog_list,
        'trend_list': trend_list,               
    }    
    return HttpResponse(template.render(context, request))

def result_page(request):
    # Process info from effect_page
    port_form = request.POST
    port_dict = port_form.dict()    
    branche_list = request.session['branche_list']  
    cur_scen = request.session['scenario_nr']  
    nr_of_prog_trend = request.session[str(cur_scen)]['nr_of_prog_trend']    
    effect_list = [[] for y in range(0,len(branche_list))]
    for branche, eff in port_dict.items():        
        if 'nt' in branche[:2] or 'np' in branche[:2]:             
            branche_clean = ''.join([i for i in branche[2:] if not i.isdigit()])                       
            effect_list[branche_list.index(branche_clean)].append(int(eff))            
    request.session[str(cur_scen)]['effect_list'] = effect_list 
    request.session.modified = True         
          
    # Let positives range from green to yellow and negatives from red to yellow    
    # Find the sum of the effects
    eff_sum_list = [sum(i) for i in effect_list]
    # Base color is yellow    
    yellow = np.array([255,255,50])    
    # RGB change required for red and green
    dred = np.array([0,-205,0])
    dgreen = np.array([-205,0,0])
    # Find largest negative and largest positive
    min_eff = min(eff_sum_list)
    max_eff = max(eff_sum_list)
    # Add delta based on effect value w.r.t. 0 and the highest negative or positive
    d_eff_sum_list = [float(eff)/max_eff for eff in eff_sum_list]
    print(d_eff_sum_list)
    new_color_list = []
    for delta in d_eff_sum_list:
        if delta < 0:
            print(delta)
            neg_delta = delta*max_eff/min_eff
            print(neg_delta)
            color = yellow + neg_delta * dred
        else:
            color = yellow + delta * dgreen
        new_color_list.append(color)
    # Create a list of strings with rgb(a,b,c)
    color_list = ['rgb('+ str(int(rgb[0])) + ',' + str(int(rgb[1])) + ',' + str(int(rgb[2])) + ')' for rgb in new_color_list]
    request.session[str(cur_scen)]['color_list'] = color_list
    # Pull information per scenario
    request.session.modified = True 
    sc_dict = {}
    for sc in range(1,cur_scen+1):
        sc_dict[str(sc)] = request.session[str(sc)]
    template = loader.get_template('result_page.html')        
    context = {          
        'branche_list' : branche_list,
        'sc_dict' : sc_dict,  
        'prog_string_list' : 'prog_string_list',     
        'trend_string_list' : 'trend_string_list',              
        
    }    
    return HttpResponse(template.render(context, request)) 

def portfolio_page(request):
    # Process info from sector_index    
    branche_form = (request.POST)
    branche_dict = branche_form.dict()
    branche_list = []
    for branche, on in branche_dict.items():        
        if on == 'on':
            branche_list.append(branche)    
    request.session['branche_list'] = branche_list         
    template = loader.get_template('portfolio_page.html')    
    context = { 'branche_list' : branche_list}    
    return HttpResponse(template.render(context, request)) 

def effect_page(request):
    # Define the strings to be attached to the heads  of the objects
    add_str_list = [' neemt af/ stagneert/ krimpt', ' neemt licht af/ krimpt lichtelijk', ' stabiel' , ' neemt licht toe/ ontwikkelt/ groeit lichtelijk', ' neemt toe / ontwikkelt / groeit']
    # Process the grading form
    grading_form = request.POST    
    grading_dict = grading_form.dict()
    # Get the id's of the selected trend and prognose    
    trend_string_qs = []
    prog_string_qs = []
    trend_string_list = []
    prog_string_list = []
    # Add string to queryset to display it more accurately    
    for ids, on in grading_dict.items():                
        if 't' in ids[0] or 'p' in ids[0]:
            index = on.split('.')            
            add_str = add_str_list[int(index[1])]            
            if 't' in ids:
                trend_id = ids[1:]
                new_trend_eff = TrendEffect()                
                currentTrend = Trend.objects.filter(trend_id=trend_id)
                new_trend_eff.body = currentTrend[0].head + ':' + add_str
                new_trend_eff.trend_id = currentTrend[0].trend_id
                trend_string_qs.append(new_trend_eff)
                trend_string_list.append(new_trend_eff.body)       
            else:
                prog_id = ids[1:]
                new_prog_eff = PrognoseEffect()                 
                currentProg = Prognose.objects.filter(prog_id=prog_id)                
                new_prog_eff.body = currentProg[0].head + ':' + add_str 
                new_prog_eff.prog_id = currentProg[0].prog_id
                prog_string_qs.append(new_prog_eff)
                prog_string_list.append(new_prog_eff.body)   
    cur_scen = request.session['scenario_nr']
    request.session[str(cur_scen)]['trend_string_list'] = trend_string_list
    request.session[str(cur_scen)]['prog_string_list'] = prog_string_list
    template = loader.get_template('effect_page.html')  
    branche_list = request.session['branche_list']  
    request.session.modified = True    
    context = { 
        'branche_list': branche_list,
        'prog_list' : prog_string_qs,
        'trend_list' : trend_string_qs, 
    }    
    return HttpResponse(template.render(context, request))    

