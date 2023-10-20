import pyodbc

# Defina os detalhes da conexão
server = 'seu_servidor'  # Endereço do servidor PostgreSQL
database = 'seu_banco_de_dados'  # Nome do banco de dados
username = 'seu_usuario'  # Nome de usuário
password = 'sua_senha'  # Senha

# Crie uma string de conexão
connection_string = f'DRIVER={{PostgreSQL}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Estabeleça a conexão
conn = pyodbc.connect(connection_string)

# Crie um cursor para executar consultas SQL
cursor = conn.cursor()

# Exemplo de SELECT
cursor.execute('SELECT * FROM sua_tabela')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Exemplo de INSERT
novo_valor1 = 'Novo Valor 1'
novo_valor2 = 'Novo Valor 2'
cursor.execute("INSERT INTO sua_tabela (coluna1, coluna2) VALUES (?, ?)", novo_valor1, novo_valor2)
conn.commit()  # Confirme a transação

# Exemplo de UPDATE
novo_valor = 'Novo Valor Atualizado'
valor_condicao = 'Valor de Condição'
cursor.execute("UPDATE sua_tabela SET coluna1 = ? WHERE coluna2 = ?", novo_valor, valor_condicao)
conn.commit()  # Confirme a transação

# Exemplo de DELETE
valor_condicao = 'Valor a ser excluído'
cursor.execute("DELETE FROM sua_tabela WHERE coluna = ?", valor_condicao)
conn.commit()  # Confirme a transação

# Feche o cursor e a conexão quando terminar
cursor.close()
conn.close()
