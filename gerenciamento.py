class Pessoa:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def print_valores(self):
        print(f"Nome: {self.__nome} | Matrícula: {self.__matricula}")


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.__disciplinas = {}

    def get_disciplinas(self):
        return self.__disciplinas

    def adicionar_disciplina(self, disciplina):
        self.__disciplinas[disciplina] = []

    def adicionar_nota(self, disciplina, nota):
        if nota >= 0 and nota <= 10:
            self.__disciplinas[disciplina].append(nota)
            print(f"\n- Adicionada a nota {nota} na disciplina {disciplina.get_nome()} ao aluno {self.get_nome()} -")
        else:
            print("\n!- A nota deve estar entre 0 e 10 -!")

    def boletim(self):
        if not self.__disciplinas:
            print(f"\n!- {self.get_nome()} não está matriculado em nenhuma matéria -!")
        else:
            print(f"\nBoletim de {self.get_nome()}")
            for disciplina in self.__disciplinas:
                notas = self.__disciplinas[disciplina]
                media = sum(notas) / len(notas) if notas else 0
                print(f"Disciplina: {disciplina.get_nome()} | Notas: {", ".join(map(str, self.__disciplinas[disciplina]))} | Média: {media}")


class Professor(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.__disciplinas = []

    def get_disciplinas(self):
        return self.__disciplinas

    def adicionar_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def get_alunos(self):
        for disciplina in self.__disciplinas:
            print(f"- {disciplina.get_nome()} -")
            for aluno in disciplina.get_alunos():
                print(f"{aluno.get_nome()}")
            print()

    def print_valores(self):
        print(f"Nome: {self.get_nome()} | Matrícula: {self.get_matricula()} | Disciplinas: {", ".join(disciplina.get_nome() for disciplina in self.__disciplinas)}")


class Disciplina:
    def __init__(self, nome, professor):
        self.__nome = nome
        self.__professor = professor
        self.__alunos = []

    def get_nome(self):
        return self.__nome

    def get_professor(self):
        return self.__professor

    def get_alunos(self):
        return self.__alunos

    def adicionar_aluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)
            aluno.adicionar_disciplina(self)
            print(f"\n- Aluno {aluno.get_nome()} matriculado à disciplina {self.__nome} -")
        else:
            print(f"\n!- {self.get_nome()} já cursa a disciplina -!")
    
    def print_alunos(self):
        for aluno in self.__alunos:
            print(aluno.get_nome())

    def print_valores(self):
        print(f"Nome: {self.__nome} | Professor: {self.__professor.get_nome()} | Alunos: {", ".join(aluno.get_nome() for aluno in self.__alunos)}")


class Sistema:
    def __init__(self):
        self.__alunos = []
        self.__professores = []
        self.__disciplinas = []

    def get_alunos(self):
        return self.__alunos

    def get_professores(self):
        return self.__professores

    def get_disciplinas(self):
        return self.__disciplinas

    def buscar_aluno(self, matricula):
        for aluno in self.__alunos:
            if aluno.get_matricula() == matricula:
                return aluno
        return None

    def buscar_professor(self, matricula):
        for professor in self.__professores:
            if professor.get_matricula() == matricula:
                return professor
        return None

    def buscar_disciplina(self, nome):
        for disciplina in self.__disciplinas:
            if disciplina.get_nome() == nome:
                return disciplina
        return None

    def adicionar_aluno(self, aluno):
        if not self.buscar_aluno(aluno.get_matricula()):
            self.__alunos.append(aluno)
            print(f"\n- Adicionado o aluno {aluno.get_nome()} de matrícula {aluno.get_matricula()} -")
        else:
            print(f"\n!- A matrícula {aluno.get_matricula()} já existe -!")

    def adicionar_professor(self, professor):
        if not self.buscar_professor(professor.get_matricula()):
            self.__professores.append(professor)
            print(f"\n- Adicionado o professor {professor.get_nome()} de matrícula {professor.get_matricula()} -")
        else:
            print(f"\n!- A matrícula {professor.get_matricula()} já existe -!")

    def adicionar_disciplina(self, nome):
        if not self.buscar_disciplina(nome):
            matricula_professor = input("Matrícula do Professor: ")
            if not self.buscar_professor(matricula_professor):
                print(f"\n!- Não há professor de matrícula {matricula_professor} -!")
            else:
                professor = self.buscar_professor(matricula_professor)
                disciplina = Disciplina(nome, professor)
                self.__disciplinas.append(disciplina)
                professor.adicionar_disciplina(disciplina)
                print(f"\n- Adicionada a disciplina {nome} com o professor {professor.get_nome()} -")
        else:
            print(f"\n!- A disciplina {nome} já existe -!")

    def listar(self):
        if not self.__alunos and not self.__professores and not self.__disciplinas:
            print("!- Não há nada cadastrado -!")
        else:
            if self.__alunos:
                print("- Alunos -")
                for aluno in self.__alunos:
                    aluno.print_valores()
                print()
            
            if self.__professores:
                print("- Professores -")
                for professor in self.__professores:
                    professor.print_valores()
                print()

            if self.__disciplinas:
                print("- Disciplinas -")
                for disciplina in self.__disciplinas:
                    disciplina.print_valores()
                print()


