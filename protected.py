


class Protected:
    def __init__(self):
      self._protectedVar = 0
      self.__privateVar = 12

    def getPrivate(self):
      print(self.__privateVar)
      self._protectedVar = 0

    def setPrivate(self, private):
      self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(24)
obj.getPrivate()
obj._protectedVar = 34
print(obj._protectedVar)
