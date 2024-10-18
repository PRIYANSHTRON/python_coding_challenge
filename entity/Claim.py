class Claim:
    def __init__(self, claim_id=None, claim_number=None, date_filed=None, 
                 claim_amount=None, status=None, policy=None, client=None):

        self.__claim_id = claim_id
        self.__claim_number = claim_number
        self.__date_filed = date_filed
        self.__claim_amount = claim_amount
        self.__status = status
        self.__policy = policy
        self.__client = client

    # Getters
    def get_claim_id(self):
        return self.__claim_id

    def get_claim_number(self):
        return self.__claim_number

    def get_date_filed(self):
        return self.__date_filed

    def get_claim_amount(self):
        return self.__claim_amount

    def get_status(self):
        return self.__status

    def get_policy(self):
        return self.__policy

    def get_client(self):
        return self.__client

    # Setters
    def set_claim_id(self, claim_id):
        self.__claim_id = claim_id

    def set_claim_number(self, claim_number):
        self.__claim_number = claim_number

    def set_date_filed(self, date_filed):
        self.__date_filed = date_filed

    def set_claim_amount(self, claim_amount):
        self.__claim_amount = claim_amount

    def set_status(self, status):
        self.__status = status

    def set_policy(self, policy):
        self.__policy = policy

    def set_client(self, client):
        self.__client = client

    def __str__(self):
        return (f"Claim(claim_id={self.__claim_id}, claim_number='{self.__claim_number}', "
                f"date_filed='{self.__date_filed}', claim_amount={self.__claim_amount}, "
                f"status='{self.__status}', policy='{self.__policy}', client='{self.__client}')")

