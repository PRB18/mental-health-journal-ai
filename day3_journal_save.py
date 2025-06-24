import json
import os

entry = {
	"date":"2025-06-23",
	"mood":"Nervous",
	"entry":"nervous",
	"reflection":"

    It sounds like you're feeling nervous. That's completely understandable; nervousness is a common human experience. It's okay to feel this way. There's no need to judge yourself for it.

Sometimes just acknowledging the feeling can be a big help. The simple act of writing "nervous" down shows you're taking the time to understand what you're going through.

Would you like to explore what might be causing this nervousness? Perhaps talking about it, even just a little, could help lessen the intensity. There's no pressure at all, but if you'd like to share more, I'm here to listen without judgment. Even if you don't know what's causing it, that's alright too. We can simply sit with the feeling together.

Remember, you are not alone in feeling this way, and it's perfectly okay to seek support. If the nervousness becomes overwhelming, please reach out to a trusted friend, family member, or mental health professional."
	}


#create file if it doesnt exist already

if not os.path.exist("data/journal.json"):
	with open("data/journal.json","w") as f:
		json.dump([], f)


#load existing data
with open("data/journal.json", "r") as f:
	data=json.load(f)

#append the new entry
data.append(entry)

#save it back
with open("data/journal/json", "w") as f:
	json.dump(data, f, indent=2)
