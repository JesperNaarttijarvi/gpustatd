
from singleton import Singleton

class Version(object):
  __metaclass__ = Singleton

  version = '1.1.4'

  def get(self):
    return self.version
