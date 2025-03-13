from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from payment.models import User, Loans
from django.views.decorators.csrf import csrf_exempt


initial_amount = 1000000000

@csrf_exempt
def add_loan(request, user_id):

    if request.method == 'POST':
        data = json.load(request.body)

        if data.get("budget") < initial_amount:
            initial_amount -= data.get("budget")
            new_amount = data.get("budget")
            User.budget = new_amount

            Loans.objects.create(
                user = user_id,
                amount_of_loan = data.get("amount_of_loan"),
                date_of_being_granted = data.get("date_of_being_granted"),
                date_of_last_installment = data.get("date_of_last_installment"),
                number_of_installments = data.get("date_of_last_installment"),
                amount_of_each_pay = (data.get("amount_of_loan") / data.get("date_of_last_installment"))
            )
            HttpResponse(f"Loan granted")

        else:
            raise ValueError("Too much amount bitch! slow down!")

def show_loans(request, user_id):
    return JsonResponse(Loans.objects.get(user_id))

def pay_installment(request, user_id):
    desired_user = User.objects.get(user__id=user_id)
    desired_loan = Loans.objects.get(user=desired_user)
    amount_of_each_pay = desired_loan.amount_of_each_pay
    desired_user.budget -= amount_of_each_pay
    initial_amount += amount_of_each_pay
    return HttpResponse(f"installment paid.")

def pay_completely(request, user_id):
    desired_user = User.objects.get(user__id=user_id)
    desired_loan = Loans.objects.get(user=desired_user)
    desired_user.budget -= 0
    initial_amount += desired_loan
    return HttpResponse(f"installment paid completely.")