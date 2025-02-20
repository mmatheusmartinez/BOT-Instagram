# **BOT Scraper de Seguidores do Instagram para Business Intelligence**

## **Descrição do Projeto**  

Este projeto foi desenvolvido para coletar e armazenar dados de seguidores de contas do Instagram utilizando a API disponibilizada pela plataforma **[RapidAPI](https://rapidapi.com/social-data-social-data-default/api/instagram-scraper-20252)**. O objetivo é obter informações estratégicas sobre os seguidores de empresas concorrentes para auxiliar em campanhas de marketing digital.  

## **Objetivo**  

O projeto tem como foco a **inteligência de negócios (Business Intelligence)**, utilizando dados coletados para analisar o perfil de seguidores de empresas concorrentes. Com essas informações, é possível segmentar campanhas de marketing, entender melhor o público-alvo e otimizar estratégias para aquisição de clientes.  

**Importante**: Este scraper **só capta seguidores de perfis públicos**.  

## **Tecnologias Utilizadas**  

- **Python**: Para requisições HTTP, processamento de dados e manipulação do banco de dados.  
- **Requests**: Biblioteca utilizada para realizar chamadas à API de scraping do Instagram.  
- **SQLite**: Banco de dados leve para armazenamento e análise dos seguidores capturados.  

## **Como Funciona**  

1. O script realiza uma requisição para a API de scraping disponível na **[RapidAPI](https://rapidapi.com/social-data-social-data-default/api/instagram-scraper-20252)**, fornecendo o nome de usuário da conta-alvo.  
2. A API retorna uma lista de seguidores contendo informações como:  
   - ID do usuário  
   - Nome de usuário  
   - Nome completo  
   - Conta pública ou privada  
   - Conta verificada ou não  
   - URL da foto de perfil  
3. Os dados coletados são armazenados em um banco de dados SQLite para análises futuras.  
4. Um segundo script permite visualizar e analisar os seguidores armazenados.  
