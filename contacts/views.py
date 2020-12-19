from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, mobile=mobile,subject=subject, message=message)
        contact.save()

        # Send email
        send_mail(
            'Someone sends an inquiry on your portfolio',
            'There has been an inquiry on your Portfolio. Sign into the admin panel for more info',
            'dipanshupandey765@gmail.com',
            ['thedevelopershub05@gmail.com'],
            fail_silently=False
        )

    return render(request, 'contacts/contacts.html')
