from sqlmodel import create_engine, SQLModel
import yaml

config = yaml.safe_load(open("./src/config/config.yaml"))
_user = config["database"]["username"]
_pass = config["database"]["password"]

# engine = create_engine(conn_str)
engine = create_engine(f"mysql+pymysql://{_user}:{_pass}@localhost:3306/workoutDb")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)