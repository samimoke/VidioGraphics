from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'contact.html' )
def portfolio(request):
    return render(request, 'portfolio.html')
def blog(request):
    return render(request,'blog.html')
def service(request):
    return render(request, 'services.html')
def blogDetail(request):
    return render(request,'blog-details.html')
