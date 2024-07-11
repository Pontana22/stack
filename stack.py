import random

used = []
remaining = [
    "Your brain cell must be lonely.",
    "If only closed minds came with closed mouths.",
    "You're proof that even evolution makes mistakes.",
    "When you were born, the gene pool needed chlorine.",
    "You bring everyone so much joy when you leave the room.",
    "Are you always this stupid, or are you making a special effort today?",
    "Light travels faster than sound, which is why you seemed bright until you spoke.",
    "If ignorance is bliss, you must be the happiest person alive.",
    "I’d agree with you, but then we’d both be wrong.",
    "You're the reason the gene pool needs a lifeguard.",
    "You have a room temperature IQ.",
    "The wheel is spinning, but the hamster is dead.",
    "Keep talking; someday you’ll say something intelligent.",
    "You’re as bright as a black hole, and twice as dense.",
    "You’re the reason they put instructions on shampoo.",
    "You’re about as useful as a screen door on a submarine.",
    "I don't know what makes you so dumb, but it really works.",
    "You're the poster child for birth control.",
    "Your IQ test came back negative.",
    "You’ve got a great brain, too bad it’s not plugged in.",
    "You bring a lot of joy, especially when you leave.",
    "You’re living proof that nature abhors a vacuum.",
    "You couldn't pour water out of a boot with instructions on the heel.",
    "You’re like a cloud; when you disappear, it’s a beautiful day.",
    "You’re the type of person who brings a snowball to a gunfight.",
    "Your intellect rivals that of garden tools.",
    "You’re as sharp as a marble.",
    "Even duct tape can’t fix stupid, but it can muffle the sound.",
    "You’ve got the perfect face for radio.",
    "You’re a real-life example of Murphy’s Law.",
    "I’m glad to see you’re not letting your education get in the way of your ignorance.",
    "The fact that you’ve lived this long is remarkable.",
    "If you were any less intelligent, you’d have to be watered twice a week.",
    "It’s impossible to underestimate you.",
    "Brains aren't everything; in your case, they're nothing.",
    "You're proof that even God makes mistakes.",
    "If I wanted to hear from an idiot, I'd watch reality TV.",
    "I’ve seen smarter cabinets at IKEA.",
    "Your brain has two parts. In the left part, there’s nothing right, and in the right part, there’s nothing left.",
    "I bet your brain feels as good as new, seeing that you’ve never used it.",
    "If I had a face like yours, I’d sue my parents.",
    "You're the reason they invented the middle finger.",
    "You’re as sharp as a bowling ball.",
    "You must have a very low opinion of people if you think they’re your equals.",
    "You couldn’t organize a one-car parade.",
    "You’re as much use as a chocolate teapot.",
    "You’re proof that light travels faster than sound; you appear bright until you speak.",
    "I’d slap you, but that would be animal abuse.",
    "You’re a prime candidate for natural selection.",
    "If brains were taxed, you’d get a refund."
]

def stack(items):
	rest = 0

	while items % 64 != 0:
		rest += 1
		items -= 1
	
	stacks = int(items / 64)

	return(stacks, rest)

def insult():
	global used
	global remaining

	if len(remaining) == 0:
		remaining = used
		used = []

	reply = random.choice(remaining)
	remaining.remove(reply)
	used.append(reply)

	return(reply)

def main():
	reasonable = False

	while not reasonable:
		userInput = input("\n")

		if userInput.lower() == "help":
			print("Insert any reasonable number of items and I will convert them to stacks and items")
			print("Do anything else and I will insult you")
		elif userInput.lower() == "stop" or userInput.lower() == "exit" or userInput.lower() == "quit" or userInput.lower() == "fuck off":
			exit()
		elif not userInput.isnumeric() or int(userInput) <= 64:
			print(insult())
		else:
			reasonable = True
		
	output = stack(int(userInput))

	s = "stacks"
	i = "items"

	if output[0] == 1:
		s = "stack"
	if output[1] == 1:
		i = "item"

	print(output[0], s, "and", output[1], i)
	
if __name__ == "__main__":
	while True:
		main()