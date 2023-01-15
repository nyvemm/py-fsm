import os
from alembic.config import Config
from alembic import command
from dotenv import load_dotenv

load_dotenv()

alembic_cfg = Config("alembic.ini")
alembic_cfg.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))
command.upgrade(alembic_cfg, "head")
