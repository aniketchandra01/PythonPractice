import os
os.makedirs('./Letters', exist_ok=True)

with open('Names.txt',mode='r') as file:
    names = file.readlines()

for name in names:
    filename = name.strip()
    with open(f"./Letters/{filename}.txt",mode='w') as file:
        file.write(f'''
Dear {name},

You are invited to my birthday this Saturday.

Hope you can make it!

Angela ''')