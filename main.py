shopping_dict = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb', 'pączek', 'bułki']
}

i = 0

print("Lista zakupów")

for store, things in shopping_dict.items():
    capitalized_things = [item.capitalize() for item in things]
    print(f"Idę do {store.capitalize()}, kupuję tu następujące rzeczy: {capitalized_things}")
    i += len(things)

print(f"W sumie kupuję {i} produktów")
print("Nobody expected the spanish inqusition")
print("I like trains")

for i in range(0,5):
    print("I like python!")
