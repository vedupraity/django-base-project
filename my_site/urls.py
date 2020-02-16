from django.urls import path

from .views import SiteDashboardView, SiteLoginView, SiteLogoutView, SiteRegisterView


urlpatterns = [
    path('', SiteLoginView.as_view(), name='site-login-view'),
    path('logout/', SiteLogoutView.as_view(), name='site-logout-view'),
    path('register/', SiteRegisterView.as_view(), name='site-register-view'),
    path('dashboard/', SiteDashboardView.as_view(), name='site-dashboard-view'),
]
