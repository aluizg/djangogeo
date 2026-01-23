from django.shortcuts import render
from django.views.generic import View
from core.utils import yelp_search, get_client_data

class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        cidade = None
        while not cidade:
            client_data = get_client_data()
            if client_data:
                cidade = client_data.get('city', None)

        termo = request.GET.get('key', None)
        local = request.GET.get('loc', None)

        print('Localidade do Cliente:', cidade)

        context = {
            'city': cidade,
            'busca': False
        }

        if not local:
            local = cidade

        if termo:
            items = yelp_search(keyword=termo, location=local)

            print(f'Search Term: {termo}, Location: {local}')
            print(f'Items Found: {items}')

            context = {
                'items': items,
                'city': local,
                'busca': True
            }

        return render(request, self.template_name, context)