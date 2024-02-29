from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contactus',views.contactus, name='contactus'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('blog',views.Blogs.as_view(), name='blog'),
    path('service', views.service, name='service'),
    path('<int:pk>/', views.PostDetail.as_view(), name='blog-detail')

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)