from sqlmodel import create_engine, SQLModel, Session
from helpers.config_helper import get_config
import yaml

# config = yaml.safe_load(open("./src/config/config.yaml"))
config = get_config()

_user = config["database"]["username"]
_pass = config["database"]["password"]


# engine = create_engine(conn_str)
engine = create_engine(f"mysql+pymysql://{_user}:{_pass}@localhost:3306/workoutDb")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_sqlmodel_session():
    with Session(engine) as db:
        yield db