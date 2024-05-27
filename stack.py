from queue import LifoQueue

# Initialize history stacks and current page variable
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# Input the number of URLs to visit
NO_of_visits = int(input("Enter the number of URL history: "))

# Visit URLs
print("Enter URLs to visit: ")
for i in range(NO_of_visits):
    url = input("URL: ")
    if current_page is not None:
        backward_history.put(current_page)
    print(f"Visiting {url}")
    current_page = url

print(f'Current page: {current_page}')

# Go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")

# Go forward
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")
