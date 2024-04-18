import DataCRUD.ProfessoresLista
import DataCRUD.DisciplinasLista
from Entities.Professor import Professor


class Disciplina:

    def __init__(self, nome_disciplina, cod_disciplina, cod_departamento):
        self.__nome_disciplina = nome_disciplina
        self.__cod_disciplina = cod_disciplina
        self.__cod_departamento = cod_departamento
        self.__cod_professores = []

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

    def get_cod_professores(self):
        for professor in self.__cod_professores:
            return DataCRUD.ProfessoresLista.professores.consultar_professor(professor)

    def add_prof_disciplina(self, cod_prof):
        professor: Professor = DataCRUD.ProfessoresLista.professores.buscar_professor(cod_prof)
        if professor:
            self.__cod_professores.append(cod_prof)
            return f"O Professor {professor.get_nome_prof()} foi adicionado a disciplina com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado nenhum professor com o código {cod_prof} vinculado!"

    def remover_prof_disciplina(self, cod_prof):
        professor: Professor = DataCRUD.ProfessoresLista.professores.buscar_professor(cod_prof)
        if professor:
            self.__cod_professores.remove(cod_prof)
            return f"O Professor {professor.get_nome_prof()} foi adicionado a disciplina com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado nenhum professor com o código {cod_prof} vinculado!"
