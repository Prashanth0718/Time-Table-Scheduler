import initialise
import random
import numpy as np

def generate_schedule(faculties, courses, prefered_courses):

    section = 1

    schedules = []

    for _ in range(2):  # Generate two schedules
        schedule = {}
        time = 800  # Starting time: 8:00 AM
        end_time = 1700  # Ending time: 5:00 PM

        for day in range(5):  # Iterate for 5 days
            schedule[day] = []
            available_faculties = faculties.copy()
            current_time = time
            prev_faculty = None

            random.shuffle(courses)

            assigned_courses = set()  # To keep track of assigned courses for the day
            assigned_faculties = {}  # To keep track of assigned faculties and their class times
            # assigned_faculties[current_time // 100] = []
            gaps = []
            n_gaps = np.arange(8, 17)
            for _ in range(9):
                n = random.choice(n_gaps)
                if n not in gaps:
                    gaps.append(n)
                if len(gaps) == 3:
                    break

            while current_time < end_time:
                if not available_faculties or len(assigned_courses) == len(courses):
                    break

                faculty = random.choice(available_faculties)

                f_courses = prefered_courses[faculty]

                for course in f_courses:
                    if course not in assigned_courses:
                        break

                if len([item for item in schedule[day] if item[0] == faculty]) >= 2:
                    available_faculties.remove(faculty)
                    continue

                # Check if the faculty is already assigned for this time in the other section
                # print("2324")
                if section>1:
                    s1 = schedules[0][day]
                    temp = None
                    # print(s1)
                    for i in s1:
                        # print(i)
                        # print("Curr",current_time//100)
                        if i[2]==str(current_time//100):
                            temp=i
                            break


                    if temp!=None and faculty==temp[0]:
                        # if len(available_faculties)!=1:
                        available_faculties.remove(faculty)
                        while(True):
                            f = random.choice(faculties)  
                            if f!=faculty:
                                available_faculties.append(f)
                                break
                        continue
                            # faculty = random.choice(available_faculties)

                if faculty == prev_faculty:
                    available_faculties.remove(faculty)
                    while(True):
                        f = random.choice(faculties)  
                        if f!=faculty:
                            available_faculties.append(f)
                            break
                    continue

                schedule[day].append([faculty, course, f"{current_time // 100}"])
                current_time += 100

                # print([faculty, course, f"{current_time // 100}"])

                if current_time // 100 in gaps:
                    current_time += 100


                assigned_courses.add(course)
                assigned_faculties[current_time // 100] = [faculty,section]
                prev_faculty = faculty
                available_faculties.append(faculty)

                #lunch
                if current_time == 1200:
                    current_time += 100
            
            # print("Schedule",schedule)

            time = 800
            current_time = time

        schedules.append(schedule)
        section +=1
    return schedules

def main():
    faculties = initialise.faculty
    courses = initialise.courses
    pref_courses = initialise.faculty_pref

    global schedules
    schedules = generate_schedule(faculties, courses, pref_courses)

    for idx, schedule in enumerate(schedules, start=1):
        print(f"Schedule {idx}:")
        for day, classes in schedule.items():
            print("\nDay", day + 1)
            for faculty, course, class_time in classes:
                print(f"{class_time} - {faculty}: {course}")

    # print(schedules)
    # return schedules

main()
