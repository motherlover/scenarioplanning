from api.models import Prognose, Trend, Info, PrognoseEffect, TrendEffect, Development, Devel_for_branche, DevEffect, Requested_Dev, Scenario
from rest_framework import viewsets
from api.serializers import PrognoseSerializer, TrendSerializer, InfoSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.template import loader
import numpy as np
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .side_functions import *
import datetime
import sqlite3
from django.contrib.auth.decorators import login_required
import re

@login_required  
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
    dev_list = Development.objects.none()  
    dev_id_list = []    
    for ids in ids_selected:
        dev_id = ids[2:] 
        dev_id_list.append(dev_id)
        currentDev = Development.objects.filter(rowid=dev_id)  
        dev_list = dev_list | currentDev         
    # Determine current scenario
    cur_scen = request.session['scenario_nr']      
    print(cur_scen)
    # Save prog and trend id's to session              
    request.session[str(cur_scen)]['dev_id_list'] = dev_id_list    
    nr_of_devs = len(dev_list) 
    request.session[str(cur_scen)]['nr_of_devs'] = nr_of_devs 
    request.session.modified = True 
      
    context = {
        'dev_list' : dev_list,
        'buttons' : np.arange(0,5),
        'branche_list': request.session['branche_list'],
    }
    
    return HttpResponse(template.render(context, request))

@login_required
def sector_index(request):
    username = request.user.get_username()
    request.session['username'] = username
    sector_list = []
    branche_list = []  
    # Initialisation
    request.session['scenario_nr'] = 0 
    request.session['dev_requested'] = False   
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

@login_required
def begin_page_2(request): 
    # Process info from sector_index    
    if request.session['scenario_nr'] == 0 and request.session['dev_requested'] != True:
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
    pre_devel_list = Devel_for_branche.objects.none()  
    devel_list = Development.objects.none() 
    for branche in branche_list:
        currentTrend = Trend.objects.filter(branche__icontains=branche)
        trend_list = trend_list | currentTrend
        currentProg = Prognose.objects.filter(branche__icontains=branche)
        prog_list = prog_list | currentProg       
        currentDevels = Devel_for_branche.objects.filter(branche__icontains=branche)
        pre_devel_list = pre_devel_list | currentDevels
    
    id_list = list(set([devel.devel_id for devel in pre_devel_list]))
    
    for id_item in id_list:
        currentDevel = Development.objects.filter(rowid=id_item)
        devel_list = devel_list | currentDevel

    cur_scen = request.session['scenario_nr']
    print(cur_scen)
    # Create a new empty dictionary for this scenario
    request.session[str(cur_scen)] = {}
    template = loader.get_template('begin_page.html')    
    context = {       
        'prog_list': prog_list,
        'trend_list': trend_list,
        'devel_list': devel_list,               
    }    
    return HttpResponse(template.render(context, request))

@login_required
def result_page(request):
    # Process info from effect_page
    port_form = request.POST
    port_dict = port_form.dict()    
    branche_list = request.session['branche_list']  
    cur_scen = request.session['scenario_nr']  
    nr_of_prog_trend = request.session[str(cur_scen)]['nr_of_devs']    
    effect_list = [[] for y in range(0,len(branche_list))]
    for branche, eff in port_dict.items():        
        if 'nd' in branche[:2]:             
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
    new_color_list = []
    for delta in d_eff_sum_list:
        if delta < 0:
            neg_delta = delta*max_eff/min_eff
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
    print(sc_dict[str(cur_scen)]['dev_string_list']) 
    template = loader.get_template('result_page.html')        
    context = {          
        'branche_list' : branche_list,
        'sc_dict' : sc_dict,  
        'prog_string_list' : 'prog_string_list',     
        'trend_string_list' : 'trend_string_list',              
        
    }    
    return HttpResponse(template.render(context, request)) 

@login_required
def result_page_new(request):
    # Process info from effect_page
    port_form = request.POST
    port_dict = port_form.dict()    
    branche_list = request.session['branche_list']  
    cur_scen = request.session['scenario_nr']  
    nr_of_prog_trend = request.session[str(cur_scen)]['nr_of_devs']    
    effect_list = [[] for y in range(0,len(branche_list))]
    for branche, eff in port_dict.items():        
        if 'nd' in branche[:2]:             
            branche_clean = ''.join([i for i in branche[2:] if not i.isdigit()])                       
            effect_list[branche_list.index(branche_clean)].append(int(eff))            
    request.session[str(cur_scen)]['effect_list'] = effect_list 
    request.session.modified = True          
    
    # Pull information per scenario
    request.session.modified = True 
    sc_dict = {}
    for sc in range(1,cur_scen+1):
        sc_dict[str(sc)] = request.session[str(sc)]
    predicted_strings = ['Omzet', 'Ebitda', 'Bruto marge', 'Liquiditeit']
    # Save new scenario data
    last_sc_dict = sc_dict[str(cur_scen)]
    new_dev = last_sc_dict['dev_string_list']
    user = request.session['username']
    todaysdate = datetime.datetime.now().date()
    estdate = todaysdate + datetime.timedelta(days=182)
    # This has to be changed, but all are set 0 for now
    turn_over = 0
    ebitda=0
    bruto_margin=0
    liquidity=0
    # Actual DB stuff    
    for branche in branche_list:
        to_save_scen = Scenario.objects.create(developments=str(new_dev),user=user,date_created=todaysdate,date_estimated=estdate, \
            turn_over=turn_over,ebitda=ebitda,bruto_margin=bruto_margin,liquidity=liquidity,branche=branche)    
        to_save_scen.save()        
    # Remove duplicates
    for row in Scenario.objects.all():
        if Scenario.objects.filter(developments=row.developments,user=row.user,date_created=row.date_created,date_estimated=row.date_estimated, \
            turn_over=row.turn_over,ebitda=row.ebitda,bruto_margin=row.bruto_margin,liquidity=row.liquidity,branche=row.branche).count() > 1:
            row.delete()
    template = loader.get_template('result_page_2.html')        
    context = {          
        'branche_list' : branche_list,
        'sc_dict' : sc_dict,  
        'predicted_strings' : predicted_strings,              
        
    }    
    return HttpResponse(template.render(context, request)) 

