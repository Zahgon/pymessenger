import hashlib
import hmac
import six


def validate_hub_signature(app_secret, request_payload, hub_signature_header):
    """
        @inputs:
            app_secret: Secret Key for application
            request_payload: request body
            hub_signature_header: X-Hub-Signature header sent with request
        @outputs:
            boolean indicated that hub signature is validated
    """
    pass


def generate_appsecret_proof(access_token, app_secret):
    """
        @inputs:
            access_token: page access token
            app_secret_token: app secret key
        @outputs:
            appsecret_proof: HMAC-SHA256 hash of page access token
                using app_secret as the key
    """
    pass
