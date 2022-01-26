file = open('jakis_tekst.txt', 'r')

for line in file:
    print(line, end = "")

file.close()

print('\n')

#%%

with open('jakis_tekst.txt', 'r') as file:
    for line in file:
        print(line, end='')

# %%

with open('jakis_tekst.txt', 'r') as file:
    line = file.readline()
    print(line)

# %%
with open('jakis_tekst.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# %%
with open('jakis_tekst.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# %%
with open('jakis_tekst.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()