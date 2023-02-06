list = [["161E90", "Raman", 41, 56000], ["161E91", "Himadri", 38, 67500], ["161E99", "Jaya", 51, 82100], ["171E20", "Tejas", 30, 55000], ["171G30", "Ajay", 45, 44000]]

class Employee:
    def __init__(self, empId ,name ,age ,salary):
        self.empId = empId,
        self.name = name,
        self.age = age,
        self.salary = salary



my_objects = []
for i in range(len(list)):
    item = list[i]
    my_objects.append(Employee(item[0], item[1], item[2], item[3]))

def searchBy(type1, rel, value):
    count = 0
    for j in range(len(my_objects)):
        obj = my_objects[j]
        if type1 == "name" and obj.name[0] == value:
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
        elif type1 == "id" and obj.empId[0] == value:
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
        elif type1 == "age" and obj.age[0] == value:
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
        elif type1 == "salary" and rel == ">" and obj.salary > value:
            count = count + 1
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
        elif type1 == "salary" and rel == "<" and obj.salary < value:
            count = count + 1
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
        elif type1 == "salary" and rel == ">=" and obj.salary >= value:
            count = count + 1
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
        elif type1 == "salary" and rel == "<=" and obj.salary <= value:
            count = count + 1
            print("EmployeeId:", obj.empId[0], ", Name:", obj.name[0], ", Age:", obj.age[0], ", Salary:", obj.salary)
    print("Total Employee: ", count)





type2 = input("Search by id/name/age/salary:")
rel = ""
if type2 == "salary":
    rel = input("Search by >/</>=/<=:")
    value = int(input("Enter value:"))
else:
    value = input("Enter value:")
searchBy(type2, rel, value)








