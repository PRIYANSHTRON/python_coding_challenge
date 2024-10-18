class Client:
    def __init__(self, client_id=None, client_name=None, contact_info=None, policy=None):

        self.__client_id = client_id
        self.__client_name = client_name
        self.__contact_info = contact_info
        self.__policy = policy

    # Getters
    def get_client_id(self):
        return self.__client_id

    def get_client_name(self):
        return self.__client_name

    def get_contact_info(self):
        return self.__contact_info

    def get_policy(self):
        return self.__policy

    # Setters
    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def set_policy(self, policy):
        self.__policy = policy

    def __str__(self):
        return (f"Client(client_id={self.__client_id}, client_name='{self.__client_name}', "
                f"contact_info='{self.__contact_info}', policy='{self.__policy}')")


