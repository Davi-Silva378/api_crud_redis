from repositories.data_repository import DataRepository

class DataService:
  def __init__(self, data_repository):
    self.data_repository = data_repository

  def get_data(self, key):
    if not key:
      raise ValueError('Key and value cannot be empty.')
    
    data = self.data_repository.get_data(key)

    if not data:
      raise ValueError(f'Data not found.')
    
    return data

  def set_data(self, key, value):
    if not key or not value:
      raise ValueError('Key and value cannot be empty.')
    
    if self.data_repository.get_data(key):
      raise ValueError('Data already exists.')
    
    self.data_repository.set_data(key, value)
    self.data_repository.redis_client.persist(key)

  def update_data(self, key, new_value):
    if not new_value:
      raise ValueError('Key and value cannot be empty.')
    
    if not self.data_repository.get_data(key):
      raise ValueError('Data not found.')
    
    self.data_repository.update_data(key, new_value)
    self.data_repository.redis_client.persist(key)

  def delete_data(self, key):
    if not key:
      raise ValueError('Key cannot be empty.')

    self.data_repository.delete_data(key)
