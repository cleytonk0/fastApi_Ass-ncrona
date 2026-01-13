import databases
import sqlalchemy as sa
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

database = databases.Database(DATABASE_URL)
# criação do metadata, que armazena informações sobre as tabelas
metadata = sa.MetaData()
# criação do engine para conectar ao banco de dados
engine = sa.create_engine(DATABASE_URL)
