from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")
        if request.user.role != "admin":  # 假设 CustomUser 有 role 字段
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapper
