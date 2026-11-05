class playlist:
    def calling():
        print("Hello there")
    def __init__(self,name,genre) :
        print("Ayesha class of object oriented programming oop part 2")
        self.name= name
        self.genre= genre
        self.song=[]
        print(f"playlist is",self.name,self.genre,"is ready")
    def add (self,song):
        self.song.append( song )
        print(f"{song}, is added to {self.name}")
    def remove (self,song ):
        if song in self.song:
            self.song.remove(song)
            print(f"{song}is removed")
        else:
            print(f"song is not there{song}")
    def display (self):
        print(f"{self.name}---{self.genre}")
        if self.song:
            for i ,song in enumerate(salf.song,1):
                print(f"{i},{song}")
            else:
                print("no song,add till yet")
    def __del__(self):
        print("playlist is deleted")

a= playlist("road the trip ","POP")
while True:
    