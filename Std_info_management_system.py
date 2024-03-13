# Initialize empty lists and dictionary
students_list = []
students_dict = {}
while True: 
    name = input ("Enter student's name (or type 'done' to finish): ")
    if name.lower() == 'done' :
        break
    age = int(input("Enter student's age: "))
    grade = int(input("Enter student's grade: "))

    # Add student information to the dictionary
    students_dict[name] = {'age': age, 'grade': grade}
    students_list.append(name)
print ("\nStudent Details: ")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']} ")

search_name = input("\nEnter Student's name to search: ")
if search_name in students_dict: 
    print("\nStudent Found!")
    print(f"Name: {search_name}, Age: {students_dict[search_name]['age']}, Grade{students_dict[search_name]['grade']}")
else:
    print ("\nStudent not found.")

remove_name = input('Enter the name of the student you want to remove or simply enter to skip : ')
if remove_name in students_list: 
    students_list.remove(remove_name)
    del students_dict[remove_name]
    print("Student removed successfully!")
else:
    print("Student not found!")
     