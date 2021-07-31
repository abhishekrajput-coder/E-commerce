from django.urls import path
from app import views
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *

urlpatterns = [
    path('', views.ProductView.as_view(), name = "home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name= 'showcart'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),


    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('/changepassword/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class= MyPasswordChange, success_url = '/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/', auth_view.PasswordResetDoneView.as_view(template_name='app/passwordchangedone.html'),name = 'passwordchangedone'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='app/passs_reset.html',form_class = MyPasswordResetForm), name= 'password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/pass_reset_confirm.html',form_class=MySetPasswordConfirm), name= 'password_reset_confirm'),
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/pass_reset_done.html'), name= 'password_reset_done'),
    path('password_reset/complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/pass_reset_complete.html'), name= 'password_reset_complete'),

    path('/mobile/', views.mobile, name = 'mobile'),
    path('/mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/',views.laptop,name ='laptop'),
    path('laptop/<slug:data>',views.laptop,name= 'laptopdata'),

    path('login/', auth_view.LoginView.as_view(template_name = 'app/login.html',authentication_form = LoginForm), name='login'),
    path('/logout/', auth_view.LogoutView.as_view(next_page='login'),name= 'logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done, name= 'paymentdone'),
    path('search/',views.search, name='search'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
