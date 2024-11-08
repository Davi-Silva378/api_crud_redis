from service.data_service import DataService

class DataController:
  def __init__(self, data_service):
    self.data_service = data_service

  def get_data(self, key):
    return self.data_service.get_data(key)

  def set_data(self, key, value):
    return self.data_service.set_data(key, value)
  
  def update_data(self, key, new_value):
    return self.data_service.update_data(key, new_value)
  
  def delete_data(self, key):
    return self.data_service.delete_data(key)

  