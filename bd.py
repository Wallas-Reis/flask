import psycopg2

# Configuração da conexão com o banco de dados
url = "postgres://wisecoin_user:gT06xyldPRImhVYLO62zl4C1DuKIta0I@dpg-cko2l3e1101c73da4tq0-a.oregon-postgres.render.com/wisecoin"

# Exemplo de consulta
def select(query):
    # Conectar ao banco de dados
    connection = psycopg2.connect(url)

    # Criar um cursor
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    # Fechar o cursor e a conexão
    cursor.close()
    connection.close()

    return result


