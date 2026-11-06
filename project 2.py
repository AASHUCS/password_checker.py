# Password Strength Checker
# A simple project to check the strength of a password based on certain criteria.

print("Welcome to the Password Strength Checker!")
password = input("Enter your password: ")
print("Checking the strength of your password...")

length = len(password)
score = 0

# Length check
if length < 6:
    print("Your password is too short. It should be at least 6 characters long.")
elif length <= 10:
    print("Your password length is medium. Use more than 10 characters for better security.")
    score = score + 1
else:
    print("Your password length is good.")
    score = score + 2

# Check what the password contains (loop sirf ek baar chalega)
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

# Ab har cheez ka message sirf ek baar
if has_upper:
    print("Contains uppercase letters. Good!")
    score = score + 1
else:
    print("No uppercase letters. Add some for better security.")

if has_lower:
    print("Contains lowercase letters. Good!")
    score = score + 1
else:
    print("No lowercase letters. Add some for better security.")

if has_digit:
    print("Contains numbers. Good!")
    score = score + 1
else:
    print("No numbers. Add some for better security.")

if has_special:
    print("Contains special characters. Good!")
    score = score + 1
else:
    print("No special characters. Add some for better security.")

# Final result
print("\nScore:", score, "out of 6")

if score <= 2:
    print("Overall: Weak password")
elif score <= 4:
    print("Overall: Medium password")
else:
    print("Overall: Strong password")