from sso.single_sign_on import SingleSignOnRegistry
from sso.sso_token import SSOToken
from sso.request import Request
from sso.my_service import MyService
from unittest.mock import Mock

# def test_hello_name(myService: MyService):
def test_service_handler_requests_hello_name():
    stubSSORegistry = Mock(SingleSignOnRegistry)
    myService = MyService(stubSSORegistry)
    
    actual = myService.handle(Request("Vincent"), SSOToken())
    
    assert actual.text == "Hello Vincent"


def test_sso_registry_used_to_validate_the_token():
    spyOnSSORegistry = Mock(SingleSignOnRegistry)
    myService = MyService(spyOnSSORegistry)
    token = SSOToken()
    
    myService.handle(Request("Vincent"), token)

    spyOnSSORegistry.isValid.assert_called_with(token)

def test_invalid_sso_should_get_pleaase_sign_in_response():
    spyOnSSORegistry = Mock(SingleSignOnRegistry)
    spyOnSSORegistry.isValid.return_value = False
    myService = MyService(spyOnSSORegistry)
    token = SSOToken()
    
    actualResponse = myService.handle(Request("Vincent"), token)

    assert actualResponse.text == "Please sign in"

