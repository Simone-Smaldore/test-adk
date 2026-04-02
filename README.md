Comandi per creazione di db e utente:
- docker exec -it devcontainer-db-1 psql -U postgres -d postgres (Apre una shell nel container devcontainer-db-1 con utente postgres db postgres)
- CREATE DATABASE adk_db; (Crea il db adk_db)
- CREATE USER myuser WITH PASSWORD 'mypassword'; (Crea lo user)
- GRANT ALL PRIVILEGES ON DATABASE adk_db TO myuser; (Da tutti i privilegi per il db allo user)
- \c adk_db (Cambia connessione al db adk_db)
- GRANT ALL ON SCHEMA public TO myuser; (Da tutti i permessi allo schema public per lo user)
- \q (Esce dal terminale psql)