@login_required
def effect_page(request):
    # Define the strings to be attached to the heads  of the objects
    add_str_list = [' neemt af/ stagneert/ krimpt', ' neemt licht af/ krimpt lichtelijk', ' stabiel' , ' neemt licht toe/ ontwikkelt/ groeit lichtelijk', ' neemt toe / ontwikkelt / groeit']
    # Process the grading form
    grading_form = request.POST    
    grading_dict = grading_form.dict()
    # Remove csrftoken from the dictionary  
    del(grading_dict['csrfmiddlewaretoken'])  
    # Get the id's of the selected trend and prognose    
    dev_string_qs = []    
    dev_string_list = []
    # Add string to queryset to display it more accurately    
    for ids, on in grading_dict.items():    
        index = on.split('.')            
        add_str = add_str_list[int(index[1])]        
        rowid = ids[1:]
        new_dev_eff = DevEffect()                
        currentDev = Development.objects.filter(rowid=rowid)
        new_dev_eff.body = currentDev[0].development + ':' + add_str
        new_dev_eff.dev_id = currentDev[0].rowid
        dev_string_qs.append(new_dev_eff)
        dev_string_list.append(new_dev_eff.body)   
    cur_scen = request.session['scenario_nr']
    request.session[str(cur_scen)]['dev_string_list'] = dev_string_list
    template = loader.get_template('effect_page.html')  
    branche_list = request.session['branche_list']  
    request.session.modified = True    
    context = { 
        'branche_list': branche_list,
        'dev_list' : dev_string_qs,         
    }    
    return HttpResponse(template.render(context, request))    

# Page to be sent to when you want a new driver to be implemented
@login_required
def request_new_dev(request):
    # Prevent empty scenarios
    request.session['scenario_nr'] = request.session['scenario_nr'] - 1
    # Prevent begin_page from reading the branche_list from the form
    request.session['dev_requested'] = True
    # Read the form
    new_dev_form = request.POST    
    new_dev_dict = new_dev_form.dict()
    for ids,values in new_dev_dict.items():        
        if ids == 'new_dev':
            new_dev = values
    print(new_dev)
    # Write to db for now with user "any"
    user = request.session['username']
    todaysdate = datetime.datetime.today()    
    for_db = Requested_Dev(development=new_dev,user=user,date=todaysdate)
    for_db.save()
    context = {}
    template = loader.get_template('request_new_dev.html')
    return HttpResponse(template.render(context, request))

# Page to be sent to in principle
def home(request):    
    context = {}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

# Page that shows all saved scenarios and allows you to delete them
def scenario_view(request):
    user = request.session['username']
    scenarios = Scenario.objects.filter(user=user)
    # Rewrite development strings and write scenarios to structured dict
    # Sorted by branche
    predicted_strings = ['Omzet', 'Ebitda', 'Bruto marge', 'Liquiditeit']
    i = 0
    sc_dict = {}    
    # Create set of branches
    branche_list = [str(scenario.branche) for scenario in scenarios]
    branche_set = set(branche_list)  
    # Create subdicts
    for branche in branche_set:
        sc_dict[branche] = {}
    # Fill subdicts
    for scenario in scenarios:
        key_list = list(sc_dict[str(scenario.branche)])        
        if key_list == []:
            i = 1
        else:
            int_list = [int(key) for key in key_list]
            i = max(int_list) + 1
        sc_dict[str(scenario.branche)][str(i)] = {}
        dev_string_list = scenario.developments
        clean_dev_string_list = [dev_string.replace('[','').replace(']','').replace("'",'') for dev_string in dev_string_list.split("',")]        
        sc_dict[str(scenario.branche)][str(i)]['dev_string_list'] = clean_dev_string_list
        sc_dict[str(scenario.branche)][str(i)]['predicted_values'] = [scenario.turn_over,scenario.ebitda,scenario.bruto_margin,scenario.liquidity]               
        sc_dict[str(scenario.branche)][str(i)]['date_created'] = scenario.date_created
    context = {
        'sc_dict' : sc_dict,
        'predicted_strings' : predicted_strings,
        'branche_set' : branche_set
        }
    template = loader.get_template('scenario_view.html')
    return HttpResponse(template.render(context, request))

# Redirect page when trying to remove a scenario
def remove_scenario(request):
    user = request.session['username']
    # Read information from the form
    remove_form = (request.POST)
    remove_dict = remove_form.dict()
    print(remove_dict)
    i = 0
    removable_dict = {}
    for branche, on in remove_dict.items():        
        if on == 'on':
            removable_dict[str(i)] = {}
            branche_date_list = branche.split('splitter')
            print(branche_date_list)
            removable_dict[str(i)]['branche'] = branche_date_list[0]
            removable_dict[str(i)]['date_created'] = branche_date_list[1]
            removable_dict[str(i)]['dev_string_list'] = branche_date_list[2]
            i += 1
    # Remove specified scenarios
    print(removable_dict)
    for j in range(0,i):
        dict_to_check = removable_dict[str(j)] 
        print(dict_to_check)       
        Scenario.objects.filter(developments=str(dict_to_check['dev_string_list']),user=user,date_created=dict_to_check['date_created'],branche=dict_to_check['branche']).delete()

    context = {}
    template = loader.get_template('remove_scenario.html')
    return HttpResponse(template.render(context, request))