student = input("Enter your full name: ")

while True:
  try:
    age = int(input("How old are you: "))
    break
  except ValueError:
    print("Invalid")

fee = input("Have you registered?(yes/no): ")
while True:
  if age < 16:
    print ("Registration Denied. You must be at least 16 years old")
    break
  elif fee == "no":
    print("Payment is required")
    break
  elif age >= 16 and fee == "yes":
    print("Registration approved")
    break
  else:
    print("Invalid payment response")
    fee = input("Have you registered?(yes/no): ")