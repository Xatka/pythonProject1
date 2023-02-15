#
# import uvicorn
# #from fastapi import FastAPI
# from fastapi import Query
# app = FastAPI()
# import redis
#
# # подключаемся к Redis из Python
# r = redis.Redis(host='localhost', port=6379, db=0)
#
#
# @app.post("/create")
# def create_publication(headline: str, content: str, author: str):
#     # генерируем id для нашей добавленной публикации
#     publication_id = r.incr("next_publication_id")
#     # сохраняем данные нашей созданной публикации в Redis
#     r.hmset(f"publication_id:{publication_id}", {"headline": headline, "content": content, "author": author})
#     return {"id": publication_id}
#
#
# @app.delete("/delete/{publication_id}")
# def delete_publication(publication_id: int):
#     # удаляем публикацию из Redis
#     r.delete(f"publication_id:{publication_id}")
#     return {"delete is success"}
#
#
# @app.put("/update/{publication_id}")
# def update_publication(publication_id: int, headline: str, content: str, author: str):
#     # обновляем данные публикации в Redis
#     r.getall(f"publication_id:{publication_id}", {"headline": headline, "content": content, "author": author})
#     return {"id": publication_id}
#
#
# @app.get("/view/{publication_id}")
# def view_publication(publication_id: int):
#     # получаем данные публикации из Redis
#     publication = r.hgetall(f"blog:post:{publication_id}")
#     return publication




# Тестовое задание №1
# Проверяем знания FastAPI + Redis
# Задание:
# Реализовать сервис блога.
# Требования к функционалу:
# - Ендпоинты для работы с блогом
# (/create, /update, /view, /delete)
# Требования к реализации:
# - данные хранить в Redis
# Минимальные требования к коду:
# - Код на github
# - Кодстайл по PEP



from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

import redis

# подключаемся к Redis из Python
r = redis.Redis(host='localhost', port=6379, db=0)

@app.post("/create")
def create_book(name: str = Query(min_length=1, max_length=100),
                content: str =Query(min_length=1)):
    # генерируем id для нашей книги
    book_id = r.incr("blog:next_post_id")
    # сохраняем данные книги в Redis
    r.hmset(f"name:content:{book_id}", {"name": name, "content": content})
    return {"id": book_id}


@app.put("/update/{book_id}")
def update_book(book_id: int, name: str = Query(min_length=1, max_length=100),
                content: str=Query(min_length=1)):
    # обновляем данные книги в Redis
    r.hmset(f"name:content:{book_id}", {"name": name, "content": content})
    return {"id": book_id}


@app.get("/view/{book_id}")
def view_book(book_id: int):
    # получаем данные книги из Redis
    post = r.hgetall(f"name:content:{book_id}")
    return post


@app.delete("/delete/{book_id}")
def delete_book(book_id: int):
    # удаляем книгу из Redis
    r.delete(f"name:content:{book_id}")
    return {"delete is success"}