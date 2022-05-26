class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print ("\u0332".join("NAME ")) #To underline a text in Python
        return self.name

    def change_age(self, new_age):
        val = isinstance(new_age, int) #checks if number is an integer
        if val == True:
            self.age = new_age
            print ("\u0332".join("AGE "))
            return self.age
        return "Invalid age"
        
    def add_track(self, new_track):
        track_set = self.tracks
        track_set.append(new_track)
        print ("\u0332".join("TRACKS "))
        return track_set
    
    def get_score(self):
        print ("\u0332".join("SCORE "))
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
print (Bob.change_name("Peter"))
print (Bob.change_age(34))
print (Bob.add_track("UI/UX"))
print (Bob.get_score())
