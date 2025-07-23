from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class TweetData(BaseModel):
    tweet_id: str
    timestamp: str
    text: str
    location: Optional[str]
    need_type: Optional[str]
    person_count: Optional[int]
    priority_score: Optional[str]

app = FastAPI()

@app.post("/ingest")
async def ingest_tweet(data: TweetData):
    # Burada veritabanına kaydetme veya queue'ya gönderme yapabilirsiniz.
    return {"status": "ok", "received": data.tweet_id}