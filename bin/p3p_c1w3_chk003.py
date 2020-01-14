items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0
for item in items:
    if 'w' in item.strip():
        acc_num+=1
print(acc_num)
