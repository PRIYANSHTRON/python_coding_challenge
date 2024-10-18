class User:
    def __init__(self, user_id=None, username=None, password=None, role=None):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__role = role

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    # Setters
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_role(self, role):
        self.__role = role

    def __str__(self):
        return (f"User(user_id={self.__user_id}, username='{self.__username}', "
                f"password='{self.__password}', role='{self.__role}')")
    

