from currencies.models import Currency


def currencies(request):
    currencies = Currency.objects.all()

    if not request.session.get('currency'):
        try:
            request.session['currency'] = Currency.objects.get(is_default__exact=True)
        except Currency.DoesNotExist:
            request.session['currency'] = None

    return {
        'CURRENCIES': currencies,
        'CURRENCY': request.session['currency']
    }
