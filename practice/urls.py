from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import signup,productos,renderLogin,Home

from core.forms import UserLoginForm, ResetPasswordForm, NewPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('PortafolioApp.urls')),  # Asegúrate de que PortafolioApp maneje la ruta raíz

    path('core/', include('core.urls')),  # Prefija las rutas para cada aplicación para evitar conflictos
    path('encuestas/', include('encuestas.urls')),  # Prefija las rutas para encuestas

    path('signup/', signup, name='signup'),
    path('home/', Home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='reset_password.html', form_class=ResetPasswordForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html', form_class=NewPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),
    path('productos/', productos, name='productos'),  # Asegúrate de tener la barra inclinada al fina
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

