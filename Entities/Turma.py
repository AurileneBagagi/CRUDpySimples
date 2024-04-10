class Turma:
    def __init__(self, codTurma, periodo):
        self._codTurma = codTurma
        self._periodo = periodo
        self._professores = []
        self._alunos = []

    def get_codTurma(self):
        return self._codTurma

    def set_codTurma(self, codTurma):
        self._codTurma = codTurma

    def get_periodo(self):
        return self._periodo

    def set_periodo(self, periodo):
        self._periodo = periodo

    def add_professor(self, professor):
        self._professores.append(professor)

    def add_aluno(self, aluno):
        self._alunos.append(aluno)

    def remove_professor(self, codProf):
        for professor in self._professores:
            if professor.get_CodProfessor() == codProf:
                self._professores.remove(professor)
                return f"O Professor {professor.get_NomeProf()} foi removido com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado professor com o código {codProf}!"

    def remove_aluno(self, codAluno):
        for aluno in self._alunos:
            if aluno.get_CodAluno() == aluno:
                self._alunos.remove(aluno)
                return f"O Aluno {aluno.get_NomeAluno()} foi removido com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado aluno com o código {codAluno}!"

    def listar_alunos(self):
        for aluno in self._alunos:
            return f"{aluno.get_NomeAluno()} | {aluno.get_matricula()} | {aluno.get_EmailAluno()}"

    def listar_professors(self):
        for professor in self._professores:
            return f"{professor.get_NomeProf()} | {professor.get_CodProfessor()} | {professor.get_EmailProf()}"
