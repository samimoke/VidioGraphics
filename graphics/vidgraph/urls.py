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
    path('register',views.register, name='register'),
    path('service', views.service, name='service'),
    path('<int:pk>/', views.PostDetail.as_view(), name='blog-detail'),
    path('login',views.logins,name="login"),
    path('logout',views.logout_request,name='logout'),
    path('paginate/', views.paginate, name='paginate'),
    path('<int:pk>/add_comment/', views.add_comment_to_post, name='add_comment'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/',views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
