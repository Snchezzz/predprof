class studentiki:
    id = 0
    name = ''
    projekt_id = 0
    clas = ''
    score = 0

students = []
f = open('students.csv')
j = 0
scip = f.readline()
for i in f:
    s = i.split(',')
    if int(s[3][:-1]) == 10:
        students.append(studentiki())
        students[j].name = s[1]
        students[j].score = int(s[4])
        j += 1

for i in range(len(students)):
    j = i
    t = students[i]
    while j > 0 and students[j - 1].score > t.score:
        students[j] = students[j-1]
        j -= 1
    students[j] = t
print(f'''
10 класс:

1 место:{students[0].name[0]}.{students[0].name.split()[0]}

2 место:{students[1].name[0]}.{students[1].name.split()[0]}

3 место:{students[2].name[0]}.{students[2].name.split()[0]}''')
