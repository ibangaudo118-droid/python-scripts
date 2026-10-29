subjects = ("English", "Mathematics", "French")

skills = {"python", "Java", "C++", "python"}
print(skills)

answer= input("Do you want to add anything to skills?(yes/no): ").lower()

while answer != "yes" and answer != "no": 
    answer= input("Do you want to add anything to skills?(yes/no): ").lower()

if answer == "no":
    print("Alright")

elif answer == "yes":
  adds = input("Add another skilss: ")
  skills.add(adds)
  print(skills)



print(subjects)


index = int(input("What index of subject would you like to display: "))

if index >= 0 and index < len(subjects):
  print(subjects[index])

else: 
  print("Invalid-index message")



