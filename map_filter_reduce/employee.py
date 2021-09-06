#print employee names only:
employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
# for employee in employees:
#     print(employee['e_name'])
e_names=list(map(lambda employee: employee['e_name'],employees))
print(e_names)
#print employee names in upper case: case 1
# for employee in employees:
#     print(employee['e_name'].upper())
e_names_upper=list(map(lambda employee: employee['e_name'].upper(),employees))
print(e_names_upper)
#print employee name in development: case 2
# for employee in employees:
#     if employee['department']=='developer':
#         print(employee['e_name'])
# developers=list(filter(lambda emp:emp['department']=='developer',employees))
# print(developers)
developers_name=list(map(lambda developer:developer['e_name'],list(filter(lambda emp:emp['department']=='developer',employees))))
print(developers_name)

#total of salaries: case 3
total=0
for employee in employees:
    total+=employee['salary']
print(total)
# salaries=list(map(lambda emp:emp['salary'],employees))
# print(salaries)
# print(sum(salaries))
salaries=sum(list(map(lambda emp:emp['salary'],employees)))
print(salaries)
#find maximum salary:
salaries=list(map(lambda emp:emp['salary'],employees))
print(max(salaries))
#find lowest salary
print(min(salaries))
#case 1 map
#case 2 filter
#case 3 reduce
#not built in need to import from functools

from functools import reduce

