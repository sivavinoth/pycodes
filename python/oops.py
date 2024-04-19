# class Object:
#   pass
# ob = Object()
# print(type(ob))


class PlayerCharcter:
    def __init__(self, name):
        self.nae = name



    def run(self):
     print('run')

    # @staticmethod
    def stat (name):
       return name

player1 =PlayerCharcter.stat('vino')
print(player1)



