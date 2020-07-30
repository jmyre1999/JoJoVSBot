from config import getApi
import os
import random

api = getApi()
characters = [
	# Part 1: Phantom Blood
	{'name': 'Jonathan Joestar', 'image': 'jonathan_joestar.png'},
	{'name': 'Dio Brando (Phantom Blood)', 'image': 'dio_brando.png'},
	{'name': 'Robert E. O. Speedwagon', 'image': 'speedwagon.jpg'},
	{'name': 'William A. Zeppeli', 'image': 'william_zeppeli.png'},
	{'name': 'Poco', 'image': 'poco.jpg'},
	{'name': 'Dire', 'image': 'dire.jpg'},
	{'name': 'Straits (Phantom Blood)', 'image': 'straits.png'},
	{'name': 'Tonpetty', 'image': 'tonpetty.png'},
	{'name': 'Erina Pendleton', 'image': 'erina_pendleton.jpg'},
	{'name': 'Wang Chan', 'image': 'wang_chan.jpg'},
	{'name': 'Bruford', 'image': 'bruford.png'},
	{'name': 'Tarkus', 'image': 'tarkus.jpg'},
	# Part 2: Battle Tendency
	{'name': 'Joseph Joestar (Battle Tendency)', 'image': 'joseph_joestar.png'},
	{'name': 'Caesar A. Zeppeli', 'image': 'caesar_zeppeli.jpg'},
	{'name': 'Lisa Lisa', 'image': 'lisa_lisa.jpg'},
	{'name': 'Kars (Light Mode)', 'image': 'kars.png'},
	{'name': 'Kars (Ultimate Life Form)', 'image': 'kars_ultimate.jpg'},
	{'name': 'Wamuu', 'image': 'wamuu.png'},
	{'name': 'Esidisi', 'image': 'esidisi.jpg'},
	{'name': 'Santana', 'image': 'santana.jpg'},
	{'name': 'Rudol Von Stroheim', 'image': 'stroheim.jpg'},
	{'name': 'Smokey Brown', 'image': 'smokey.png'},
	{'name': 'Mark', 'image': 'mark.jpg'},
	{'name': 'Messina', 'image': 'messina.png'},
	{'name': 'Loggins', 'image': 'loggins.png'},
	{'name': 'Suzie Q', 'image': 'suzie_q.png'},
	{'name': 'Mario Zeppeli', 'image': 'mario_zeppeli.png'},
	{'name': 'Wired Beck', 'image': 'wired_beck.png'},
	{'name': 'Straits (Battle Tendency)', 'image': 'straits_vampire.png'},
	{'name': 'Donovan', 'image': 'donovan.jpg'},
	# Part 3: Stardust Crusaders
]

def postStatus(update):
	status = api.PostUpdate(update)
	print(status)

def postMatchUp(text, image1, image2):
	api.PostUpdate(text, media=[image1, image2])

def createMatchUp():
	first_character = random.randint(0, len(characters) - 1)
	second_character = random.randint(0, len(characters) - 1)
	while first_character == second_character:
		second_character = random.randint(0, len(characters) - 1)
	status = postMatchUp(characters[first_character]['name'] + ' VS ' + characters[second_character]['name'], 'characters/' + characters[first_character]['image'], 'characters/' + characters[second_character]['image'])

createMatchUp()