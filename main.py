thisdict ={
    "Raz":"09-17-2000",
    "D'Andre":"09-24-2000",
    "Tal":"03-03-1999",
    "Zevi":"08-25-2004",
    "Amit":"10-23-2001",
    "Ronen":"12-06-1970",
    "Havi":"05-06-1967",
    "Daniel":"07-22-2002",
    "Rachel":"08-23-1994",
}

for name,bday in thisdict.items():
    print(f"happy birthday {name} {bday}")

def bday(name,bday):
    return f"happy birthday {name} {bday}"
print (bday("Raz","09-17-2000"))



