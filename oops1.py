class employee:
    def __init__(self):
        self.id = 123
        self.salary = 20000
        self.designation = "SDE"
        print("Attributes has been initialized")
    
    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination} ")


sam = employee()

sam.travel("Dhaka")