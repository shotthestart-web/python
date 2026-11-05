class house:
    def __init__(self,name,area,room,construction ):
       self.name=name
       self.area=area
       self.room=room
       self.construction=construction
    def calling(self):
        print("House is",self.name,"area is",self.area,"room are",self.room,"costruction site is",self.construction)
mini=house("minialmist","500square feet",5,"started")
mini.calling()

class countries:
    hello="ayesha"
    def calling(self):
        print("my name is",self.hello)
    def __init__(self,name,capital, president,currency):
        self.name=name
        self.capital=capital
        self.president=president
        self.currency=currency
    def a (self):
     print ("country name is",self.name,"its president is",self.president,"its capital",self.capital,"and lastly its currency is",self.currency)
a = countries("pakistan","islamabad","shahbaz sharif","pkr")
a.a()
a.calling()

b = countries("america","california","donald trump","usd")
b.a()

