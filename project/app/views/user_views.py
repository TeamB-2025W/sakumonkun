from django.shortcuts import render, redirect, get_object_or_404
from app.forms import UserCreateForm
from app.models.user_model import User


def info(request):
    context = {
        'user_info': User.objects.all(),
    }

    return render(request, 'app/user_info.html', context)


def register(request):
    form = UserCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:register')
    
    context = {
        'form': form
    }
    return render(request, 'app/user_register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            try:
                user = get_object_or_404(User, username=username, password=password)
                request.session['user_id'] = user.id
                return redirect('app:login')
            except:
                return redirect('app:login')
    
    return render(request, 'app/user_login.html')



def logout(request, pk):
    request.session.clear()
    return render(request, 'app/user_logout.html')


def username(request, pk, username):
    user = get_object_or_404(User, pk=pk, username=username)
    form = UserCreateForm(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:username')
    
    context = {
        'form':form
    }
    return render(request, 'app/user_update.html', context)


def password(request, pk, password):
    user = get_object_or_404(User, pk=pk, password=password)
    form = UserCreateForm(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:password')
    
    context = {
        'form':form
    }
    return render(request, 'app/user_update.html', context)
