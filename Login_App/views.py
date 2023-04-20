from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Login_App.forms import SignUpForm, UserProfileChange, ProfilePic
# Create your views here.


# SIGN UP PAGE
def sign_up(request):
    form = SignUpForm() #default
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registered': registered}    
    return render(request, 'Login_App/signup.html', context=dict)   

# SIGN IN Page
def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #all data pick
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # user available or not?
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Blog_App:home'))

    return render(request, 'Login_App/signin.html', context = {'form':form})     


# LOG OUT
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Blog_App:home'))

# user profile
@login_required
def user_profile(request):
    return render(request, 'Login_App/user_profile.html', context={})


# Update profile
@login_required
def user_change(request):
    current_user = request.user #user will save in current_user
    form = UserProfileChange(instance=current_user) # change value of current user
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user) 
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)

    return render(request, 'Login_App/change_profile.html', context={'form':form})        

# PASSWORD CHANGE
@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
    return render(request, 'Login_App/change_pass.html', context={'form':form, 'changed':changed})        


@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request, 'Login_App/profile_pic_add.html', context={'form': form})

@login_required
def change_picture(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request, 'Login_App/profile_pic_add.html', context={'form': form})









