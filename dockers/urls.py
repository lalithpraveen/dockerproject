# urls.py
from django.urls import path
from .views import FileUploadView, DocketListView, create_docket_entry, get_purchase_order_description, get_purchase_orders, CreatedDocketsListView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file_upload'),
    path('dockets/', DocketListView.as_view(), name='docket_list'),
    path('create_docket_entry/', create_docket_entry, name='create_docket_entry'),
    path('get_purchase_orders/', get_purchase_orders, name='get_purchase_orders'),
    path('get_purchase_order_description/', get_purchase_order_description, name='get_purchase_order_description'),
    path('created_dockets/', CreatedDocketsListView.as_view(), name='created_dockets_list'),
]
