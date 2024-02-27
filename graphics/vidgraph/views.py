from django.shortcuts import render,HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from graphics.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the form data to database (assuming contactform is a ModelForm)
            form.save()

            # Send email to receiver
            # receiver_email = 'samimokehirpa@gmail.com'  # Replace with the receiver's email address
            receiver_email=EMAIL_HOST_USER
            send_mail(
                'Contact Form Submission from {}'.format(name),
                message,
                email,  # Sender's email
                [receiver_email],
                fail_silently=False,
            )

            # Send a reply email to the sender
            sender_message = "Welcome to our page! We will contact you soon."
            send_mail(
                'Thank you for contacting us',
                sender_message,
                receiver_email,  # Replace with your own email address
                [email],  # Sender's email
                fail_silently=False,
            )

            return render(request, 'thanks.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    
    
def portfolio(request):
    return render(request, 'portfolio.html')
def blog(request):
    return render(request,'blog.html')
def service(request):
    return render(request, 'services.html')
def blogDetail(request):
    return render(request,'blog-details.html')
