class User:
    """
    Empacota os dados do usuário, que vai ser utilizado na camada de repositório e serviço(autenticação).
    - Métodos: getters e setters.

    user_id: int = None, pois o objeto User pode não possuir um id, no contexto onde ele está sendo criado.
    - Como o setter age nessa situação? Como não tem validação no setter, ele irá aceitar um valor None.
    """

    def __init__(
        self,
        user_id: int = None,
        name: str = None,
        email: str = None,
        password_hash: str = None,
    ):
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

    @classmethod
    def constructor_dict(cls, dict):
        """
        Retorna uma instância da classe, sendo sua contrução abnstraída de um dicionário.
        """
        return cls(dict["id"], dict["name"], dict["email"], dict["password_hash"])
