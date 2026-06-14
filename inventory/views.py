from .models import InventoryItem
from .forms import (
    InventoryItemForm,
    StockInForm,
    AssetAssignmentForm
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count

from .models import StockTransaction, AuditLog
from django.shortcuts import get_object_or_404
from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth import (
    authenticate,
    login,
    logout
)


from .models import (
    Category,
    InventoryItem,
    AssetAssignment,
    StockTransaction
)

def is_admin(user):
    return user.is_superuser

@login_required
def dashboard(request):

    total_categories = Category.objects.count()

    total_items = InventoryItem.objects.count()

    total_assets_assigned = AssetAssignment.objects.count()

    total_transactions = StockTransaction.objects.count()

    recent_transactions = StockTransaction.objects.order_by(
        '-transaction_date'
    )[:5]

    low_stock_items = InventoryItem.objects.filter(
        quantity__lte=5
    )

    category_data = Category.objects.annotate(
        total=Count('inventoryitem')
    ).filter(
        total__gt=0
    )

    stock_in_count = StockTransaction.objects.filter(
        transaction_type='IN'
    ).count()

    stock_out_count = StockTransaction.objects.filter(
        transaction_type='OUT'
    ).count()


    context = {
        'total_categories': total_categories,
        'total_items': total_items,
        'total_assets_assigned': total_assets_assigned,
        'total_transactions': total_transactions,
        'recent_transactions': recent_transactions,
        'low_stock_items': low_stock_items,
        'category_data': category_data,
        'stock_in_count': stock_in_count,
        'stock_out_count': stock_out_count,
    }

    return render(
        request,
        'inventory/dashboard.html',
        context
    )

@login_required
def inventory_list(request):

    items = InventoryItem.objects.all()

    context = {
        'items': items
    }

    return render(
        request,
        'inventory/inventory_list.html',
        context
    )


@user_passes_test(is_admin)
def add_inventory(request):

    form = InventoryItemForm(
        request.POST or None
    )

    if form.is_valid():

        item = form.save()

        create_audit_log(
            request.user,
            "Inventory Created",
            f"{item.name} was added"
        )

        return redirect('inventory_list')

    else:

        print(form.errors)

    context = {
        'form': form
    }

    return render(
        request,
        'inventory/add_inventory.html',
        context
    )

@user_passes_test(is_admin)
def edit_inventory(request, id):

    item = get_object_or_404(
        InventoryItem,
        id=id
    )

    form = InventoryItemForm(
        request.POST or None,
        instance=item
    )

    if form.is_valid():

        form.save()
        create_audit_log(
            request.user,
            "Inventory Updated",
            f"{item.name} was updated"
        )

        return redirect(
            'inventory_list'
        )

    return render(
        request,
        'inventory/add_inventory.html',
        {'form': form}
    )


@user_passes_test(is_admin)
def delete_inventory(request, id):

    item = get_object_or_404(
        InventoryItem,
        id=id
    )

    create_audit_log(
        request.user,
        "Inventory Deleted",
        f"{item.name} was deleted"
    )

    item.delete()

    return redirect(
        'inventory_list'
    )

@login_required
def transaction_list(request):

    transactions = StockTransaction.objects.all().order_by(
        '-transaction_date'
    )

    context = {
        'transactions': transactions
    }

    return render(
        request,
        'inventory/transaction_list.html',
        context
    )

@user_passes_test(is_admin)
def stock_in(request, id):

    item = get_object_or_404(
        InventoryItem,
        id=id
    )

    form = StockInForm(
        request.POST or None
    )

    if form.is_valid():

        quantity = form.cleaned_data[
            'quantity'
        ]

        # Increase stock

        item.quantity += quantity

        item.save()

        # Create transaction record

        StockTransaction.objects.create(
            item=item,
            user=request.user,
            transaction_type='IN',
            quantity=quantity,
            description='Stock added'
        )

        create_audit_log(
            request.user,
            "Stock In",
            f"{quantity} units added to {item.name}"
        )

        return redirect(
            'inventory_list'
        )

    context = {
        'item': item,
        'form': form
    }

    return render(
        request,
        'inventory/stock_in.html',
        context
    )

@user_passes_test(is_admin)
def assign_asset(request, id):

    item = get_object_or_404(
        InventoryItem,
        id=id
    )

    if item.quantity <= 0:

        return redirect(
            'inventory_list'
        )

    form = AssetAssignmentForm(
        request.POST or None
    )

    if form.is_valid():

        assignment = form.save(
            commit=False
        )

        assignment.item = item

        assignment.assigned_by = request.user

        assignment.save()

        create_audit_log(
            request.user,
            "Asset Assigned",
            f"{item.name} assigned to {assignment.assigned_to}"
        )

        # Reduce inventory

        item.quantity -= 1

        item.save()

        # Create stock transaction

        StockTransaction.objects.create(
            item=item,
            user=request.user,
            transaction_type='OUT',
            quantity=1,
            description=f'Assigned to {assignment.assigned_to}'
        )



        return redirect(
            'assign_asset',
            id=item.id
        )

    assignments = AssetAssignment.objects.all().order_by(
        '-assigned_date'
    )

    context = {
        'item': item,
        'form': form,
        'assignments': assignments
    }

    return render(
        request,
        'inventory/assign_asset.html',
        context
    )

@login_required
def reports(request):

    total_items = InventoryItem.objects.count()

    total_categories = Category.objects.count()

    total_assignments = AssetAssignment.objects.count()

    total_transactions = StockTransaction.objects.count()

    low_stock_items = InventoryItem.objects.filter(
        quantity__lte=5
    )

    recent_transactions = StockTransaction.objects.order_by(
        '-transaction_date'
    )[:5]

    context = {

        'total_items': total_items,

        'total_categories': total_categories,

        'total_assignments': total_assignments,

        'total_transactions': total_transactions,

        'low_stock_items': low_stock_items,

        'recent_transactions': recent_transactions
    }

    return render(
        request,
        'inventory/reports.html',
        context
    )

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )

    return render(
        request,
        'inventory/login.html'
    )

def user_logout(request):

    logout(request)

    return redirect(
        'login'
    )

def create_audit_log(
    user,
    action,
    description
):

    AuditLog.objects.create(
        user=user,
        action=action,
        description=description
    )

@login_required
def audit_logs(request):

    logs = AuditLog.objects.order_by(
        '-timestamp'
    )

    context = {
        'logs': logs
    }

    return render(
        request,
        'inventory/audit_logs.html',
        context
    )