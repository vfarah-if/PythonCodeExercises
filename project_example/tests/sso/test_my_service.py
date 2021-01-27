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

    spyOnSSORegistry.is_valid.assert_called_with(token)

def test_invalid_sso_should_get_pleaase_sign_in_response():
    spyOnSSORegistry = Mock(SingleSignOnRegistry)
    spyOnSSORegistry.is_valid.return_value = False
    myService = MyService(spyOnSSORegistry)
    token = SSOToken()
    
    actualResponse = myService.handle(Request("Vincent"), token)

    assert actualResponse.text == "Please sign in"

def test_sso_receives_the_correct_token():
    mockSSORegistry = Mock(SingleSignOnRegistry)
    correctToken = SSOToken();
    mockSSORegistry.is_valid = Mock(side_effect=confirmToken(correctToken))
    myService= MyService(mockSSORegistry)

    myService.handle(Request("Vincent"), correctToken)

    mockSSORegistry.is_valid.assert_called()


def confirmToken(correctToken: SSOToken):
    def is_valid(actualToken):
         if actualToken != correctToken:
            raise ValueError("Wrong token received")
    return is_valid