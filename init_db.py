from models.base import Base
from config import engine

# Создаём все таблицы
Base.metadata.create_all(bind=engine)

print("✅ Таблицы успешно созданы!")

