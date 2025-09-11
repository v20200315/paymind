from typing import Optional
from rest_framework.pagination import BasePagination
from rest_framework.response import Response
from django.db.models import Q


class DataTablesPagination(BasePagination):
    draw: int
    start: int
    length: int
    search_value: str
    order_column_index: Optional[str]
    order_direction: str
    records_total: int
    records_filtered: int

    def paginate_queryset(self, queryset, request, view=None):
        self.draw = int(request.GET.get("draw", 1))
        self.start = int(request.GET.get("start", 0))
        self.length = int(request.GET.get("length", 10))
        self.search_value = request.GET.get("search[value]", "")
        self.order_column_index = request.GET.get("order[0][column]")
        self.order_direction = request.GET.get("order[0][dir]", "asc")
        # 过滤
        if self.search_value and hasattr(view, "search_fields"):
            q_objects = Q()
            for field in view.search_fields:
                q_objects |= Q(**{f"{field}__icontains": self.search_value})
            queryset = queryset.filter(q_objects)
        self.records_total = queryset.model.objects.count()
        self.records_filtered = queryset.count()
        # 排序
        if self.order_column_index is not None and hasattr(view, "ordering_fields"):
            try:
                column_index = int(self.order_column_index)
                sort_col = view.ordering_fields[column_index]
                if self.order_direction == "desc":
                    sort_col = f"-{sort_col}"
                queryset = queryset.order_by(sort_col)
            except (IndexError, ValueError):
                pass
        # 分页
        return queryset[self.start : self.start + self.length]

    def get_paginated_response(self, data):
        return Response(
            {
                "draw": self.draw,
                "recordsTotal": self.records_total,
                "recordsFiltered": self.records_filtered,
                "data": data,
            }
        )
