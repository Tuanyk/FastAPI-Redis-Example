from fastapi import FastAPI
import aioredis
import hashlib
from func import detect_bad_words
from pydantic import BaseModel

app = FastAPI()
redis = aioredis.from_url('redis://localhost:6379', encoding='utf-8', decode_responses=True)

class DataItem(BaseModel):
    paragraph: str

class DataAPI(BaseModel):
    paragraph: str

@app.get("/items")
async def get_all_hashs():
    result = await redis.keys()
    return result

@app.get("/items/len")
async def get_number_of_items():
    result = len(await redis.keys())
    return result

#
# For testing purpose only
#
@app.get('/items/clearall')
async def clear_all_data():
    keys = await redis.keys()
    for key in keys:
        await redis.delete(key)
    return True
#
#
#


@app.get("/items/{item_hash}")
async def get_item_by_hash(item_hash: str):
    return await redis.get(item_hash)


@app.post("/items")
async def create_item(data: DataItem):
    paragraph = data.paragraph.lower()
    key = hashlib.md5(paragraph.encode()).hexdigest()
    await redis.set(key, paragraph)
    return key


@app.delete("/items/{item_hash}")
async def delete_item(item_hash: str):
    await redis.delete(item_hash)
    return True

# @app.post("/api")
# async def detect_bad_words_api(paragraph: str):
#     bad_words = []
#     keys = await redis.keys()
#     for key in keys:
#         bad_words.append(await redis.get(key))
#     return detect_bad_words(paragraph, bad_words)

@app.post("/api")
async def detect_bad_words_api(data: DataAPI):
    keys = await redis.keys()
    paragraph = data.paragraph.lower()
    for key in keys:
        value = await redis.get(key)
        if value in paragraph:
            return 1
    return 0


