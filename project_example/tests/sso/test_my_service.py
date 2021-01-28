from sso.single_sign_on import SingleSignOnRegistry
from sso.sso_token import SSOToken
from sso.request import Request
from sso.my_service import MyService
from unittest.mock import Mock


# def test_hello_name(my_service: MyService):
def test_service_handler_requests_hello_name():
    stub_sso_registry = Mock(SingleSignOnRegistry)
    my_service = MyService(stub_sso_registry)

    actual = my_service.handle(Request("Vincent"), SSOToken())

    assert actual.text == "Hello Vincent"


def test_sso_registry_used_to_validate_the_token():
    spy_on_sso_registry = Mock(SingleSignOnRegistry)
    my_service = MyService(spy_on_sso_registry)
    token = SSOToken()

    my_service.handle(Request("Vincent"), token)

    spy_on_sso_registry.is_valid.assert_called_with(token)


def test_invalid_sso_should_get_please_sign_in_response():
    spy_on_sso_registry = Mock(SingleSignOnRegistry)
    spy_on_sso_registry.is_valid.return_value = False
    my_service = MyService(spy_on_sso_registry)
    token = SSOToken()

    actual_response = my_service.handle(Request("Vincent"), token)

    assert actual_response.text == "Please sign in"


def test_sso_receives_the_correct_token():
    mock_sso_registry = Mock(SingleSignOnRegistry)
    correct_token = SSOToken()
    mock_sso_registry.is_valid = Mock(side_effect=confirm_token(correct_token))
    my_service = MyService(mock_sso_registry)

    my_service.handle(Request("Vincent"), correct_token)

    mock_sso_registry.is_valid.assert_called()


def confirm_token(correct_token: SSOToken):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError("Wrong token received")

    return is_valid
