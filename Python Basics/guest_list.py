# Initial List
guest_list = ["Alex","Bob","Cathy"]
print(f"{guest_list[0]}, you are invited to the dinner")
print(f"{guest_list[1]}, you are invited to the dinner")
print(f"{guest_list[2]}, you are invited to the dinner")

#Modifying List
print(f"{guest_list[0]}, can't make it")
guest_list[0] = "David"
print(f"{guest_list[0]}, you are invited to the dinner")
print(f"{guest_list[1]}, you are invited to the dinner")
print(f"{guest_list[2]}, you are invited to the dinner")

# Inserting Elements
print("I found a bigger table")
guest_list.insert(0, "Eve")
guest_list.insert(2, "Frank")
guest_list.append("George")
print(f"{guest_list[0]}, you are invited to the dinner")
print(f"{guest_list[1]}, you are invited to the dinner")
print(f"{guest_list[2]}, you are invited to the dinner")
print(f"{guest_list[3]}, you are invited to the dinner")
print(f"{guest_list[4]}, you are invited to the dinner")
print(f"{guest_list[5]}, you are invited to the dinner")

# Removing Elements
print("I can only invite two people to the dinner")

total_guests_to_be_removed = len(guest_list) - 2

for i in range(total_guests_to_be_removed):
    removed_guest = guest_list.pop()
    print(f"{removed_guest}, you are not invited to the dinner")

print(f"{guest_list[0]}, you are still invited to the dinner")
print(f"{guest_list[1]}, you are still invited to the dinner")

print(guest_list)

print(f"I'm inviting {len(guest_list)} people to the dinner")

guest_list.clear()
print(guest_list)