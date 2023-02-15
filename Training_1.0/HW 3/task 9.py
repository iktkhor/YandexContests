students = int(input())
languages = {}
all_known = []
atleast_one_known = []

for i in range(students):
    count = int(input())
    for i in range(count):
        lang = input()
        if lang not in languages:
            languages[lang] = 0
        languages[lang] += 1

for key, value in languages.items():
    if value == students:
        all_known.append(key)
        atleast_one_known.append(key)
    else:
        atleast_one_known.append(key)

print(len(all_known))
print('\n'.join(all_known))
print(len(atleast_one_known))
print('\n'.join(atleast_one_known))