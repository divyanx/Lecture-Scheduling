
class Instructor:
"""
Instructor class holds name of an instructor
get_name and to_string returns gives the name

"""
    def __init__(self,name):
        self._name = name
    def get_name(self): return self.name
    def __str__(self) : return self.name


class ClassRoom:
    def __init__(self, number, capacity):
        self._number = number
        self._capacity = capacity
    def get_number(self): return self._number
    def get_capacity(self) : return self._capacity

class Lecture :
    def __inti__(self,id,branch,course):
        self._id = id
        self._branch = branch
        self._course = course
        self._instructor = None
        self._timing = None
        self.room = None
    def get_id(self) : return self._id
    def get_branch(self) : return self._branch
    def get_course(self) : return self._course
    def get_instructor(self) : return self._instructor
    def get_timing(self): return self._timing
    def get_room(self): return self._room
    def set_instructor(self,instructor) : self._instructor = instructor
    def set_timing(self,timing) : self._timing = timing
    def set_room(self, room): self._room = room
   
        
