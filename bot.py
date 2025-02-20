import requests
import sqlite3

url = "https://instagram-scraper-20252.p.rapidapi.com/v1/followers" #url da API

querystring = {"username_or_id_or_url":"liguemedicina"} # definindo conta (usuario, id ou url)

headers = {
	"x-rapidapi-key": "SUAAPI", #minha api
	"x-rapidapi-host": "instagram-scraper-20252.p.rapidapi.com" # codigo do host 
}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())

## Transformando em dataframe
response_json = response.json()

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("instagram_followers.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS followers (
    id TEXT PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    is_private BOOLEAN,
    is_verified BOOLEAN,
    latest_story_ts INTEGER,
    profile_pic_url TEXT
)
''')
followers = response_json["data"]["items"]
for follower in followers:
    cursor.execute('''
    INSERT OR IGNORE INTO followers (id, username, full_name, is_private, is_verified, latest_story_ts, profile_pic_url)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        follower["id"],
        follower["username"],
        follower["full_name"],
        follower["is_private"],
        follower["is_verified"],
        follower["latest_story_ts"],
        follower["profile_pic_url"]
    ))

# Salvar e fechar conexão
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("instagram_followers.db")
cursor = conn.cursor()

# Buscar todos os seguidores
cursor.execute("SELECT * FROM followers")
followers = cursor.fetchall()

# Exibir os dados
for f in followers:
    print(f)

# Fechar conexão
conn.close()
