class Aluno:
    def __init__(self, nome_aluno, email_aluno, cpf_aluno, matricula, periodo, situacao):
        self.__nome_aluno = nome_aluno
        self.__email_aluno = email_aluno
        self.__cpf_aluno = cpf_aluno
        self.__matricula = matricula
        self.__periodo = periodo
        self.__situacao = situacao

    def get_nome_aluno(self):
        return self.__nome_aluno

    def set_nome_aluno(self, nome_aluno):
        self.__nome_aluno = nome_aluno

    def get_email_aluno(self):
        return self.__email_aluno

    def set_email_aluno(self, email_aluno):
        self.__email_aluno = email_aluno

    def get_matricula(self):
        return self.__matricula

    def get_periodo(self):
        return self.__periodo

    def get_situacao(self):
        return self.__situacao

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def __str__(self):
        return f"Nome: {self.__nome_aluno}\n E-mail: {self.__email_aluno}\n Matricula: {self.__matricula}\n Situação: {self.get_situacao()}\n Periodo de ingresso: {self.get_periodo()}"
