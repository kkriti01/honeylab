from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Count
import json

from models import Customer


def home(request):
    cust_count = Customer.objects.count()
    amount = Customer.objects.aggregate(Sum('Amount'))
    cust_order = Customer.objects.values('name').annotate(c=Count('name'))
    order_count_one = []
    order_counts_one = 0
    order_count_two = 0
    order_count_three = 0
    order_count_four = 0
    order_count_five = 0
    for order in cust_order:
        print order
        order_count = order['c']
        if order_count == 1:
            order_count_one.append({'count':order['c'],'name':order['name']})
            order_counts_one += 1
        elif order_count == 2:
            order_count_two += 1
        elif order_count == 3:
            order_count_three += 1
        elif order_count == 4:
            order_count_four += 1
        else:
            order_count_five += 1
    return render(request, 'home.html',{'order_count_one':order_count_one,'cust_count':cust_count,
                                        'order_counts_one':order_counts_one,'amount':amount,
                        'order_count_two':order_count_two,
                        'order_count_three': order_count_three,
                        'order_count_four': order_count_four,
                        'order_count_five': order_count_five})

