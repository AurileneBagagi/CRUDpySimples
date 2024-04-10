class Aluno:
    def __init__(self, nomeAlunoAluno, emailAluno, cpfAluno, matricula, periodo, situacao):
        self._nomeAlunoAluno = nomeAlunoAluno
        self._emailAluno = emailAluno
        self._cpfAluno = cpfAluno
        self._matricula = matricula
        self._periodo = periodo
        self._situacao = situacao

    def get_NomeAluno(self):
        return self._nomeAluno

    def set_NomeAluno(self, nomeAluno):
        self._nomeAluno = nomeAluno

    def get_EmailAluno(self):
        return self._emailAluno

    def set_EmailAluno(self, emailAluno):
        self._emailAluno = emailAluno

    def get_matricula(self):
        return self._matricula

    def get_Periodo(self):
        return self._periodo

    def get_Situacao(self):
        return self._situacao

    def set_Situacao(self, situacao):
        self._situacao = situacao

    def __str__(self):
        return f"Nome: {self._nomeAluno}\n E-mail: {self._emailAluno}\n Matricula: {self._matricula}\n Situação: {self.get_Situacao()}\n Periodo de ingresso: {self.get_Periodo()}"
