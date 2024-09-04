import initialise
import tts
# import temp

# schedule_dict = tts.schedule

schedules = tts.schedules

file_path = "SectionTT.txt"

file = open(file_path,'a')

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sections = ['SEC-01',"SEC-02"]

file.write("Section\t")

for i in days_of_week:
    for j in range(1,9):
        if j!=12:
            file.write(i+str(j)+"\t")
        

file.write("\n")

end_time = 16

i=0
for schedule in schedules:
    file.write(sections[i]+"\t")
    for j in schedule.keys():
        curr_time = 8
        for k in schedule[j]:
            # file.write(str(k))

            if curr_time<int(k[2]):
                # if curr_time!=12:
                while(True):
                    if curr_time!=12:
                        file.write("\t")
                    curr_time+=1
                    if str(curr_time)==k[2]:
                        break


            if curr_time==int(k[2]):
                file.write(str(k[0])+" ("+str(k[1])+")\t")
                curr_time+=1
            
        if curr_time<end_time:
            while (True):
                file.write("\t")
                if curr_time==end_time:
                    break
                curr_time+=1
    i+=1
    file.write("\n")


#Faculty TT

file_path = "FacultyTT.txt"

file = open(file_path,'a')

fac = {}

print(schedules)
print('------------------------------\n')
# for i in initialise.faculty:
#     for j in schedules:
#         day=0
#         file.write(str(j[day]))
#         break
# file.write(str(schedules[0][0]))
day=0
curr_time=8
# file.write('------------------------------\n')

for y in range(8,17):
    if y!=12:
        fac[y] = []

for j in schedules:
    for k in j:
        for t in j[k]:
            fac[int(t[2])].append([f'{(schedules.index(j))+1}',t[0],t[1],k])



 

# print("asdasdasfasdqjhbdkqkjdbaksjb")
print(fac)


file.write('Faculty\t')
for i in days_of_week:
    for j in range(1,9):
        if j!=12:
            file.write(i+str(j)+"\t")
file.write('\n')

ftt = {}

for i in initialise.faculty:
    ftt[i] = []
    # file.write(i+'\t')
    for d in range(0,5):
        for j in fac.keys():
            temp = fac[j]
            # file.write(str(j))
            curr_time=8
            for k in temp:
                # file.write(str(k))
                if k[1]==i and d==k[3]:
                    # file.write(f'SEC-0{k[0]} ({k[2]})\t')
                    ftt[i].append([f'SEC-0{k[0]} ({k[2]})',d,j])
                    curr_time+=1 

    # file.write('\n')

print("*"*10)
print(ftt)

# file.write("------------------------------\n")
curr_time=8
for i in initialise.faculty:
    file.write(i+'\t')
    
    curr_time=8
    prev_day=0
    for k in ftt[i]:
        
        if prev_day<k[1]:
            if curr_time<end_time:
                while (True):
                    if curr_time!=12:
                        file.write("\t")
                    curr_time+=1
                    if curr_time==end_time:
                        file.write('\t')
                        break
        
        if k[1]>prev_day:
            curr_time=8

        if curr_time<k[2]:
            while(True):
                if curr_time!=12:
                    file.write("\t")
                curr_time+=1
                if curr_time==k[2]:
                    break
        

        if curr_time==k[2]:
            file.write(k[0]+'\t')
            curr_time+=1

        # if k[1]>prev_day:
        #     curr_time=8

        prev_day = k[1]

    # if curr_time<end_time:
    #     while (True):
    #         if curr_time!=12:
    #             file.write("\t")
    #         curr_time+=1
    #         if curr_time==end_time:
    #             break

    file.write('\n')

