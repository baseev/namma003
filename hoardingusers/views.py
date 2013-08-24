from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from hoardingusers.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from hoardingusers.models import UserInfo
from hoarding.models import Hoarding
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

def HoardingUserRegistration(request):
    if request.user.is_authenticated() :
        return HttpResponseRedirect('/profile/')
    if request.method == "POST" :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            
            user        = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()    
            
            userInfo    = UserInfo(user=user, user_type=form.cleaned_data['user_type'])
            userInfo.save()
                        
            return HttpResponseRedirect('/profile/')
        else :
            context = {'form':form}
            return render_to_response("register.html", context, context_instance=RequestContext(request))
            
    else :
        form = RegistrationForm()
        context = {'form':form}
        return render_to_response("register.html", context, context_instance=RequestContext(request))
    
    
    
def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context = {'form' : form}
        if form.is_valid():
            username    = form.cleaned_data['username']
            password    = form.cleaned_data['password']
            user        = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('login.html', context, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', context, context_instance=RequestContext(request))
        
    else:
        '''user is not submitted the form, show the login form '''
        form = LoginForm
        context = {'form' : form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))
        

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    profile    = request.user.get_profile()
    hoardings = Hoarding.objects.filter(user=profile.user).order_by('-created')
    context = {'profile' : profile, 'hoardings' : hoardings}    
    return render_to_response('profile.html', context, context_instance=RequestContext(request))
    
    




    
    
    
    