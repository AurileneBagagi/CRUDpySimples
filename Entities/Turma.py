from io import StringIO


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

    def add_professor(self, cod_prof):
        self.__cod_professores.append(cod_prof)

    def add_aluno(self, aluno):
        self.__alunos.append(aluno)

    def remove_prof_turma(self, cod_prof):
        for professor in self.__professores:
            if professor.get_cod_prof() == cod_prof:
                self.__professores.remove(professor)
                return f"O Professor {professor.get_nome_prof()} foi removido da turma com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado nesta turma um professor com o código {cod_prof}!"

    def remove_aluno_turma(self, matricula):
        for aluno in self.__alunos:
            if aluno.get_matricula() == aluno:
                self.__alunos.remove(aluno)
                return f"O Aluno {aluno.get_nome_aluno()} foi removido da turma com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado nesta turma um aluno com o código {matricula}!"

    def ata_turma(self):
        ata = StringIO()
        ata.write("{} Dados da Turma {}".format(("=" * 21), ("=" * 21)))

        ata.write("{}\nNome do Professor | Código | E-mail".format(("-" * 81)))
        for professor in self.__professores:
            ata.write(f"{professor.get_NomeProf()} | {professor.get_CodProfessor()} | {professor.get_EmailProf()}")

        ata.write("{}\nNome do Aluno | Matricula | E-mail".format(("-" * 81)))
        for aluno in self.__alunos:
            ata.write(f"{aluno.get_nome_aluno()} | {aluno.get_matricula()} | {aluno.get_email_aluno()}")
        return ata
