text = input("Enter a sentence:") or "I Love learning python"

print("Length",len(text))
print("Characters in the given texts:")

for ch in text:
    print(ch,end=",")
