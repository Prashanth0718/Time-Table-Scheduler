# Open a file in read mode ('r')
sections = []
courses = []
file_path = 'Sections.txt'
with open(file_path, 'r') as file:
    # Read the entire file
    for line in file:
        l = line.split()
        sections.append(l[0])
        temp = []
        temp.append(l[1])

    for i in temp:
        cor = i.split(",")
       
    for i in cor:
        courses.append(i)

# print(sections)
# print(courses)

print("*"*100)

faculty = []
faculty_pref = {}
dummy_val =[]

file_path = "Faculty.txt"
with open(file_path,'r') as file:
    temp = []

    for line in file:
        l = line.split()
        faculty.append(l[0])
        temp.append(l[1])
        dummy_val.append(l[2])


    count = 0
    for l in temp:
        faculty_pref[faculty[count]] = ((l.split(",")))
        count+=1



print(faculty)
print(faculty_pref)
# print(dummy_val)

print("*"*100)

slots = {}

file_path = 'Course.txt'
with open(file_path,'r') as file:
    temp = []
    for line in file:
        l = line.split()    
        temp.append(l[1])

    count=0
    for i in temp:
        slots[courses[count]] = int(i)
        count += 1

# print(slots)      

