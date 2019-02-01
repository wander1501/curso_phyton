alunos = [{"nome": "Rodrigo", "matricula": 1},
          {"nome": "João", "matricula": 2},
          {"nome": "André", "matricula":3}]

disciplinas = [{"nome": "Python 1", "professor": "prof 1", "id": 1, "dependencias": []},
               {"nome": "Python 2", "professor": "prof 2", "id": 2, "dependencias": [1, 3]},
               {"nome": "Estatística", "professor": "prof 3", "id": 3, "dependencias": [4]},
               {"nome": "Algebra", "professor": "prof 4", "id": 4, "dependencias": []},
               {"nome": "R", "professor": "prof 3", "id": 5, "dependencias": [1, 3]}]

turmas = [
         {"id_curso": 1, "lista_inscritos": [1, 3], "ano": 2019},
         {"id_curso": 3, "lista_inscritos": [2], "ano": 2018},
         {"id_curso": 2, "lista_inscritos": [2], "ano": 2019}]

alunos_python1 = None

for turma in turmas:
    for disciplina in disciplinas:
        if turma["id_curso"] == disciplina["id"]:
           if disciplina["nome"] == "Python 1":
              alunos_python1 = [aluno["nome"] for aluno in alunos if aluno["matricula"] in turma["lista_inscritos"]]
              break;
print(alunos_python1)
