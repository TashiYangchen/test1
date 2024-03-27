for number in range(1, 10):
    if number == 3: 
         print(f"Skipping {number} in the inner loop")
         continue # skip number 3 in the inner loop
    elif number == 7: 
         print(f"Reached {number}, breakng outer loop")
         break # Exit the inner loop (optinal)
    else:
         print(number)
        