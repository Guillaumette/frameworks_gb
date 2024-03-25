from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from hw_6 import crud
from hw_6 import models
from hw_6 import schemas
from hw_6.database import SessionLocal, engine
from hw_6.models import User, Item, Order

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Получение экземпляра сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Маршруты для пользователей
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Маршруты для товаров
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Маршруты для заказов
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


def create_users():
    db = SessionLocal()
    try:
        users_data = [
            {"first_name": "Иван", "last_name": "Иванов", "email": "ivan@example.com", "password": "password123"},
            {"first_name": "Петр", "last_name": "Петров", "email": "petr@example.com", "password": "qwerty123"},
            {"first_name": "Мария", "last_name": "Сидорова", "email": "maria@example.com", "password": "abcdef"},
        ]
        for user_data in users_data:
            user = User(**user_data)
            db.add(user)
            print("Added user:", user_data)
        db.commit()
        print("Committed users")
    except Exception as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()


print("Creating users...")
create_users()


# Заполнение таблицы "Товары"
def create_items():
    db = SessionLocal()
    try:
        items_data = [
            {"title": "Ноутбук", "description": "Мощный ноутбук с процессором Intel Core i7", "price": 1500.00},
            {"title": "Смартфон", "description": "Современный смартфон с OLED-дисплеем", "price": 800.00},
            {"title": "Планшет", "description": "Легкий планшет с высоким разрешением экрана", "price": 400.00},
        ]
        for item_data in items_data:
            item = Item(**item_data)
            db.add(item)
            print("Added item:", item_data)
        db.commit()
        print("Committed items")
    except Exception as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()


create_items()


# Заполнение таблицы "Заказы"
def create_orders():
    db = SessionLocal()
    try:
        orders_data = [
            {"user_id": 1, "item_id": 1, "order_date": "2024-03-28", "status": "processed"},
            {"user_id": 2, "item_id": 2, "order_date": "2024-03-29", "status": "pending"},
            {"user_id": 3, "item_id": 3, "order_date": "2024-03-30", "status": "delivered"},
        ]
        for order_data in orders_data:
            order = Order(**order_data)
            db.add(order)
            print("Added order:", order_data)
        db.commit()
        print("Committed orders")
    except Exception as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()


create_orders()
