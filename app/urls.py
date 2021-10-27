"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # Admin Management
                  path('admin/', admin.site.urls),

                  # REST Auth
                  path('api/', include('rest_framework.urls')),
                  path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
                  path('api/dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
                  path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
                  path('api/dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(),
                       name='account_email_verification_sent'),
                  path('api/dj-rest-auth/password/reset/confirm/<slug:uidb64>/<slug:token>/',
                       PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),

                  # User Management

                  # REST management
                  path('api/', include('todos.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
