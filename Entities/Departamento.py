class Departamento:
    def __init__(self, nome_departamento: str, cod_departamento: str):
        self.__nome_departamento: str = nome_departamento
        self.__cod_departamento: str = cod_departamento

    def get_nome_departamento(self):
        return self.__nome_departamento

    def set_nome_departamento(self, nome_departamento: str):
        self.__nome_departamento = nome_departamento

    def get_cod_departamento(self):
        return self.__cod_departamento

    def set_cod_departamento(self, cod_departamento: str):
        self.__cod_departamento = cod_departamento


