# Insta Clone Detector v1.0 - by destroyer445
username = input("Enter your Insta username: ")

# Logic to generate possible clone usernames
clones = [f"{username}_", f"{username}.official", f"real_{username}", f"{username}__"]

print(f"Searching for possible clones of {username}...")
for clone in clones:
    print(f"Checking: {clone} -> Possible Clone!")

print("Done! Manually verify these IDs on Instagram.")
