from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from django.conf import settings
from M2Crypto import EVP


@csrf_exempt
def sign_printer_request(request):
    # Load the private key
    # http://chandlerproject.org/Projects/MeTooCrypto
    key = EVP.load_key_string(open(settings.QZTRAY_PRIVATE_KEY).read())

    # Create the signature
    key.sign_init()
    key.sign_update(request.body)
    signature = key.sign_final()

    return HttpResponse(base64.b64encode(signature), content_type='text/plain')