if __name__ == "__main__":
    sistema = Sistema()

    while True:
        print("1. Cadastrar aluno")
        print("2. Cadastrar professor")
        print("3. Cadastrar disciplina")
        print("4. Matricular aluno em matéria")
        print("5. Adicionar nota a aluno")
        print("6. Exibir boletim de aluno")
        print("7. Listar alunos de professor")
        print("8. Listar alunos, professores e disciplinas")
        print("9. Finalizar\n")

        opcao = int(input("> "))
        print("")

        if opcao == 1:
            nome = input("Nome: ")
            matricula = input("Matricula: ")

            sistema.adicionar_aluno(Aluno(nome, matricula))

        elif opcao == 2:
            nome = input("Nome: ")
            matricula = input("Matricula: ")

            sistema.adicionar_professor(Professor(nome, matricula))
            
        elif opcao == 3:
            if not sistema.get_professores():
                print("!- Não há professores cadastrados; cada disciplina deve ter um professor -!")
            else:
                nome = input("Nome: ")

                sistema.adicionar_disciplina(nome)

        elif opcao == 4:
            if not sistema.get_alunos():
                print("!- Não há alunos cadastrados -!")
            elif not sistema.get_disciplinas():
                print("!- Não há disciplinas cadastradas -!")
            else:
                matricula_aluno = input("Matrícula do aluno: ")
                nome_disciplina = input("Nome da disciplina: ")

                aluno = sistema.buscar_aluno(matricula_aluno)
                disciplina = sistema.buscar_disciplina(nome_disciplina)

                disciplina.adicionar_aluno(aluno)

        elif opcao == 5:
            if not sistema.get_alunos():
                print("!- Não há alunos cadastrados -!")
            elif not sistema.get_disciplinas():
                print("!- Não há disciplinas cadastradas -!")
            else:
                matricula = input("Matricula: ")
                    
                aluno = sistema.buscar_aluno(matricula)
                if not aluno:
                    print(f"\n!- Não há aluno com a matrícula {matricula} -!")
                else:
                    nome_disciplina = input("Disciplina: ")

                    disciplina = sistema.buscar_disciplina(nome_disciplina)

                    if disciplina not in aluno.get_disciplinas():
                        print(f"\n!- O aluno {aluno.get_nome()} não cursa a disciplina {disciplina} -!")
                    else:
                        nota = input("Nota: ")

                        if not nota.replace('.', '', 1).isdigit():
                            print(f"\n!- A nota deve ser um valor numérico -!")
                        else:
                            aluno.adicionar_nota(disciplina, float(nota))

        elif opcao == 6:
            if not sistema.get_alunos():
                print("!- Não há alunos cadastrados -!")
            elif not sistema.get_disciplinas():
                print("!- Não há disciplinas cadastradas -!")
            else:
                matricula = input("Matricula: ")

                aluno = sistema.buscar_aluno(matricula)
                if not aluno:
                    print(f"\n!- Não há aluno com a matrícula {matricula} -!")
                else:
                    aluno.boletim()

        elif opcao == 7:
            if not sistema.get_professores():
                print("!- Não há professores cadastrados -!")
            elif not sistema.get_alunos():
                print("!- Não há alunos cadastrados -!")
            else:
                matricula = input("Matricula do professor: ")

                professor = sistema.buscar_professor(matricula)
                if not professor:
                    print(f"\n!- Não há professor com a matrícula {matricula} -!")
                else:
                    professor.get_alunos()

        elif opcao == 8:
            sistema.listar()

        elif opcao == 9:
            break

        else:
            print("\n!- Opção inválida -!")
        
        print("\n")