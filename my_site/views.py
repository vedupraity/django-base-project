from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class SiteLoginView(LoginView):
    success_url = reverse_lazy('site-dashboard-view')
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or self.success_url


class SiteLogoutView(LogoutView):
    next_page = reverse_lazy('site-login-view')


class SiteRegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('site-login-view')
    template_name = 'register.html'


class SiteDashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('site-login-view')
    template_name = 'dashboard.html'
