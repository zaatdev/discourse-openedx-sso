from urllib.parse import parse_qs, urlencode, quote
import hashlib, hmac, base64

from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def _sign(payload):
    return hmac.new(
    settings.DISCOURSE_SECRET.encode(),
    msg=payload.encode(),
    digestmod = hashlib.sha256
    ).hexdigest()

def _validate_sign(sso,sign):
    return hmac.compare_digest(_sign(sso),sign)

def _create_payload(sso,user):
    payload = {}
    based64_decoded_request = base64.b64decode(sso)
    url_decoded_request = parse_qs(based64_decoded_request.decode())
    nonce = url_decoded_request['nonce'][0]
    payload['nonce'] = nonce
    payload['username'] = user.username
    payload['email'] = user.email
    payload['name'] = user.profile.name
    payload['external_id'] = user.id
    payloadurl_encoded = urlencode(payload)

    if settings.DISCOURSE_VALIDATE_EMAIL:
        payload['require_activation'] = True

    return base64.b64encode(payloadurl_encoded.encode()).decode()

def _get_redirect_url(sso):
    decoded_payload = base64.b64decode(sso)
    return parse_qs(decoded_payload.decode())['return_sso_url'][0]

@login_required
@never_cache
def auth(request):
    if request.user.is_active:
        correct =  _validate_sign(request.GET.get('sso'),request.GET.get('sig'))
        if correct:
            response_payload = _create_payload(request.GET.get('sso'), request.user)
            redirect_url = _get_redirect_url(request.GET.get('sso'))
            return redirect(f'{redirect_url}?sso={quote(response_payload)}&sig={_sign(response_payload)}')
    return HttpResponseForbidden()
