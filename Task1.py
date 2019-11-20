# Page 46-47
print("Page 46-47")
guestList = ["Apoy", "Aloi", "Popoi"]

for names in guestList:
    print("Wow, " + names + " is invited !")

print("")

removed = guestList.pop()
guestList.append("Budi Setiawan")
print("But", removed, "cannot come oh no :(..... but", guestList[-1], "is joining us now yay !")

print("")

for names in guestList:
    print("Wow, " + names + " is invited !")

print("")

print("Wow now we have a bigger table so 3 more people can come")

print("")

guestList.insert(0, "Jong Aru")
guestList.insert(2, "Popoi 2")
guestList.append("James")

for names in guestList:
    print("Wow, " + names + " is invited !")

print("Tapi bohong :( only 2 people can come")

for i in range(4):
    guestList.pop()

print("")

for names in guestList:
    print("Wow, " + names + " is invited !")

for i in range(2):
    del guestList[i-1]

print(guestList)

print("")
print("")
print("")

#Page 50
print("Page 50")

places = ["Old York", "South Canada", "Barat Leste"]

print(places)

print(sorted(places))

print(places)

print(sorted(places, reverse = True))

print(places)

places.reverse()

print(places)

places.reverse()

print(places)

places.sort()

print(places)

places.sort(reverse = True)

print(places)

print("sir Bagus told me to make modifications")
