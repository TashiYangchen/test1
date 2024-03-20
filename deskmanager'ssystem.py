from queue import Queue

# initiate patient queue
patient_name = Queue()
current_patient_name = None

# menu-driven program for desktop manager
while True:
    print("Desk Manager - Patient Registration and Appointment System")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    task = int(input("Enter your choice (just enter the option number): "))
    if task == 1:
        name = input("Enter Patient Name: ")
        patient_name.put(name)
        current_patient_name = name
        print(f"Patient {name} registered")

    elif task == 2:
        if not patient_name.empty():
            removed_patient = patient_name.get()
            print(f"Patient {removed_patient} removed after meeting the doctor")
        else:
            print("No patient in the queue")
            
    elif task == 3:
        print("Current Patient Queue: ")
        print(list(patient_name.queue))
        
    elif task == 4:
        print("Exiting program...")
        break
        
    else:
        print("Invalid Input")