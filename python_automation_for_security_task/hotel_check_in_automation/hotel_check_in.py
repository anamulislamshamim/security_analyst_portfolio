initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

# create a guests.txt file and store the initial_guests names in the file
guests = open('./guests.txt', 'w')

# iterating through initial_guests list and store value in the guests.txt file
for guest in initial_guests:
    guests.write(guest + '\n')


# close guests.txt file
guests.close()


new_guests = ["Sam", "Danielle", "Jacob"]
# add the new_guests names in the guests.txt file too
with open("./guests.txt", "a") as file:
    for new_guest in new_guests:
        file.write(new_guest + '\n')


checked_out=["Andrea", "Manuel", "Khalid"]
# remove the checked_out guests list from the guests.txt file
temp_guest_list = []
# Store the guest name from guests.txt file in temp_guest_list 
with open('guests.txt', 'r') as file:
    for guest in file:
        temp_guest_list.append(guest.strip())


# Remove checked_out names from the temp_guest_list and store the rest of
# guests in the guests.txt file again
with open('guests.txt', 'w') as file:
    for guest in temp_guest_list:
        if guest not in checked_out:
            file.write(guest + '\n')


# Now let's check whether guests_to_check = ['Bob', 'Andrea'] are still checked in. 
guests_to_check = ['Bob', 'Andrea']
checked_in = []
# now check whether 'Bob' or 'Andrrea' are still in checked in ?
with open("guests.txt", "r") as file:
    for guest in file:
        checked_in.append(guest.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))