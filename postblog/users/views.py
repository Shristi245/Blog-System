from   django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from blog.models import *
from blog.forms import *
from .models import Profile
from django.shortcuts import render, get_object_or_404

def register_user(request):
        
    form = UserRegisterForm()
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print("POST", form)
        print("valid")
        if form.is_valid():
            print("valid")
            user = form.save()
            username = form.cleaned_data.get('username')

           
            messages.success(request,"Account Created for " + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)






# LOGIN
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
            
            
        if user is not None:
            login(request, user)
             
            return redirect('/')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'users/login.html')



# LOGOUT
def logoutUser(request):
    
    logout(request)
    return redirect('login')







class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')





@login_required
def profile(request, username):
       # Get the user's profile or return a 404 error if the user doesn't exist
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    user_posts = user_profile.user.post_set.all() # Assuming your Post model has a ForeignKey to User
    print('posts:', user_posts)

    return render(request, 'users/profile.html', {'user_profile': user_profile, 'user_posts': user_posts})

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'users/profile_update.html', context)


@login_required
def create_post(request):
    if request.method == "POST" and "add" in request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            # Redirect to the home page and pass the newly created post's ID as a parameter
            return redirect("/", post_id=id)
    else:
        form = PostForm()
        

    context = {'form': form}

       
    return render(request, 'users/create.html', )
