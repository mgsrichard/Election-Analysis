dwarves = ['Dopey','Bashful','Sleepy','Grumpy','Doc','Sneezy','Happy']

favorite_dwarf = int(input('Choose a number from 1 to 7'))

dwarf_report=(
    f"Your favorite dwarf is {dwarves[favorite_dwarf-1]}"
)

print(dwarf_report)
new_dwarf=""
new_dwarf=input('Make up a fun name for a new dwarf!')
dwarves.append(new_dwarf)
new_dwarf_report=(
    f"Now there are eight dwarves!"
)
print(new_dwarf_report)
for dwarf in dwarves:
    print(dwarf)