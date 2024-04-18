from Entities.Aluno import Aluno


class AlunosLista:
    def __init__(self):
        self._AlunosLista = []

    def buscar_aluno(self, matricula):
        for aluno in self._AlunosLista:
            if matricula == aluno.get_matricula():
                return aluno
        return False

    def matricular_aluno(self, aluno):
        self._AlunosLista.append(aluno)
        return f"O Aluno {aluno.get_nome_aluno()} foi matriculado com sucesso"

    def desmatricular_aluno(self, matricula):
        aluno: Aluno = self.buscar_aluno(matricula)
        if aluno:
            return f"O Aluno {aluno.get_nome_aluno()} foi removido da  com sucesso!"
        return f"Operação Invalida!\nNão foi encontrado aluno com o código {matricula}!"

    def alterar_aluno(self, matricula, nome_aluno, email_aluno, situacao):
        aluno: Aluno = self.buscar_aluno(matricula)
        if aluno:
            aluno.set_nome_aluno(nome_aluno)
            aluno.set_email_aluno(email_aluno)
            aluno.set_situacao(situacao)
            return f"Os  dados do Aluno de matricula {matricula} foram atualizado sucesso!\n{aluno.__str__()}"
        return f"Operação Invalida!\nNão foi encontrado aluno com o código {matricula}!"

    def consultar_aluno(self, matricula):
        aluno: Aluno = self.buscar_aluno(matricula)
        if aluno:
            return aluno.__str__()
        return f"Operação Invalida!\nNão foi encontrado aluno com o código {matricula}!"

    def __str__(self):
        for aluno in self._AlunosLista:
            return aluno.__str__()


alunos = AlunosLista()
