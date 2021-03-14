from employee import Employee, Manager

e1 = Manager(10, "ritesh")
e2 = Manager(2, "Navneet")

a = [e1,e2]

a.sort()
print(a[0].id)
print(a[1].id)

   