class Task:
    """main class for tasks, 
    takes care of all of the
    functionalities of the task
    """
    def __init__(self, date, priority, contains):
        """all the basic components for the task"""
        self.done = False
        self.date = date
        self.contains = contains
        self.priority = priority
    
    def read_task(self):
        """read tasks from file"""
        pass
    def write_task(self):
        """write task to file"""
        pass
    def show_task(self):
        pass
if __name__ == "main":
    pass
