# Create a greeting variable for the mentor using the data imported from the nested files
# Print the greeting to your terminal

# It should look something like "Good afternoon Simon Jackson!"
import data.file_1 as f1, data.file_2 as f2

greeting = "Good afternoon " + f1.mentor_first_name + " " + f2.mentor_last_name
print(greeting)
