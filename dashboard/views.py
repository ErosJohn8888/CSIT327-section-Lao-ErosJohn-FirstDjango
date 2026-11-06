from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.db.models import Q
from django.views.generic import TemplateView
from accounts.models import CustomUser

class AdminPanelView(LoginRequiredMixin,
                    UserPassesTestMixin, TemplateView):
    template_name = "dashboard/admin_panel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_count"] = CustomUser.objects.count()
        context["admin_count"] = CustomUser.objects.filter(
            Q(is_staff=True)
            | Q(is_superuser=True)
            | Q(role=CustomUser.Role.ADMIN)
        ).count()
        context["active_count"] = CustomUser.objects.filter(
            is_active=True
        ).count()
        context["members"] = CustomUser.objects.order_by(
            "-date_joined"
        )[:100]
        return context

    def test_func(self):
        user = self.request.user
        return (
            user.is_staff
            or user.is_superuser
            or user.role == CustomUser.Role.ADMIN
        )

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_count"] = CustomUser.objects.count()
        context["is_admin"] = (
            self.request.user.is_staff
            or self.request.user.is_superuser
            or self.request.user.role == CustomUser.Role.ADMIN
        )
        return context