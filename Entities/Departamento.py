class Departamento:
    def __init__(self, nomeDepartamento, codDepartamento):
        self.nomeDepartamento = nomeDepartamento
        self.codDepartamento = codDepartamento

    def get_nomeDepartamento(self):
        return self.nomeDepartamento

    def set_nomeDepartamento(self, nomeDepartamento):
        self.nomeDepartamento = nomeDepartamento

    def get_codDepartamento(self):
        return self.codDepartamento

    def set_codDepartamento(self, codDepartamento):
        self.codDepartamento = codDepartamento


class ListaDeDepartamentos:
    def __init__(self):
        self.departamentos = []

    def add_departamento(self, departamento):
        self.departamentos.append(departamento)

    def remove_departamento(self, codDepartamento):
        for departamento in self.departamentos:
            if departamento.get_codDepartamento() == codDepartamento:
                self.departamentos.remove(departamento)
                return f"o Departamento {departamento.get_nomeDepartamento()} foi removido com sucesso!"
        return f"Operação Invalida!\nO Departamento {departamento.get_nomeDepartamento()} não foi encontrado!"