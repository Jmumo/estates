from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        email = request.POST['email']
        user_id = request.POST['user_id']

        contact = Contact(listing=listing,listing_id=listing_id,name=name,phone=phone,message=message,
        email=email,user_id=user_id)

        if request.user.is_authenticated:
            user_id = request.user.id 
            has_requested = Contact.objects.all().filter(listing_id = listing_id,user_id = user_id)

            if has_requested:
                messages.error(request,'you have already made a request')
                return redirect('/listings/'+listing_id)


        contact.save()

        send_mail(
            'enquiry on a property',
            'there is a enquiry for the property' ,
            'johnmumo22@gmail.com',
            ['jmn.mumo@gmail.com','kathinirachael96@gmail.com'],

            fail_silently=False
        )

        messages.success(request,'submitted realtor will get back to you soon')


    
        return redirect('/listings/'+listing_id)
       
     