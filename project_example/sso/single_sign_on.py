# REMARKS: Intentionally left empty to mock
class SingleSignOnRegistry:
    def __init__(self):
        pass
    
    def registerNewSession(self, credentials):
        """Returns an instance of an SSOToken if the credentials are valid"""
        pass

    def isValid(self, token):
        """Returns True if the token refers to a current session"""
        pass
