message = "Hello ladies and gentle men. I am Bernard Kirk Katamanso and I am here to present on the topic: Investigating the nexus between the implementaion of various computer architectures their effects and properties"
characters = {}

for character in message:
    characters.setdefault(character,0)
    characters[character] += 1

print(characters)