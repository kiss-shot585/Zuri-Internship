class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        #initializing attributes
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        #pass
    
    def change_name(self, new_name):
            #to change the student's name
            self.new_name = new_name
            print(f"Student's name is now {self.new_name}")
            
    def change_age(self, new_age):
                #to change the student's age
                self.new_age = new_age
                print(f"student's name is now {self.new_age}")
                
    def add_track(self, new_tracks):
                    #add a new track
                    self.new_tracks = new_tracks
                    print(f"new track added is {self.new_tracks}")
                    
    def get_score(self):
                        #to get score
                        print(f"Student's score is {self.score}")
                   
           
            



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
