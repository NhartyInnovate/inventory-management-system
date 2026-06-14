from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'inventory/',
        views.inventory_list,
        name='inventory_list'
    ),

    path(
        'inventory/add/',
        views.add_inventory,
        name='add_inventory'
    ),

    path(
        'inventory/edit/<int:id>/',
        views.edit_inventory,
        name='edit_inventory'
    ),

    path(
        'inventory/delete/<int:id>/',
        views.delete_inventory,
        name='delete_inventory'
    ),

    path(
        'transactions/',
        views.transaction_list,
        name='transaction_list'
    ),

    path(
        'stock-in/<int:id>/',
        views.stock_in,
        name='stock_in'
    ),

    path(
        'assign/<int:id>/',
        views.assign_asset,
        name='assign_asset'
    ),

    path(
        'reports/',
        views.reports,
        name='reports'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    path(
        'audit-logs/',
        views.audit_logs,
        name='audit_logs'
    ),

]