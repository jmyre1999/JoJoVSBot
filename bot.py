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
	{'name': 'Danny', 'image': 'danny.jpg'},
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
	{'name': 'Jotaro Kujo (Stardust Crusaders)', 'image': 'jotaro_kujo.png'},
	{'name': 'DIO (Stardust Crusaders)', 'image': 'dio_sdc.png'},
	{'name': 'Joseph Joestar (Stardust Crusaders)', 'image': 'joseph_joestar_sdc.jpg'},
	{'name': 'Muhammad Avdol', 'image': 'avdol.png'},
	{'name': 'Noriaki Kakyoin', 'image': 'kakyoin.png'},
	{'name': 'Jean Pierre Polnareff (Stardust Crusaders)', 'image': 'polnareff.jpg'},
	{'name': 'Iggy', 'image': 'iggy.png'},
	{'name': 'Gray Fly', 'image': 'gray_fly.jpg'},
	{'name': 'Captain Tennille (Imposter)', 'image': 'captain_tennille.png'},
	{'name': 'Forever', 'image': 'forever.png'},
	{'name': 'Devo the Cursed', 'image': 'devo.png'},
	{'name': 'Rubber Soul', 'image': 'rubber_soul.jpg'},
	{'name': 'Hol Horse', 'image': 'hol_horse.png'},
	{'name': 'J. Geil', 'image': 'j_geil.jpg'},
	{'name': 'Nena', 'image': 'nena.png'},
	{'name': 'ZZ', 'image': 'zz.png'},
	{'name': 'Enya the Hag', 'image': 'enya.png'},
	{'name': 'Steely Dan', 'image': 'steely_dan.jpg'},
	{'name': 'Arabia Fats', 'image': 'arabia_fats.png'},
	{'name': 'Mannish Boy', 'image': 'mannish_boy.jpg'},
	{'name': 'Cameo', 'image': 'cameo.png'},
	{'name': 'Midler', 'image': 'midler.png'},
	{'name': "N'Doul", 'image': 'ndoul.jpg'},
	{'name': 'Oingo', 'image': 'oingo.jpg'},
	{'name': 'Boingo', 'image': 'boingo.png'},
	{'name': 'Chaka', 'image': 'chaka.png'},
	{'name': 'Khan', 'image': 'khan.png'},
	{'name': 'Mariah', 'image': 'mariah.png'},
	{'name': 'Alessi', 'image': 'alessi.jpg'},
	{'name': "Daniel J. D'Arby", 'image': 'daniel_darby.png'},
	{'name': "Telence T. D'Arby", 'image': 'telence_darby.png'},
	{'name': 'Kenny G.', 'image': 'kenny_g.png'},
	{'name': 'Nukesaku', 'image': 'nukesaku.jpg'},
	{'name': 'Vanilla Ice', 'image': 'vanilla_ice.png'},
	{'name': 'Holy Kujo', 'image': 'holy_kujo.png'},
	{'name': 'Anne', 'image': 'anne.jpg'},
	{'name': 'Roses', 'image': 'roses.png'},
	{'name': 'Pet Shop', 'image': 'pet_shop.jpg'},
	# Diamond is Unbreakable
	{'name': 'Josuke Higashikata', 'image': 'josuke_higashikata.png'},
	{'name': 'Yoshikage Kira', 'image': 'kira.jpg'},
	{'name': 'Yoshikage Kira (Bites the Dust)', 'image': 'kira_btd.png'},
	{'name': 'Koichi Hirose (Act 1)', 'image': 'koichi_hirose_act1.jpg'},
	{'name': 'Koichi Hirose (Act 2)', 'image': 'koichi_hirose_act2.jpg'},
	{'name': 'Koichi Hirose (Act 3)', 'image': 'koichi_hirose_act3.jpg'},
	{'name': 'Okuyasu Nijimura', 'image': 'okuyasu.jpg'},
	{'name': 'Rohan Kishibe', 'image': 'rohan_kishibe.jpg'},
	{'name': 'Jotaro Kujo (Diamond is Unbreakable)', 'image': 'jotaro_kujo_diu.png'},
	{'name': 'Tomoko Higashikata', 'image': 'tomoko.png'},
	{'name': "Nijimura's Father", 'image': 'nijimura.png'},
	{'name': 'Joseph Joestar (Diamond is Unbreakable)', 'image': 'joseph_joestar_diu.png'},
	{'name': 'Reimi Sugimoto', 'image': 'reimi.png'},
	{'name': 'Arnold', 'image': 'arnold.jpg'},
	{'name': 'Shigekiyo Yangu', 'image': 'shigechi.jpg'},
	{'name': 'Mikitaka Hazekura', 'image': 'mikitaka.png'},
	{'name': 'Hayato Kawajiri', 'image': 'hayato.png'},
	{'name': 'Angelo Katagiri', 'image': 'angelo.png'},
	{'name': 'Keicho Nijimura', 'image': 'keicho.jpg'},
	{'name': 'Tamami Kobayashi', 'image': 'tamami.png'},
	{'name': 'Toshikazu Hazamada', 'image': 'hazamada.png'},
	{'name': 'Yukako Yamagishi', 'image': 'yukako.jpg'},
	{'name': 'Akira Otoishi', 'image': 'akira.jpg'},
	{'name': 'Bug-Eaten', 'image': 'bug-eaten.jpg'},
	{'name': 'Yoshihiro Kira', 'image': 'yoshihiro.png'},
	{'name': 'Stray Cat', 'image': 'stray_cat.jpg'},
	{'name': 'Ken Oyanagi', 'image': 'ken.png'},
	{'name': 'Yuya Fungami', 'image': 'yuya.png'},
	{'name': 'Toyohiro Kanedaichi', 'image': 'toyohiro.png'},
	{'name': 'Terunosuke Miyamoto', 'image': 'terunosuke.png'},
	{'name': 'Masazo Kinoto', 'image': 'masazo.png'},
	{'name': 'Tonio Trussardi', 'image': 'tonio.jpg'},
	{'name': 'Aya Tsuji', 'image': 'aya.png'},
	{'name': 'Shizuka Joestar', 'image': 'shizuka.png'},
	{'name': 'Shinobu Kawajiri', 'image': 'shinobu.jpg'},
	{'name': 'Police', 'image': 'police.png'},
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