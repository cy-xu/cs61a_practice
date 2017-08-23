shakes = open('shakespeare.txt')
text = shakes.read().split()

print(text[:25])
print(len(text))
{w for w in text if len(w) == 6 and w[::-1] in text}


