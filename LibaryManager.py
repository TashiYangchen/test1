# Intilialize emmty lists, set and dictionary
books_list = []
authors_set = set()
books_dict = {}
# Add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Sturctures and Algorithms")
authors_set.add("Joan Doe")
books_dict["Data Sturctures and Algorithms"] = "Joan Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

# Display all the books
print("List of Books:") # Book stored should be displayed using a loop
for book in books_list:
    print(book)

# Search for a book
search_title = input("Enter the title of the book to search: ") 
if search_title in books_list:# this code will check if the entered title exist in the books_list
    print(f"Book found! Author: {books_dict[search_title]}")
else :
    print("Book not found!")

# Remove a book
remove_title =input ("Enter the title of the book to remove or eles enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Books removed successfully!")
    print("Books available: ", books_list)
else:
    print("Books not found!")