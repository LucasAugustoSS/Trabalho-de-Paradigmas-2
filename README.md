
# 🎓 Trabalho de Paradigmas - Gerenciamento de Notas em Python (POO)

Este projeto foi desenvolvido como parte do trabalho da disciplina **Paradigmas de Linguagens de Programação (CC05MA/CC05NA)** do curso de Ciência da Computação do CESUPA.  
O objetivo é demonstrar a aplicação do **paradigma orientado a objetos** por meio de um sistema simples de gerenciamento de notas de alunos.

## 📌 Objetivo

Desenvolver um sistema em Python, utilizando os princípios da Programação Orientada a Objetos (POO), que permita:
- Cadastrar alunos
- Atribuir disciplinas
- Inserir notas
- Calcular médias
- Exibir boletins

## 🧠 Paradigma Escolhido

O paradigma utilizado foi o **orientado a objetos**, por sua modularidade, organização e reutilização de código.  
Conceitos aplicados:
- **Classes e Objetos**
- **Herança**
- **Encapsulamento**
- **Polimorfismo (simples)**

## 🧱 Estrutura das Classes

- `Pessoa`: Classe base com atributo `nome`
- `Aluno`: Subclasse de `Pessoa`, com `matrícula` e `disciplinas`
- `Disciplina`: Armazena notas e calcula a média
- `GerenciadorAlunos`: Controla o CRUD dos alunos

## 🖥️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- Paradigma Orientado a Objetos (OOP)

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucasAugustoSS/Trabalho-de-Paradigmas-2.git
   cd Trabalho-de-Paradigmas-2


2. Execute o programa:

   ```bash
   python main.py
   ```

## 📷 Exemplo de Saída

```
Boletim de João (Matrícula: 2025001)
Disciplina: Matemática, Notas: [8.0, 7.5], Média: 7.75
Disciplina: História, Notas: [9.0], Média: 9.00

Boletim de Maria (Matrícula: 2025002)
Disciplina: Matemática, Notas: [6.5], Média: 6.50
Disciplina: Português, Notas: [8.5], Média: 8.50
```

## 👨‍💻 Integrantes

* Thiago Rosa da Silva
* João Dário Pamplona Arruda
* Lucas Augusto Souza da Silva

## 📚 Licença

Este projeto é apenas para fins educacionais.

```


