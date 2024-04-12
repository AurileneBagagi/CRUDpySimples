class Professor:
    def __init__(self, nome_prof, email_prof, cpf_prof, cod_prof, cod_departamento):
        self.__nome_prof = nome_prof
        self.__email_prof = email_prof
        self.__cpf_prof = cpf_prof
        self.__cod_prof = cod_prof
        self.__cod_departamento = cod_departamento

    def get_nome_prof(self):
        return self.__nome_prof

    def set_nome_prof(self, nome_prof):
        self.__nome_prof = nome_prof

    def get_email_prof(self):
        return self.__email_prof

    def set_email_prof(self, email_prof):
        self.__email_prof = email_prof

    def get_cod_prof(self):
        return self.__cod_prof

    def set_cod_prof(self, cod_prof):
        self.__cod_prof = cod_prof

    def get_cod_departamento_prof(self):
        return self.__cod_departamento

    def set_cod_departamento_prof(self, cod_departamento):
        self.__cod_departamento = cod_departamento

    def __str__(self):
        return f"Nome: {self.__nome_prof}\n E-mail: {self.__email_prof}\n Código: {self.__cod_prof}\n "
