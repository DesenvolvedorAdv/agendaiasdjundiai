from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib import messages
# from django.shortcuts import redirect

@receiver(user_signed_up)
def user_signed_up_request(request, user, **kwargs):
    messages.success(request, 'Registro concluído com sucesso! Por favor, faça login.')
    # return redirect('account_login')
