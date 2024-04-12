from DataCRUD.ProfessoresLista import ProfessorLista
from Entities.Professor import Professor


class Disciplina:
    def __init__(self, nome_disciplina, cod_disciplina, cod_departamento):
        self.__nome_disciplina = nome_disciplina
        self.__cod_disciplina = cod_disciplina
        self.__cod_departamento = cod_departamento
        self.__professores = []

    def get_nome_disciplina(self):
        return self.__nome_disciplina

    def set_nome_disciplina(self, nome_disciplina):
        self.__nome_disciplina = nome_disciplina

    def get_cod_disciplina(self):
        return self.__cod_disciplina

    def set_cod_disciplina(self, cod_disciplina):
        self.__cod_disciplina = cod_disciplina

    def get_cod_departamento(self):
        return self.__cod_departamento

    def set_cod_departamento(self, cod_departamento):
        self.__cod_departamento = cod_departamento



