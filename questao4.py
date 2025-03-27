import os
import logging
from dotenv import load_dotenv
import psycopg
from psycopg_pool import ConnectionPool

# Carrega as variáveis de ambiente do arquivo .env
# Caso seu arquivo esteja em UTF-8, altere o encoding para "utf-8".
load_dotenv(encoding="utf-8")

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabasePool:
    """
    Essa classe gerencia o pool de conexões usando psycopg3 e psycopg_pool.
    """
    def __init__(self, dsn, minconn=1, maxconn=10):
        if not dsn:
            raise ValueError("dsn não encontrado. Verifique seu .env ou variável de ambiente.")
        
        # Aqui usamos o DSN diretamente; se houver caracteres especiais, considere URL-encode.
        self.pool = ConnectionPool(conninfo=dsn, min_size=minconn, max_size=maxconn)
        logger.info("DSN utilizado: %s", dsn)
    
    def get_conn(self):
        """
        Retorna uma conexão do pool.
        """
        return self.pool.connection()

    def close_all(self):
        """
        Fecha todas as conexões do pool.
        """
        self.pool.close()

def process_logs(logs, db_pool):
    """
    Recebe uma lista de logs e insere todos no banco de dados de uma vez.
    
    :param logs: lista de dicionários contendo (timestamp, level, message).
    :param db_pool: instância de DatabasePool para obter conexões.
    """
    if not logs:
        logger.warning("Nenhum log recebido, nada a inserir.")
        return

    with db_pool.get_conn() as conn:
        with conn.cursor() as cursor:
            log_data = [
                (log["timestamp"], log["level"], log["message"])
                for log in logs
            ]
            query = "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)"
            cursor.executemany(query, log_data)
            conn.commit()
            logger.info("Inserimos %s logs de uma vez só.", len(log_data))

# Teste a resolução do hostname (opcional)
import socket
try:
    ip = socket.gethostbyname("pg-21858a36-demithehomie-3e1b.i.aivencloud.com")
    print("IP resolvido:", ip)
except Exception as e:
    print("Erro ao resolver o hostname:", e)

# Executa o código
dsn = os.getenv("DATABASE_URL")
if not dsn:
    raise ValueError("Variável DATABASE_URL não encontrada no .env")

db_pool = DatabasePool(dsn=dsn, minconn=2, maxconn=20)

sample_logs = [
    {"timestamp": "2025-02-24 10:00:00", "level": "INFO",  "message": "start process"},
    {"timestamp": "2025-02-24 10:00:05", "level": "ERROR", "message": "fail"},
    {"timestamp": "2025-02-24 10:00:10", "level": "INFO",  "message": "ending process"},
]

process_logs(sample_logs, db_pool)
db_pool.close_all()
