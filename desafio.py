import sqlite3

conexao = sqlite3.connect('Desafio')
cursor = conexao.cursor()

## Questão 1
cursor.execute('CREATE TABLE alunos (id INT, nome VARCAHR(100), idade INT, curso VARCHAR(100));')

## Questão 2
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Jullia", 19, "Eng Comp")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Julia", 19, "Eng Comp")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Anna Laura", 20, "Eng Comp")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Lucas", 21, "Eng Comp")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Mariana", 20, "Eng Comp")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Leticia", 19, "Eng Comp")')


## Questão 3
## Letra A
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)

## Letra B
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20 ')
print('ALunos com idade maior que 20 anos')
for aluno in dados:
    print(aluno)   

## Letra C
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Eng Comp" ORDER BY nome ')
print()
for aluno in dados:
    print(aluno)

## Letra D
cursor.execute('SELECT COUNT(1) FROM alunos')
count = cursor.fetchone()
print('A quantidade de pessoas na tabela é de: ',count[0])


# ## Questão 4
# ## Letra A
# cursor.execute('UPDATE alunos SET idade = 20 WHERE nome = "Julia"')

# ## Letra B
# cursor.execute('DELETE FROM alunos WHERE id = 6')

# ## Questão 5
# cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1, "Jullia", 19, 3000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2, "Jake", 22, 5000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3, "James", 20, 4000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4, "Manu", 20, 2000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5, "Charlie", 20, 4000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(6, "Gisely", 46, 1000000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(7, "Alessandro",47 , 200000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(8, "Liz", 20, 60000000.00)')
# cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(9, "Josh", 52, 4000000.00)')




# ## Questão 6
# ## Letra A
# print()
# dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
# for cliente in dados:
#     print(cliente)

# ## Letra B
# print()
# dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
# print('A média de saldo dos clientes é de: ',dados.fetchone()[0])

# ## Letra C
# cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
# nome_cliente, saldo_cliente = cursor.fetchone()
# print(f'O cliente {nome_cliente} possui o maior saldo sendo de {saldo_cliente} ')

# ## Letra D
# cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
# resultado = cursor.fetchone()
# print(f'A quantidade de clientes com saldo maior que 1000 é de: {resultado[0]}')

## Questão 7
## Letra A
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (10, "Fernando", 14, 2000.00)')
# cursor.execute('UPDATE clientes SET saldo = 5000.00 WHERE nome = "Jullia"')

## Letra B
# cursor.execute('DELETE FROM clientes WHERE id = 5')

## Questão 8
# cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT);')

# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Celular", 3000.00)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 1, "Notebook", 4000.00)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 6, "Celular", 5000.00)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 7, "Carro", 100000.00)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 10, "PC Gamer", 5000.00)')

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for dado in dados:
    print(dado)



conexao.commit()
conexao.close()