from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.db.models import Sum

def main_budget(request):
    # Retrieve all entries
    entries = Entry.objects.all()

    # Calculate totals for income, debits, and balance
    total_income = entries.aggregate(Sum('income'))['income__sum'] or 0
    total_debits = entries.aggregate(Sum('debits'))['debits__sum'] or 0
    total_balance = entries.aggregate(Sum('balance'))['balance__sum'] or 0

    # Handle the form submission
    form = EntryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_budget')  # Redirect to the main budget page

    # Render the template with context data
    return render(request, 'budget/main_budget.html', {
        'entries': entries,
        'total_income': total_income,
        'total_debits': total_debits,
        'total_balance': total_balance,
        'form': form
    })

def reports(request):
    entries = Entry.objects.all()
    total_spent = entries.aggregate(Sum('debits'))['debits__sum'] or 0
    total_income = entries.aggregate(Sum('income'))['income__sum'] or 0
    remaining = total_income - total_spent

    category_data = (
        entries.values('category')
        .annotate(total_debits=Sum('debits'))
        .order_by('-total_debits')
    )
    categories = [item['category'] for item in category_data]
    category_spends = [float(item['total_debits']) for item in category_data]

    return render(request, 'budget/reports.html', {
        'total_spent': total_spent,
        'remaining': remaining,
        'categories': categories,
        'category_spends': category_spends,
    })
