from django.shortcuts import render,HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Blog
# from django.contrib.auth.models import Users
from .models import User
from django.views.generic import ListView,DetailView
from graphics.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm,  UserLoginForm
from django.shortcuts import redirect
from django.contrib import messages
# from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def logins(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
           email=request.POST.get('email')
           password=request.POST.get('password')
           try:
               user=User.objects.get(email=email)
    
           except:
            # print('Username does not exist!')
            
               messages.error(request, " Email does not exist")
               return render(request,'Sign-in-siginup.html')

           authenticate(request,email=email,password=password)
           user = authenticate(request, email=email, password=password)
           if user is not None:
               login(request, user)
            # if request.user.is_authenticated and user:
               if user.is_authenticated and user.is_staff and user.is_superuser:
            #        messages.success(request,'Authentication is successful')
            #        return redirect('message_chart')
            #    elif user.is_authenticated:
            #        return redirect('choice')
            # return render(request,'admin')
            
                 return redirect('/admin/')
               else:
                  return redirect('index')
             


            #   return HttpResponse("doesnot exist")
        
           else:
            
            # print('Username or password incorrect')
               messages.error(request, "email or password incorrect")
            
               return render(request,'Sign-in-siginup.html')
       else:
        # messages.error(request, "Invalid Username or password.")
           f = UserLoginForm()
           return render(request = request,
                    template_name = "Sign-in-siginup.html",
                context={"f":f})
def SignupPage(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'Sign-in-siginup.html')
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
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                email = form.cleaned_data['email']
                
                
                # Save the form data to database (assuming contactform is a ModelForm)
                form.save()
                # group=Group.objects.get(name="Customer")
                # user.groups.add(group)
                # Student.objects.create(user=user)
                
                sender_email=EMAIL_HOST_USER
        
                sender_message = "Welcome to our page! You are successfully registered ."
                send_mail(
                    'Thank you for your registration',
                    sender_message,
                    sender_email,  
                    [email], 
                    fail_silently=False,
                )
                return redirect('home')
                # return render(request,'message/index.html')
                # return redirect(f"{reverse('index')}#pricing")
        else:
        
          form = RegistrationForm()
        # return render(request, 'message/Login_and_Register.html', {'form': form})
          messages.error(request,'There is some errors')
          return render(request,'Sign-in-siginup.html', {'form': form})
@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")
def logins(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Email does not exist")
                return render(request, "login.html")

            user = authenticate(request, email=email, password=password)
            if user is not None:
                authenticate(request)  # Pass the 'user' object to the authenticate function
                login(request,user)  # Pass the 'request' object to the login function

                if user.is_authenticated and user.is_staff and user.is_superuser:
                    messages.success(request, 'Authentication is successful')
                    return redirect('/admin')
                elif user.is_authenticated:
                    return redirect('index')
                else:
                    return redirect('index')
            else:
                messages.error(request, "Email or password incorrect")
                return render(request, "login.html")
        else:
            f = UserLoginForm()
            return render(request=request,
                          template_name="Sign-in-siginup.html",
                          context={"f": f})
   
def is_valid_form(values):
    valid=True
    for field in values:
        if field=='':
            valid=False
        return valid