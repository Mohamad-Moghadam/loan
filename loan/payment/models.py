from django.db import models


class User(models.Model):
    name = models.CharField(max_length= 100)
    budget = models.PositiveBigIntegerField()

class Loans(models.Model):
    user = models.ForeignKey(to= User, on_delete= models.CASCADE, related_name= 'loans_of_each_use')
    amount_of_loan = models.PositiveBigIntegerField()
    date_of_being_granted = models.DateField(auto_now_add= True)
    date_of_last_installment = models.DateField()
    number_of_installments = models.DateField()
    amount_of_each_pay = models.PositiveIntegerField()