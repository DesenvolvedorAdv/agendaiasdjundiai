from django import forms
from allauth.account.forms import SignupForm
from django.contrib import messages

class MyCustomSignupForm(SignupForm):
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        # Adicione a mensagem de sucesso aqui
        messages.success(request, 'Cadastro realizado com sucesso! Por favor, faça login.')
        return user