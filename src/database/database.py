import sqlalchemy as sa
import databases

from src.config.settings import settings

# Cria o objeto database (para FastAPI assíncrono)
database = databases.Database(settings.database_url)

# Cria o metadata (usado pelos models)
metadata = sa.MetaData()

# Define o engine do SQLAlchemy
if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})
