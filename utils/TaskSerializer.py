import json
from utils.Task import Task

class TaskSerializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Task):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)