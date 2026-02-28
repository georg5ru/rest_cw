from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Пагинация с 5 элементами на странице"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20