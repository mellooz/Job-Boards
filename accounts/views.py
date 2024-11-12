from django.shortcuts import redirect, render 
from django.urls import reverse
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate , login 
from .models import Profile , City
# Create your views here.


def signup(request):
    if request.method=='POST':
        #if request method=post (pressed signup button) then do (take the data from the form using -> SignupForm(request.POST))
        form = SignupForm(request.POST)
        # if data is valid
        if form.is_valid():
            form.save()
            # when u signup u should be loggedin and django should change ur session
            # and update the session with my username and password
            # we get username and password from the form using cleaned_data['FieldName']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # u most authenticate by send the session username and password to check that u r
            # authenticate takes to args username=,password= 
            # authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            user = authenticate(username=username , password=password)
            # then login (login is built in func)
            login(request , user)
            return redirect('/accounts/profile/')
    else:
        # if u didnt press signup button (that only show the form)
        form = SignupForm()
    return render(request ,'registration/signup.html' , {'form' : form})



# func view to show the profile
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request , 'accounts/profile.html' , {'profile' : profile})



# func view to show the edit profile 
def profile_edit(request):
    # we write this cuz u need the currnet user info profile = Profile.objects.get(user=request.user)
    # request.user refer to current user
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST' : 
        # instance=request.user refer to the current data
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            # we will not save profileform now 
            myprofile = profileform.save(commit=False)
            # cuz the profile need to take user field first
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else :
        # we will write this cuz when u edit ur profile u see ur username and email... then delete it and write the new
        # so write this instance=request.user to get user data
        userform = UserForm(instance=request.user)
        # so write this instance=profile to get profile data
        profileform = ProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})
