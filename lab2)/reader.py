s = input()
ans = []
for i in range(1, int(input()) + 1):
    with open(f"{s}/{i}.py", "r") as file:
        # text = file.readlines()
        text = [i.rstrip('\n') for i in file.readlines()]
        ans.append(text)
for i in  range(len(ans)):
    with open(f"{s}.py", "a") as second_file:
        second_file.write(f'#Task {i+1} \n')
        second_file.write('\n'.join(ans[i]))
        second_file.write('\n')
