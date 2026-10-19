"""
URL configuration for petshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from pet.views import home,pet_detal,application_form,dashbord,logins,register,logouts,filterpet,ProductListView,ProductDetalView,AdoptionRequestView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=home,name='home'),
    path('petdetail/<int:pk>/',view=pet_detal,name='pet_detail'),
    path('applicationform/<int:pk>/',view=application_form,name='application_form'),
    path('dashbord/',view=dashbord,name='dashbord'),
    path('login/',view=logins,name='login'),
    path('register/',view=register,name='register'),
    path('logout/',view=logouts,name='logout'),
    path('filter/',view=filterpet,name='filter_pet'),
    path("api-auth/", include("rest_framework.urls")),
    path('petlists/',ProductListView.as_view(),name='pet_lists'),
    path('productdetals/<int:pk>/',ProductDetalView.as_view(),name='product_detals'),
      # Path to obtain token (Login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Path to refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('adoptionrequest/',AdoptionRequestView.as_view(),name='adoption_request')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
