# string concatenation

youtuber = ""

#few ways
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all tthe time because \ I love to {verb1}. Stay hydrated and {verb2} like {famous_person}."

print(madlib)