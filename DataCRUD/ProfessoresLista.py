from Entities.Professor import Professor


class ProfessoresLista:
    def __init__(self):
        self.professores = []

    def buscar_professor(self, cod_prof):
        for professor in self.professores:
            if professor.get_cod_prof() == cod_prof:
                return professor
        return False

    def vincular_professor(self, professor):
        self.professores.append(professor)
        return f"O professor {professor.get_nome_prof()} foi vinculado com sucesso!"

    def desvincular_professor(self, cod_prof: int):
        professor: Professor = self.buscar_professor(cod_prof)
        if Professor:
            self.professores.remove(Professor)
            return f"O Professor {professor.get_nome_prof()} foi desvinculado com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado nenhum professor com o código {cod_prof} vinculado!"

    def atualizar_professor(self, cod_prof: int, nome_prof, email_prof, cod_departamento):
        professor: Professor = self.buscar_professor(cod_prof)
        if Professor:
            professor.set_nome_prof(nome_prof)
            professor.set_email_prof(email_prof)
            professor.set_cod_departamento_prof(cod_departamento)
            return f"Os  dados do Professor de código {cod_prof} foram atualizado sucesso!\n{professor.__str__()}"
        return f"Operação Invalida!\nNão foi encontrado nenhum professor com o código {cod_prof} vinculado!"

    def consultar_professor(self, cod_prof):
        professor: Professor = self.buscar_professor(cod_prof)
        if Professor:
            return professor.__str__()
        else:
            return f"Operação Invalida!\nNão foi encontrado nenhum professor com o código {cod_prof} vinculado!"

    def __str__(self):
        for professor in self.professores:
            return professor.__str__()


professores = ProfessoresLista()
