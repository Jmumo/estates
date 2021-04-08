from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password = password
        )
        if user is not None:
            auth.login(request,user)
            messages.success(request,'your now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid crediantials')
            return redirect('login')

    

    return render(request, 'accounts/login.html')

def register(request):
    if request.method =='POST':
        fname = request.POST['firstname']
        sname = request.POST['secondname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                 messages.error(request,'username exist')
                 return redirect('register')
                
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email exist')
                    return redirect('register')
                 
                else:
                     user = User.objects.create_user(
                         first_name=fname,
                         last_name=sname,
                         username=username,
                         email=email,
                         password=password
                     )
                     user.save()
                     messages.success(request,'registered you can log in now')
                     return redirect('login')


        else:
            messages.error(request,'passwords do not match')  

            return redirect('register')  
       

    return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'logged out')

    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact-date').filter(user_id = request.user.id)
    
    context = {
        'contacts':user_contacts
    }
    return render(request, 'accounts/dash.html',context)   





