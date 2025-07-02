from django.utils.deprecation import MiddlewareMixin


class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('='*75)
        current_agent = request.META.get('HTTP_USER_AGENT')
        print('='*75)

        if current_agent == 'Chrome':
            print("Chrome browser detected")
        else:
            print("Other browser detected")
        print('=' * 75)

    def process_response(self, request, response):
        response['X-TEST-HEADER'] = 'OUR CUSTOM TEST HEADER FROM DJANGO 5.2.3'
        return response