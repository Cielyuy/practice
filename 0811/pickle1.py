import json
d = dict(name = 'huihui',age = 20)
a = json.dumps(d)
print(a)
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }
