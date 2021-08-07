import socket
from fastapi import FastAPI
import sys


app = FastAPI()

hostname = socket.gethostname()


version = f"{sys.version_info.major}.{sys.version_info.minor}"

books = {}


@app.get("/")
async def read_root():
	return {
		"name": "my-app",
		"host": hostname,
		"version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}",
	}


@app.get("/")
def root():
	return {"detail": "hello"}


@app.get("/books")
def getBooks():
	return books


@app.get("/books/{bookId}")
def getBook(bookId: str):
	if bookId not in books:
		return {"detail": f'Book "{bookId}" not found.'}, 404
	return books[bookId]


@app.post("/books")
def addBook():
	return {"detail": "Book not added"}
	return {"detail": "Book added"}


@app.delete("/books/{bookId}")
def deleteBook(bookId: str):
	if bookId not in books:
		return {"detail": f'Book "{bookId}" not found.'}, 404
	del books[bookId]

	return {"detail": "Success"}
