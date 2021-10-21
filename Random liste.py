import random

listRandom = ["Hvad hedder verdens fattigste konge? - Kong Kurs", "Hvorfor hyler prærieulve kun om natten? - De kan kun se kaktusser om dagen", "Din mor"]
RandomJoke = random.randrange(len(listRandom))
print(random.choice(listRandom))