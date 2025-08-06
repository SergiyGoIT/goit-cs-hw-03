from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import pprint

# Завантажуємо змінні середовища з файлу .env
load_dotenv()

# Отримуємо URI для MongoDB
MONGO_URI = os.getenv("MONGO_URI")

# Підключення до бази даних
client = MongoClient(MONGO_URI)
db = client["cat_db"]
cats = db["cats"]


# ---------- CREATE ----------
def insert_cat(name, age, features):
    result = cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })
    print(f"Inserted cat with _id: {result.inserted_id}")


# ---------- READ ----------
def get_all_cats():
    print("All cats:")
    for cat in cats.find():
        pprint.pprint(cat)


def get_cat_by_name(name):
    cat = cats.find_one({"name": name})
    if cat:
        pprint.pprint(cat)
    else:
        print("Cat not found")


# ---------- UPDATE ----------
def update_cat_age(name, new_age):
    result = cats.update_one({"name": name}, {"$set": {"age": new_age}})
    print(f"Updated {result.modified_count} document(s)")


def add_feature(name, new_feature):
    result = cats.update_one({"name": name}, {"$push": {"features": new_feature}})
    print(f"Added feature to {result.modified_count} cat(s)")


# ---------- DELETE ----------
def delete_cat_by_name(name):
    result = cats.delete_one({"name": name})
    print(f"Deleted {result.deleted_count} cat(s)")


def delete_all_cats():
    result = cats.delete_many({})
    print(f"Deleted {result.deleted_count} cats")


# ---------- MAIN ----------
if __name__ == "__main__":
    # Розкоментуй функції для тесту:
    
    insert_cat("Barsik", 3, ["руде хутро", "любить капці"])
    get_cat_by_name("Barsik")
    update_cat_age("Barsik", 4)
    add_feature("Barsik", "спить на ноутбуці")
    get_all_cats()
    delete_cat_by_name("Barsik")
    delete_all_cats()
    pass
