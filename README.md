 
# Setup Redis Container

Pull redis image:

`docker pull redis`

Run command below:

`docker run --name rds -d -p 6379:6379 -p 8000:8000 -v "$(pwd)"/redis_data:/data redis redis-server /data/redis.conf`


Port 8000 is for fastapi to run

Port 6379 is default port of redis

Custom redis.conf file => is in the redis_data folder


# Run FastApi

Run command:

`uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

# Calculate Function Complexity

```
async def detect_bad_words_api(data: DataAPI):
    keys = await redis.keys()           => 1
    paragraph = data.paragraph.lower()  => 2
    for key in keys:                    => 3
        value = await redis.get(key)    => 4
        if value in paragraph:          => 5
            return 1                    => 6
    return 0                            => 7
```

Big O = O(C) + O(C) + O(N^2) + O(C) = O(N^2)
