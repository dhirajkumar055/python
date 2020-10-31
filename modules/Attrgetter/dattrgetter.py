from operator import attrgetter

class Employees:
    def __init__(self,name,eid):
        self.name=name
        self.employee_id=eid
    
    def __repr__(self):
        return self.name+" : "+self.employee_id

    
emp=[Employees("Sahil","25"),Employees("Sanyam","223"),Employees("Divyesh","50"),Employees("Ishaan","75"),Employees("Dheeraj","100")]

for employee in emp:
    print(employee)

print("-----------")

for user in sorted(emp,key=attrgetter('name')):
    print(user)

print("-----------")

for eid in sorted(emp,key=attrgetter('employee_id')):
    print(eid)