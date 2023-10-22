from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import config

# 使用pymysql作为MySQL的驱动
DATABASE_URL = config.DATABASE_URL.replace("mysql://", "mysql+pymysql://")

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建一个SessionLocal类，该类的每个实例都是一个数据库会话。
# 您可以使用这个类来创建和管理您的数据库会话。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个Base类，该类是所有模型类的基类。
# 您可以使用这个类来定义您的模型。
Base = declarative_base()
