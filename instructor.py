"""
Instructor class holds name of an instructor
get_name and to_string returns gives the name
"""
class Instructor:
    def __init__(self,name):
        self.name = name
    def get_name(self): return self.name
    def __str__(self) : return self.name