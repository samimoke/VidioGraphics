from django.shortcuts import render,HttpResponse, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Blog, Video
from django.http import JsonResponse
from .models import User
from django.views.generic import ListView,DetailView
from graphics.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm,  UserLoginForm, CommentForm, SubscriptionForm
from django.shortcuts import redirect
from django.contrib import messages
# from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm


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
    return render(request, 'Sign-in-siginup.html',context)
def home(request):
    video=Video.objects.all()
    return render(request,'index.html',{'videos':video})
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

class Blogs(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        # Your queryset logic goes here
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_list = self.get_queryset()
        paginator = Paginator(blog_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context
def paginate(request):
    page_number = request.GET.get('page')
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return JsonResponse({'html': render_to_string('blog.html', context)})
class PostDetail(DetailView):
    model = Blog
    queryset = Blog.objects.order_by('-created_on')
    template_name = 'blog-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object  # Add the 'post' object to the context
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
                messages.error(request,'Check if you input unique email and other correct credientials')
                return render(request,'Sign-in-siginup.html', {'form': form})
        return render(request,'Sign-in-siginup.html')        
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
                return render(request, "Sign-in-siginup.html")

            user = authenticate(request, email=email, password=password)
            if user is not None:
                authenticate(request)  # Pass the 'user' object to the authenticate function
                login(request,user)  # Pass the 'request' object to the login function

                if user.is_authenticated and user.is_staff and user.is_superuser:
                    messages.success(request, 'Authentication is successful')
                    return redirect('/admin')
                elif user.is_authenticated:
                    return redirect('home')
                else:
                    return redirect('login')
            else:
                messages.error(request, "Your password is incorrect")
                return render(request, "Sign-in-siginup.html")
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
def add_comment_to_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
        return redirect('blog-detail', pk=post.pk)
        
        # return render(request, 'Post_detail.html', {'comment':comment})
     
    else:
        form = CommentForm()
    return render(request, 'blog-details.html', {'form': form})
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you, you are successfully subscribed')
            return redirect('home')
        else:
           form = SubscriptionForm()
           return render(request, 'blog-details.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    form = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'emails/password_reset_email.txt'  # Custom plain text template
    html_email_template_name = 'emails/password_reset_email.html'  # Custom HTML template


    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        subject_template_name = 'emails/password_reset_subject.txt'
        # Render the subject
        subject = render_to_string(subject_template_name, context).strip()

        # Render the plain text message
        body = render_to_string(email_template_name, context)
        from_email = EMAIL_HOST_USER

        # Get to_email from context
        to_email = [context.get('email')]

        # Render the HTML message (if provided)
        html_message = render_to_string(html_email_template_name, context) if html_email_template_name else None

        # Send the email
        send_mail(
            subject,
            body,
            from_email,
            to_email,
            html_message=html_message,
        )

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

       