import redis

def get_connection():
  try:
    return redis.Redis(host='localhost', port=6379, db=0)
  except Exception as e:
    raise ValueError(f'Cannot connect with Redis database: {str(e)}')