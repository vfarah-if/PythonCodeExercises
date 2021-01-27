# REMARKS: Intentionally left empty to mock
class SingleSignOnRegistry:
    def __init__(self):
        pass
    
    def register_new_session(self, credentials):
        """Returns an instance of an SSOToken if the credentials are valid"""
        pass

    def is_valid(self, token):
        """Returns True if the token refers to a current session"""
        pass
