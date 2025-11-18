class User:
    """
        Empacota os dados do usuário, que vai ser utilizado na camada de repositório e serviço(autenticação).
        - Métodos: getters e setters.
    """
    def __init__(self, user_id: int, name: str, email: str, password_hash: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = password_hash

    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id):
        # validation ? acho que não pois a camada de autenticação será responsável por garantir a validade do usuário
        self.__user_id = user_id
    
    @property
    def password_hash(self):
        return self.__password_hash
    
    @password_hash.setter
    def password_hash(self, password_hash):
        self.__password_hash = password_hash