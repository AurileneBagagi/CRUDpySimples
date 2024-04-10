from Entities.Aluno import Aluno

class Alunos_Lista:
    def __init__(self):
        self._AlunosLista = []

    def buscar_aluno(self, matricula):
        for aluno in self._AlunosLista:
            if matricula == aluno.get_matricula():
                return aluno
        return False

    def matricular_alunoLista(self, aluno):
        self._AlunosLista.append(aluno)

    def desmatricular_aluno(self, matricula):
        aluno: Aluno = self.buscar_aluno(matricula)
        if aluno:
            return f"O Aluno {aluno.get_NomeAluno()} foi removido da  com sucesso!"
        else:
            return f"Operação Invalida!\nNão foi encontrado aluno com o código {matricula}!"

    def alterar_aluno(self, matricula, nomeAluno, emailAluno, situacao):
        aluno: Aluno = self.buscar_aluno(matricula)
        if aluno:
            aluno.set_NomeAluno(nomeAluno)
            aluno.set_EmailAluno(emailAluno)
            aluno.set_Situacao(situacao)
            return f"Os  dados do Aluno de matricula {matricula} foram atualizado sucesso!\n{aluno.__str__()}"

    def consultar_aluno(self, matricula):
        aluno: Aluno = self.buscar_aluno(matricula)
        if aluno:
            return aluno.__str__()

    def listarTodosAluno(self):
        for aluno in self._AlunosLista:
            return aluno.__str__()
