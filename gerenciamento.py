class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def print_valores(self):
        return f"Nome: {self.__nome}"


class Disciplina:
    def __init__(self, nome):
        self.__nome = nome
        self.__notas = []

    def get_nome(self):
        return self.__nome

    def get_notas(self):
        return self.__notas

    def print_valores(self):
        notas_str = ", ".join(map(str, self.__notas))
        return f"Disciplina: {self.__nome}, Notas: [{notas_str}], Média: {self.media():.2f}"

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

    def media(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.__matricula = matricula
        self.__disciplinas = {}

    def get_matricula(self):
        return self.__matricula

    def get_disciplinas(self):
        return self.__disciplinas

    def adicionar_disciplina(self, nome_disciplina):
        if nome_disciplina not in self.__disciplinas:
            self.__disciplinas[nome_disciplina] = Disciplina(nome_disciplina)
            print(f"- Adicionada a disciplina {nome_disciplina} ao aluno {self.get_nome()} -")
        print(f"!- O aluno {self.get_nome()} já cursa a disciplina {nome_disciplina} -!")

    def adicionar_nota(self, nome_disciplina, nota):
        if nome_disciplina in self.__disciplinas:
            self.__disciplinas[nome_disciplina].adicionar_nota(nota)
            print(f"- Adicionada a nota {nota} na disciplina {nome_disciplina} ao aluno {self.get_nome()} -")
        else:
            print(f"!- O aluno {self.get_nome()} não cursa a disciplina {nome_disciplina} -!")

    def exibir_boletim(self):
        print(f"\nBoletim de {self.get_nome()}")
        for disciplina in self.__disciplinas.values():
            print(disciplina.print_valores())


class Gerenciamento:
    def __init__(self):
        self.__alunos = []

    def get_alunos(self):
        return self.__alunos

    def adicionar_aluno(self, aluno):
        if not self.buscar_aluno(aluno.get_matricula()):
            self.__alunos.append(aluno)
            print(f"- Adicionado o aluno {aluno.get_nome()} de matrícula {aluno.get_matricula()} -")
        else:
            print(f"!- A matrícula {aluno.get_matricula()} já existe -!")

    def remover_aluno(self, matricula):
        aluno = self.buscar_aluno(matricula)

        if aluno:
            self.__alunos.remove(aluno)
            print(f"- Removido o aluno {aluno.get_nome()} de matrícula {aluno.get_matricula()} -")
        else:
            print(f"!- Não há aluno com a matrícula {matricula} -!")

    def buscar_aluno(self, matricula):
        for aluno in self.__alunos:
            if aluno.get_matricula() == matricula:
                return aluno
        return None

    def listar_alunos(self):
        for aluno in self.__alunos:
            print(f"{aluno.get_nome()} - Matrícula: {aluno.get_matricula()}")


# ---------- USO EXEMPLO ----------
if __name__ == "__main__":
    sistema = Gerenciamento()

    while True:
        print("1. Cadastrar Aluno")
        print("2. Remover Aluno")
        print("3. Adicionar Disciplina")
        print("4. Adicionar Nota")
        print("5. Ver Notas")
        print("6. Listar Alunos")
        print("7. Finalizar\n")
    
        # TODO completar as opções

        # aluno1.exibir_boletim()
        # aluno2.exibir_boletim()

        opcao = int(input("> "))
        print("")

        if opcao == 1:
            nome = input("Nome: ")
            matricula = input("Matricula: ")

            sistema.adicionar_aluno(Aluno(nome, matricula))
        elif opcao == 2:
            matricula = input("Matricula: ")

            sistema.remover_aluno(matricula)
        elif opcao == 3:
            matricula = input("Matricula: ")
            
            aluno = sistema.buscar_aluno(matricula)
            if not aluno:
                print(f"!- Não há aluno com a matrícula {matricula} -!")
                break

            disciplina = input("Disciplina: ")

            aluno.adicionar_disciplina(disciplina)
        elif opcao == 4:
            matricula = input("Matricula: ")
            
            aluno = sistema.buscar_aluno(matricula)
            if not aluno:
                print(f"!- Não há aluno com a matrícula {matricula} -!")
                break

            disciplina = input("Disciplina: ")

            if disciplina not in aluno.get_disciplinas():
                print(f"!- O aluno {aluno.get_nome()} não cursa a disciplina {disciplina} -!")
                break

            nota = input("Nota: ")

            if not nota.replace('.', '', 1).isdigit():
                print(f"!- A nota deve ser um valor numérico -!")

            aluno.adicionar_nota(disciplina, float(nota))
        elif opcao == 5:
            break # tirar
        elif opcao == 6:
            break # tirar
        elif opcao == 7:
            break
        else:
            print("!- Opção Inválida -!")
        
        print("\n")