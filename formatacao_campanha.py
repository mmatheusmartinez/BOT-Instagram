import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("instagram_followers.db")

# Consultar todos os dados da tabela 'followers'
query = "SELECT * FROM followers"
df = pd.read_sql_query(query, conn)

# Fechar a conexão com o banco de dados
conn.close()

# Exportar os dados para um arquivo Excel
df.to_excel("followers.xlsx", index=False)

print("Exportação concluída! O arquivo 'followers.xlsx' foi criado.")

