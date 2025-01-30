#Class with in a class
#object is created then only memory is allocated
'''Task Schedular
design a class TaskScheduler to schedule and manage tasks.
Each task has a unique ID, a description,and a priority.
Implement the following:
add_task(task_id,description,priority):Adds a task to the scheduler.
remove_task(task_id):Removes a task by ID.
get_next_task():Retrives and removes the task with the
highest priority(lower number indicates higher priority).
list_tasks():Lists all tasks sorted by priority'''
#__repr__  -->private constructor

class Task:#id,description,priority (3 attributes)
    def __init__ (self,task_id,des,priority):#default constructor
        self.task_id=task_id
        self.des=des
        self.priority=priority
        #take a method for representation
    def __repr__(self):#it is a constructor but it not default
        return f"Task({self.task_id},{self.des},{self.priority})"
class TaskScheduler:
    def __init__ (self):
        self.tasks=[]
    def add_task(self,task_id,des,priority):
        self.tasks.append(Task(task_id,des,priority))
        #Based on tasks we append
        #include the three arguments
        return f"Task{task_id} added"
    def remove_task(self,task_id):
        #remove is done with condition base
        #i.e., itteration forloop
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return f"Task{task_id} removed"
            else:
                return f"Task{task_id} not found"
    #priority based sorting
    def get_next_task(self):
        if not self.tasks:
            return "No tasks available"
        #pop is default remove last element
        self.tasks.sort(key=lambda t:t.priority)
        next_task=self.tasks.pop(0)
        #lowest number has highest priority given so pop(0)
        return f"Next task: {next_task}"
    def list_tasks(self):
        if not self.tasks:
            return "No tasks available"
        #pop is default remove last element
        self.tasks.sort(key=lambda t:t.priority)
        return [repr(task) for task in self.tasks]
    #task ia argument it is itteratable
scheduler=TaskScheduler()
print(scheduler.list_tasks())
print(scheduler.add_task(1,"HomeWork",2))
print(scheduler.add_task(2,"Preparation",3))
print(scheduler.add_task(3,"Presentation",4))
print(scheduler.add_task(4,"Visit doctor",1))
print(scheduler.list_tasks())
print(scheduler.get_next_task())
print(scheduler.list_tasks())
      
