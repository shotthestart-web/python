class circket:
    def __init__(self, player, score, background):
        self.__player=player
        self.__score=score
        self.__background=background
    def info(self):
        print(f"Circket  - player{self.__player} - score :{self.__score}and background")
    def play (self):
        print(f"{self.__player}hit a six !")
    def get_score (self):
        return self.__score;
    def set_score (self, new_score):
        if new_score>=0:
            self.__score= new_score;
            print(f"Score update to {self.__score}")        
        else:
            print("Score can't be nagtive")
class football:
    def __init__(self, player, score, background):
        self.__player=player
        self.__score=score
        self.__background=background
    def info(self):
        print(f"Circket  - player{self.__player} - score :{self.__score}and background")
    def play (self):
        print(f"{self.__player}hit a six !")
    def get_score (self):
        return self.__score;
    def set_score (self, new_score):
        if new_score>=0:
            self.__score= new_score;
            print(f"Score update to {self.__score}")        
        else:
            print("Score can't be nagtive")

circket= circket ("baber azam ", 34 ,"azam khan")
circket.play()
circket.info()

football= football("ronald",89,"ronald famliy")
football.info()
football.play()

print("Encapasulation")
circket.__score=99
print(f"get_score() stil shows{circket.get_score()}")

print("setter")
circket.set_score(100)
football.set_score(88)