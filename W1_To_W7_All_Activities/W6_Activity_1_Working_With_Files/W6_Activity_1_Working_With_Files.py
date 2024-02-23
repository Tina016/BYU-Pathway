#Week 6 | Activity 1 - Working with Files

"""
Author: Martina Toebe

Purpose: Practice opening files and reading text from them.

"""
# Open a file
books = open("books.txt")

# Open a file using with
with open("books.txt") as books_file:
    for line in books_file:
        clean_line = line.strip() #Removing extra whitespace using strip
        print(clean_line)

# End