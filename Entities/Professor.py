class Professor:
    def __init__(self, nomeProf, email, cpfProf, codProf, codDepartamento):
        self._nomeProf = nomeProf
        self._email = email
        self._cpfProf = cpfProf
        self._codProf = codProf
        self._codDepartamento = codDepartamento

    def get_NomeProf(self):
        return self._nomeProf

    def set_NomeProf(self, nomeProf):
        self._nomeProf = nomeProf

    def get_EmailProf(self):
        return self._emailProf

    def set_EmailProf(self, emailProf):
        self._emailProf = emailProf

    def get_CodProfessor(self):
        return self._codProf

    def set_CodProfessor(self, codProf):
        self._codProf = codProf

    def get_CodDepartamentoProf(self):
        return self._codProfDepartamento

    def set_CodDepartamentoProf(self, codDepartamento):
        self._codDepartamento = codDepartamento

    def __str__(self):
        return f"Nome: {self._nomeProf}\n E-mail: {self._emailProf}\n Código: {self._codProf}\n "
