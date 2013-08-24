from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from hoarding.forms import HoardingForm
from hoardingusers.forms import LoginForm
from hoarding.models import Hoarding
from django.contrib.auth.decorators import login_required


@login_required
def AddHoarding(request):
    if request.user.is_authenticated() :
        form = HoardingForm()
        if request.method == "POST" :
            form = HoardingForm(request.POST)
            if form.is_valid() :
                hoarding = Hoarding(user                = request.user, 
                                    town                = form.cleaned_data['town'], 
                                    media_type          = form.cleaned_data['media_type'],
                                    width               = form.cleaned_data['width'],
                                    height              = form.cleaned_data['height'],
                                    hoarding_type       = form.cleaned_data['hoarding_type'],
                                    area_particulars    = form.cleaned_data['area_particulars'],
                                    units               = form.cleaned_data['units'],
                                    latitude            = form.cleaned_data['latitude'],
                                    longitude           = form.cleaned_data['longitude'],
                                    diaplay_cost        = form.cleaned_data['diaplay_cost'],
                                    production_cost     = form.cleaned_data['production_cost'],
                                    mounting_cost       = form.cleaned_data['mounting_cost']                                    
                                     )
                hoarding.save()
                #return HttpResponseRedirect('/')
                response_data = {'rslt' : True, 'msg' : 'sucess'}
                return HttpResponse(json.dumps(response_data), mimetype="application/json")
            else :
                context = {'form': form}
                return render_to_response("add_hoarding.html", context, context_instance=RequestContext(request))
        else :
                context = {'form': form}
                return render_to_response("add_hoarding.html", context, context_instance=RequestContext(request))    
    else :
        '''user is not submitting the form, show the login form '''
        form = LoginForm
        context = {'form' : form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))
    
    
    
    




    
    
    
    