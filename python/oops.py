# class Object:
#   pass
# ob = Object()
# print(type(ob))

class PlayerCharcter:
    def __init__(self, name):
        self._name = name

    def run(self):
     print('run')

    def stat (self):
      print(f'my name is {self._name} ')
    
player1 =PlayerCharcter('vino')
# print(player1)

player1.stat = 'siva'
print(player1.stat)





    

