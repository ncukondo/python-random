import random

source = list(range(1,19))

print(f"source:{source}")

for i in range(1,6):
    generated = random.sample(source,len(source))
    print(f"generated {i}: {generated}")