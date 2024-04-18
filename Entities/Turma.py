import DataCRUD.ProfessoresLista
import DataCRUD.AlunosLista
from Entities.Professor import Professor


class Turma:
    def __init__(self, cod_turma, periodo, disciplina):
        self.__cod_turma = cod_turma
        self.__periodo = periodo
        self.__cod_disciplina = disciplina
        self.__cod_professores = []
        self.__cod_alunos = []

    def get_cod_turma(self):
        return self.__cod_turma

    def set_cod_turma(self, cod_turma):
        self.__cod_turma = cod_turma

    def get_periodo(self):
        return self.__periodo

    def set_periodo(self, periodo):
        self.__periodo = periodo

    def add_prof_turma(self, cod_prof):
        professor: Professor = DataCRUD.ProfessoresLista.professores.buscar_professor(cod_prof)
        if professor:
            self.__cod_professores.append(cod_prof)
            return f"O Professor {professor.get_nome_prof()} foi adicionado a disciplina com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado nenhum professor com o código {cod_prof} vinculado!"

    def remove_prof_turma(self, cod_prof):
