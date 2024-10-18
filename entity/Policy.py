# entity/Policy.py
class Policy:
    def __init__(self, policyId=None, policyName=None, policyDescription=None):
        self.__policyId = policyId
        self.__policyName = policyName
        self.__policyDescription = policyDescription

    def get_policyId(self):
        return self.__policyId
    
    def get_policyName(self):
        return self.__policyName
    
    def get_policyDescription(self):
        return self.__policyDescription

    def set_policyId(self, policyId):
        self.__policyId = policyId


    def set_policyName(self, policyName):
        self.__policyName = policyName

    
    def set_policyDescription(self, policyDescription):
        self.__policyDescription = policyDescription

    def __str__(self):
        return f"Policy (policyId={self.__policyId}, policyName={self.__policyName}, policyDescription={self.__policyDescription})"