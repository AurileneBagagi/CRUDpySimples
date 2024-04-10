class Disciplina:
    def __init__(self, nomeDisciplina, codDisciplima):
        self.nomeDisciplina = nomeDisciplina
        self.codDisciplima = codDisciplima

    def get_Nome(self):
        return self.nomeDisciplina

    def set_Nome(self, nomeDisciplina):
        self.nomeDisciplina = nomeDisciplina

    def get_CodDisciplima(self):
        return self.codDisciplima

    def set_CodDisciplima(self, codDisciplima):
        self.codDisciplima = codDisciplima