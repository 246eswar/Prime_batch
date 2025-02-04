class job:
    def __init__(self):
        self.queue = []
        self.max_size = 5  # Maximum number of print jobs allowed in the queue

    def add(self, data):
        if len(self.queue) < self.max_size:
            self.queue.append(data)
            print("Added print job:", data)
        else:
            print("Queue is full. Cannot add more print jobs.")

    def process(self):
        if len(self.queue) == 0:
            print("No print jobs to process.")
        else:
            data = self.queue[0]
            print("Printing job:", data)
            self.queue.pop(0)

    def display(self):
        if len(self.queue) == 0:
            print("Current print queue is empty.")
        else:
            print("Current print queue:", self.queue)

jp = job()
a = ""
while a != "exit":
    a = input("Enter 'add' to add a print job, 'process' to print the next job, or 'exit': ")
    
    if a == "add":
        j = input("Enter print job name: ")
        jp.add(j)
        jp.display()
    
    if a == "process":
        jp.process()
        jp.display()
    
    if a == "exit":
        print("Exiting print queue system.")
