class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}"


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __str__(self):
        notas_str = ", ".join(map(str, self.notas))
        return f"Disciplina: {self.nome}, Notas: [{notas_str}], Média: {self.media():.2f}"


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.disciplinas = {}

    def adicionar_disciplina(self, nome_disciplina):
        if nome_disciplina not in self.disciplinas:
            self.disciplinas[nome_disciplina] = Disciplina(nome_disciplina)

    def adicionar_nota(self, nome_disciplina, nota):
        if nome_disciplina in self.disciplinas:
            self.disciplinas[nome_disciplina].adicionar_nota(nota)
        else:
            print(f"Disciplina '{nome_disciplina}' não encontrada para {self.nome}")

    def exibir_boletim(self):
        print(f"\nBoletim de {self.nome} (Matrícula: {self.matricula})")
        for disciplina in self.disciplinas.values():
            print(disciplina)


class GerenciadorAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"{aluno.nome} - Matrícula: {aluno.matricula}")

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None



if __name__ == "__main__":
    sistema = GerenciadorAlunos()

 
    aluno1 = Aluno("João", "2025001")
    aluno2 = Aluno("Maria", "2025002")

    sistema.adicionar_aluno(aluno1)
    sistema.adicionar_aluno(aluno2)

 
    aluno1.adicionar_disciplina("Matemática")
    aluno1.adicionar_disciplina("História")

    aluno2.adicionar_disciplina("Matemática")
    aluno2.adicionar_disciplina("Português")


    aluno1.adicionar_nota("Matemática", 8.0)
    aluno1.adicionar_nota("Matemática", 7.5)
    aluno1.adicionar_nota("História", 9.0)

    aluno2.adicionar_nota("Matemática", 6.5)
    aluno2.adicionar_nota("Português", 8.5)

   
    aluno1.exibir_boletim()
    aluno2.exibir_boletim()
