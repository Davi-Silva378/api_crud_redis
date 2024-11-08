from config import get_connection

class DataRepository:
  def __init__(self):
    self.redis_client = get_connection()

  def get_data(self, key):
    data = self.redis_client.get(key)
    if data is not None:
      return data.decode('utf-8')
    return None
  
  def set_data(self, key, value):
    self.redis_client.set(key, value)

  def update_data(self, key, new_value):
    self.redis_client.set(key, new_value) 

  def delete_data(self, key):
    self.redis_client.delete(key)

      
