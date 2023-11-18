#DAO - DATA ACESS OBJECT
from aluno_model import Aluno
import pymysql.cursors

class AlunoData:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost', user='root', password='', database='escola',
                                      cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conexao.cursor()
    def insert (self, aluno: Aluno):
        try:
            sql = "INSERT INTO alunos (matricula, nome, idade, curso, nota) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao Inserir: erro: {error}")
    def update(self, aluno: Aluno):
        try:
            sql = 'UPDATE alunos SET nome = %s, idade = %s, curso = %s, nota = %s WHERE matricula = %s'
            self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota, aluno.matricula))
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao tentar atualizar! Erro: {error}')
    def select(self):
        try:
            sql = 'SELECT * FROM alunos'
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f'Erro ao Listar! Erro: {error}')
    def delect(self, matricula: str):
        try:
            sql = 'DELETE FROM alunos WHERE matricula = %s'
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao deletar! Erro: {error}')



if __name__=='__main__':
    a=AlunoData()
    a.delect('7c56061a-b335-4f87-95b3-a3dcc9de3aeb')
    print(a.select())