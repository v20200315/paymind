from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from webpages.decorators import admin_required
from webpages.models import Menu


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "auth/login.html")


def register(request):
    return render(request, "auth/register.html")


def forgot_password(request):
    return render(request, "auth/forgot_password.html")


@login_required(login_url="/login")
def dashboard(request):
    menus = get_user_menus(request.user)
    return render(request, "console/dashboard.html", {"menus": menus})


@login_required(login_url="/login")
def profile(request):
    menus = get_user_menus(request.user)
    return render(request, "console/settings/profile.html", {"menus": menus})


@login_required(login_url="/login")
def security(request):
    menus = get_user_menus(request.user)
    return render(request, "console/settings/security.html", {"menus": menus})


@login_required(login_url="/login")
def sandbox_user(request):
    menus = get_user_menus(request.user)
    return render(request, "console/sandbox/user.html", {"menus": menus})


@login_required(login_url="/login")
def sandbox_member(request):
    menus = get_user_menus(request.user)
    return render(request, "console/sandbox/member.html", {"menus": menus})


@login_required(login_url="/login")
def sandbox_admin(request):
    menus = get_user_menus(request.user)
    return render(request, "console/sandbox/admin.html", {"menus": menus})


@login_required(login_url="/login")
def sandbox_owner(request):
    menus = get_user_menus(request.user)
    return render(request, "console/sandbox/owner.html", {"menus": menus})


def get_user_menus(user):
    role = user.get_role(organization=None)
    menus = Menu.objects.filter(is_active=True, parent__isnull=True).order_by("order")

    def build_tree(menu):
        if menu.role != role:
            return None
        children = [build_tree(c) for c in menu.children.all().order_by("order")]
        children = [c for c in children if c]
        menu.children_tree = children
        return menu

    tree = [build_tree(m) for m in menus]
    return [m for m in tree if m]
