from django.shortcuts import render,HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Blog
from django.views.generic import ListView,DetailView
from graphics.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def LoginPage(request):
    return render(request, 'login.html')

def SignupPage(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'signup.html')
def home(request):
    context = {}
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
class  Blogs(ListView):
    model=Blog
    template_name='blog.html'
    context_object_name = 'posts' 
    # p=Paginator(Blog.objects.all(),3)
    paginate_by = 1
    def get_queryset(self):
        # Your queryset logic goes here
        return Blog.objects.all()
class PostDetail(DetailView):
    model = Blog
    # queryset= Blog.objects.all().order_by('-created_on')[:4]
    queryset = Blog.objects.order_by('-created_on')
    
    # paginator = Paginator(queryset, 3)
    # page_number = request.GET.get('page')
    template_name = 'blog-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()  # Retrieve comments for the post
        context['comments'] = comments
        return context
def service(request):
    return render(request, 'services.html')
def blogDetail(request):
    return render(request,'blog-details.html')
