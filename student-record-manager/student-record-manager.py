
student = {
  'name': 'David Udoh',
  "age": 20,
  'course': 'Computer Science'
}

print(student)

user = input("Do you want to update age?(yes/no): ")

if user == "no":
  print("Alright")

elif user == "yes":
  ask_for_age = int(input("Enter value for new age: "))
  student["age"] = ask_for_age
  

else:
  print("Invalid input")

new_key = input("Do you want to add a new key-value pair(yes/no)?: ")

if new_key == "no":
  print("Alright")

elif new_key == "yes":
  ask_of_new_key_name = input("Enter the key name: ")
  ask_of_new_key_value = input("Enter the value for the new key: ")
  student[ask_of_new_key_name] = ask_of_new_key_value
  

else: 
  print("Invalid input")

remove_key = input("Do you want to remove a key(yes/no)?: ")

if remove_key == "no":
  print("Alright")

elif remove_key == "yes":
  ask_of_remove_key = input("Which key do you want to remove: ")
  if ask_of_remove_key not in student:
    print("Invalid Key")
  else:
    student.pop(ask_of_remove_key)
    
  

else:
  print("Invalid input")

print(student)
  