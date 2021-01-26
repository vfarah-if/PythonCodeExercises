from sso.single_sign_on import SingleSignOnRegistry
from sso.request import Request
from sso.sso_token import SSOToken
from sso.response import Response


class MyService():
    def __init__(self, sso_registry: SingleSignOnRegistry):
        self.sso_registry = sso_registry

    def handle(self, request: Request, ssoToken: SSOToken = None):
        result = Response("Hello {}".format(request.name)) if self.sso_registry.isValid(ssoToken) else Response("Please sign in")
        return result
