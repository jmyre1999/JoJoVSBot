from config import getApi
import os
import random

api = getApi()
characters = [
	# Part 1: Phantom Blood
	{'name': 'Jonathan Joestar', 'image': 'jonathan_joestar.png', 'anime': True},
	{'name': 'Dio Brando (Phantom Blood)', 'image': 'dio_brando.png', 'anime': True},
	{'name': 'Robert E. O. Speedwagon', 'image': 'speedwagon.jpg', 'anime': True},
	{'name': 'William A. Zeppeli', 'image': 'william_zeppeli.png', 'anime': True},
	{'name': 'Poco', 'image': 'poco.jpg', 'anime': True},
	{'name': 'Dire', 'image': 'dire.jpg', 'anime': True},
	{'name': 'Straits (Phantom Blood)', 'image': 'straits.png', 'anime': True},
	{'name': 'Tonpetty', 'image': 'tonpetty.png', 'anime': True},
	{'name': 'Erina Pendleton', 'image': 'erina_pendleton.jpg', 'anime': True},
	{'name': 'Wang Chan', 'image': 'wang_chan.jpg', 'anime': True},
	{'name': 'Bruford', 'image': 'bruford.png', 'anime': True},
	{'name': 'Tarkus', 'image': 'tarkus.jpg', 'anime': True},
	{'name': 'Danny', 'image': 'danny.jpg', 'anime': True},
	# Part 2: Battle Tendency
	{'name': 'Joseph Joestar (Battle Tendency)', 'image': 'joseph_joestar.png', 'anime': True},
	{'name': 'Caesar A. Zeppeli', 'image': 'caesar_zeppeli.jpg', 'anime': True},
	{'name': 'Lisa Lisa', 'image': 'lisa_lisa.jpg', 'anime': True},
	{'name': 'Kars (Light Mode)', 'image': 'kars.png', 'anime': True},
	{'name': 'Kars (Ultimate Life Form)', 'image': 'kars_ultimate.jpg', 'anime': True},
	{'name': 'Wamuu', 'image': 'wamuu.png', 'anime': True},
	{'name': 'Esidisi', 'image': 'esidisi.jpg', 'anime': True},
	{'name': 'Santana', 'image': 'santana.jpg', 'anime': True},
	{'name': 'Rudol Von Stroheim', 'image': 'stroheim.jpg', 'anime': True},
	{'name': 'Smokey Brown', 'image': 'smokey.png', 'anime': True},
	{'name': 'Mark', 'image': 'mark.jpg', 'anime': True},
	{'name': 'Messina', 'image': 'messina.png', 'anime': True},
	{'name': 'Loggins', 'image': 'loggins.png', 'anime': True},
	{'name': 'Suzie Q', 'image': 'suzie_q.png', 'anime': True},
	{'name': 'Mario Zeppeli', 'image': 'mario_zeppeli.png', 'anime': True},
	{'name': 'Wired Beck', 'image': 'wired_beck.png', 'anime': True},
	{'name': 'Straits (Battle Tendency)', 'image': 'straits_vampire.png', 'anime': True},
	{'name': 'Donovan', 'image': 'donovan.jpg', 'anime': True},
	# Part 3: Stardust Crusaders
	{'name': 'Jotaro Kujo (Stardust Crusaders)', 'image': 'jotaro_kujo.png', 'anime': True},
	{'name': 'DIO (Stardust Crusaders)', 'image': 'dio_sdc.png', 'anime': True},
	{'name': 'Joseph Joestar (Stardust Crusaders)', 'image': 'joseph_joestar_sdc.jpg', 'anime': True},
	{'name': 'Muhammad Avdol', 'image': 'avdol.png', 'anime': True},
	{'name': 'Noriaki Kakyoin', 'image': 'kakyoin.png', 'anime': True},
	{'name': 'Jean Pierre Polnareff (Stardust Crusaders)', 'image': 'polnareff.jpg', 'anime': True},
	{'name': 'Iggy', 'image': 'iggy.png', 'anime': True},
	{'name': 'Gray Fly', 'image': 'gray_fly.jpg', 'anime': True},
	{'name': 'Captain Tennille (Imposter)', 'image': 'captain_tennille.png', 'anime': True},
	{'name': 'Forever', 'image': 'forever.png', 'anime': True},
	{'name': 'Devo the Cursed', 'image': 'devo.png', 'anime': True},
	{'name': 'Rubber Soul', 'image': 'rubber_soul.jpg', 'anime': True},
	{'name': 'Hol Horse', 'image': 'hol_horse.png', 'anime': True},
	{'name': 'J. Geil', 'image': 'j_geil.jpg', 'anime': True},
	{'name': 'Nena', 'image': 'nena.png', 'anime': True},
	{'name': 'ZZ', 'image': 'zz.png', 'anime': True},
	{'name': 'Enya the Hag', 'image': 'enya.png', 'anime': True},
	{'name': 'Steely Dan', 'image': 'steely_dan.jpg', 'anime': True},
	{'name': 'Arabia Fats', 'image': 'arabia_fats.png', 'anime': True},
	{'name': 'Mannish Boy', 'image': 'mannish_boy.jpg', 'anime': True},
	{'name': 'Cameo', 'image': 'cameo.png', 'anime': True},
	{'name': 'Midler', 'image': 'midler.png', 'anime': True},
	{'name': "N'Doul", 'image': 'ndoul.jpg', 'anime': True},
	{'name': 'Oingo', 'image': 'oingo.jpg', 'anime': True},
	{'name': 'Boingo', 'image': 'boingo.png', 'anime': True},
	{'name': 'Chaka', 'image': 'chaka.png', 'anime': True},
	{'name': 'Khan', 'image': 'khan.png', 'anime': True},
	{'name': 'Mariah', 'image': 'mariah.png', 'anime': True},
	{'name': 'Alessi', 'image': 'alessi.jpg', 'anime': True},
	{'name': "Daniel J. D'Arby", 'image': 'daniel_darby.png', 'anime': True},
	{'name': "Telence T. D'Arby", 'image': 'telence_darby.png', 'anime': True},
	{'name': 'Kenny G.', 'image': 'kenny_g.png', 'anime': True},
	{'name': 'Nukesaku', 'image': 'nukesaku.jpg', 'anime': True},
	{'name': 'Vanilla Ice', 'image': 'vanilla_ice.png', 'anime': True},
	{'name': 'Holy Kujo', 'image': 'holy_kujo.png', 'anime': True},
	{'name': 'Anne', 'image': 'anne.jpg', 'anime': True},
	{'name': 'Roses', 'image': 'roses.png', 'anime': True},
	{'name': 'Pet Shop', 'image': 'pet_shop.jpg', 'anime': True},
	# Diamond is Unbreakable
	{'name': 'Josuke Higashikata', 'image': 'josuke_higashikata.png', 'anime': True},
	{'name': 'Yoshikage Kira', 'image': 'kira.jpg', 'anime': True},
	{'name': 'Yoshikage Kira (Bites the Dust)', 'image': 'kira_btd.png', 'anime': True},
	{'name': 'Koichi Hirose (Act 1)', 'image': 'koichi_hirose_act1.jpg', 'anime': True},
	{'name': 'Koichi Hirose (Act 2)', 'image': 'koichi_hirose_act2.jpg', 'anime': True},
	{'name': 'Koichi Hirose (Act 3)', 'image': 'koichi_hirose_act3.jpg', 'anime': True},
	{'name': 'Okuyasu Nijimura', 'image': 'okuyasu.jpg', 'anime': True},
	{'name': 'Rohan Kishibe', 'image': 'rohan_kishibe.jpg', 'anime': True},
	{'name': 'Jotaro Kujo (Diamond is Unbreakable)', 'image': 'jotaro_kujo_diu.png', 'anime': True},
	{'name': 'Tomoko Higashikata', 'image': 'tomoko.png', 'anime': True},
	{'name': "Nijimura's Father", 'image': 'nijimura.png', 'anime': True},
	{'name': 'Joseph Joestar (Diamond is Unbreakable)', 'image': 'joseph_joestar_diu.png', 'anime': True},
	{'name': 'Reimi Sugimoto', 'image': 'reimi.png', 'anime': True},
	{'name': 'Arnold', 'image': 'arnold.jpg', 'anime': True},
	{'name': 'Shigekiyo Yangu', 'image': 'shigechi.jpg', 'anime': True},
	{'name': 'Mikitaka Hazekura', 'image': 'mikitaka.png', 'anime': True},
	{'name': 'Hayato Kawajiri', 'image': 'hayato.png', 'anime': True},
	{'name': 'Angelo Katagiri', 'image': 'angelo.png', 'anime': True},
	{'name': 'Keicho Nijimura', 'image': 'keicho.jpg', 'anime': True},
	{'name': 'Tamami Kobayashi', 'image': 'tamami.png', 'anime': True},
	{'name': 'Toshikazu Hazamada', 'image': 'hazamada.png', 'anime': True},
	{'name': 'Yukako Yamagishi', 'image': 'yukako.jpg', 'anime': True},
	{'name': 'Akira Otoishi', 'image': 'akira.jpg', 'anime': True},
	{'name': 'Bug-Eaten', 'image': 'bug-eaten.jpg', 'anime': True},
	{'name': 'Yoshihiro Kira', 'image': 'yoshihiro.png', 'anime': True},
	{'name': 'Stray Cat', 'image': 'stray_cat.jpg', 'anime': True},
	{'name': 'Ken Oyanagi', 'image': 'ken.png', 'anime': True},
	{'name': 'Yuya Fungami', 'image': 'yuya.png', 'anime': True},
	{'name': 'Toyohiro Kanedaichi', 'image': 'toyohiro.png', 'anime': True},
	{'name': 'Terunosuke Miyamoto', 'image': 'terunosuke.png', 'anime': True},
	{'name': 'Masazo Kinoto', 'image': 'masazo.png', 'anime': True},
	{'name': 'Tonio Trussardi', 'image': 'tonio.jpg', 'anime': True},
	{'name': 'Aya Tsuji', 'image': 'aya.png', 'anime': True},
	{'name': 'Shizuka Joestar', 'image': 'shizuka.png', 'anime': True},
	{'name': 'Shinobu Kawajiri', 'image': 'shinobu.jpg', 'anime': True},
	{'name': 'Police', 'image': 'police.png', 'anime': True},
	# Golden Wind
	{'name': 'Giorno Giovanna (GE)', 'image': 'giorno_ge.jpg', 'anime': True},
	{'name': 'Giorno Giovanna (GER)', 'image': 'giorno_ger.jpg', 'anime': True},
	{'name': 'Diavolo', 'image': 'diavolo.jpg', 'anime': True},
	{'name': 'Vinegar Doppio', 'image': 'doppio.png', 'anime': True},
	{'name': 'Bruno Bucciarati', 'image': 'bruno.jpg', 'anime': True},
	{'name': 'Leone Abbacchio', 'image': 'abbacchio.png', 'anime': True},
	{'name': 'Guido Mista', 'image': 'mista.jpg', 'anime': True},
	{'name': 'Narancia Ghirga', 'image': 'narancia.jpg', 'anime': True},
	{'name': 'Pannacotta Fugo', 'image': 'fugo.jpg', 'anime': True},
	{'name': 'Trish Una', 'image': 'trish.jpg', 'anime': True},
	{'name': 'Pericolo', 'image': 'pericolo.jpg', 'anime': True},
	{'name': 'Coco Jumbo', 'image': 'coco_jumbo.png', 'anime': True},
	{'name': 'Mario Zucchero', 'image': 'zucchero.jpg', 'anime': True},
	{'name': 'Sale', 'image': 'sale.jpg', 'anime': True},
	{'name': 'Leaky-Eye Luca', 'image': 'luca.png', 'anime': True},
	{'name': 'Risotto Nero', 'image': 'risotto.jpg', 'anime': True},
	{'name': 'Formaggio', 'image': 'formaggio.jpg', 'anime': True},
	{'name': 'Illuso', 'image': 'illuso.png', 'anime': True},
	{'name': 'Prosciutto', 'image': 'prosciutto.jpg', 'anime': True},
	{'name': 'Pesci', 'image': 'pesci.png', 'anime': True},
	{'name': 'Melone', 'image': 'melone.png', 'anime': True},
	{'name': 'Ghiaccio', 'image': 'ghiaccio.jpg', 'anime': True},
	{'name': 'Sorbet', 'image': 'sorbet.png', 'anime': True},
	{'name': 'Gelato', 'image': 'gelato.jpg', 'anime': True},
	{'name': 'Squalo', 'image': 'squalo.jpg', 'anime': True},
	{'name': 'Tiziano', 'image': 'tiziano.jpg', 'anime': True},
	{'name': 'Carne', 'image': 'carne.jpg', 'anime': True},
	{'name': 'Cioccolata', 'image': 'cioccolata.jpg', 'anime': True},
	{'name': 'Secco', 'image': 'secco.jpg', 'anime': True},
	{'name': 'Jean Pierre Polnareff (Golden Wind)', 'image': 'polnareff_gw.jpg', 'anime': True},
	{'name': 'Scolippi', 'image': 'scolippi.jpg', 'anime': True},
	# Stone Ocean
	{'name': 'Jolyne Cujoh', 'image': 'jolyne.jpg', 'anime': True},
	{'name': 'Enrico Pucci', 'image': 'pucci.JPG', 'anime': True},
	{'name': 'Enrico Pucci (C-Moon)', 'image': 'pucci_cmoon.JPG', 'anime': True},
	{'name': 'Enrico Pucci (MiH)', 'image': 'pucci_mih.JPG', 'anime': True},
	{'name': 'Ermes Costello', 'image': 'ermes.jpg', 'anime': True},
	{'name': 'Emporio Alnino', 'image': 'emporio.jpg', 'anime': True},
	{'name': 'Weather Emporio', 'image': 'weather_emporio.JPG', 'anime': True},
	{'name': 'Jotaro Kujo (Stone Ocean)', 'image': 'jotaro_kujo_so.jpg', 'anime': True},
	{'name': 'Foo Fighters', 'image': 'foo_fighters.jpg', 'anime': True},
	{'name': 'Narciso Anasui', 'image': 'anasui.jpg', 'anime': True},
	{'name': 'Weather Report', 'image': 'weather_report.jpg', 'anime': True},
	{'name': 'Gwess', 'image': 'gwess.jpg', 'anime': True},
	{'name': 'Donatello Versus', 'image': 'donatello.JPG', 'anime': True},
	{'name': 'Rikiel', 'image': 'rikiel.JPG', 'anime': True},
	{'name': 'Ungalo', 'image': 'ungalo.JPG', 'anime': True},
	{'name': 'The Green Baby', 'image': 'green_baby.JPG', 'anime': True},
	{'name': 'Johngalli A', 'image': 'johngalli.png', 'anime': True},
	{'name': 'Sports Maxx', 'image': 'sports_maxx.jpg', 'anime': True},
	{'name': 'Miuccia Miuller', 'image': 'miuccia.JPG', 'anime': True},
	{'name': 'Thunder McQueen', 'image': 'thunder_mcqueen.jpg', 'anime': True},
	{'name': 'Miraschon', 'image': 'miraschon.png', 'anime': True},
	{'name': 'Lang Rangler', 'image': 'lang_rangler.JPG', 'anime': True},
	{'name': 'Viviano Westwood', 'image': 'viviano.JPG', 'anime': True},
	{'name': 'Kenzou', 'image': 'kenzou.JPG', 'anime': True},
	{'name': 'Guccio', 'image': 'guccio.JPG', 'anime': True},
	{'name': 'D an G', 'image': 'd_an_g.png', 'anime': True},
	{'name': 'Romeo Jisso', 'image': 'romeo.png', 'anime': True},
	{'name': 'Perla Pucci', 'image': 'perla_pucci.JPG', 'anime': True},
	{'name': 'Gloria Costello', 'image': 'gloria_costello.jpg', 'anime': True},
	# Steel Ball Run
	{'name': 'Johnny Joestar (Act 1)', 'image': 'johnny_act_1.JPG', 'anime': False},
	{'name': 'Johnny Joestar (Act 2)', 'image': 'johnny_act_2.JPG', 'anime': False},
	{'name': 'Johnny Joestar (Act 3)', 'image': 'johnny_act_3.JPG', 'anime': False},
	{'name': 'Johnny Joestar (Act 4)', 'image': 'johnny_act_4.JPG', 'anime': False},
	{'name': 'Funny Valentine (D4C)', 'image': 'funny_valentine_d4c.JPG', 'anime': False},
	{'name': 'Funny Valentine (Love Train)', 'image': 'funny_valentine_love_train.jpg', 'anime': False},
	{'name': 'Gyro Zeppeli', 'image': 'gyro_zeppeli.JPG', 'anime': False},
	{'name': 'Lucy Steel', 'image': 'lucy_steel.JPG', 'anime': False},
	{'name': 'Steven Steel', 'image': 'steven_steel.JPG', 'anime': False},
	{'name': 'Hot Pants', 'image': 'hot_pants.JPG', 'anime': False},
	{'name': 'Mountain Tim', 'image': 'mountain_tim.JPG', 'anime': False},
	{'name': 'Diego Brando (Scary Monsters)', 'image': 'diego_scary_monsters.JPG', 'anime': False},
	{'name': 'Diego Brando (The World)', 'image': 'diego_the_world.JPG', 'anime': False},
	{'name': 'Wekapipo', 'image': 'wekapipo.JPG', 'anime': False},
	{'name': 'Pocoloco', 'image': 'pocoloco.JPG', 'anime': False},
	{'name': 'Norisuke Higashikata I', 'image': 'norisuke_higashikata_I.JPG', 'anime': False},
	{'name': 'Blackmore', 'image': 'blackmore.JPG', 'anime': False},
	{'name': 'Mike O.', 'image': 'mike_o.JPG', 'anime': False},
	{'name': 'Ringo Roadagain', 'image': 'ringo_roadagain.JPG', 'anime': False},
	{'name': 'Axl RO', 'image': 'axl_ro.JPG', 'anime': False},
	{'name': 'Magent Magent', 'image': 'magent_magent.JPG', 'anime': False},
	{'name': 'Dr. Ferdinand', 'image': 'dr_ferdinand.JPG', 'anime': False},
	{'name': 'D-I-S-C-O', 'image': 'disco.JPG', 'anime': False},
	{'name': 'Sandman', 'image': 'sandman.JPG', 'anime': False},
	{'name': 'Benjamin Boom Boom', 'image': 'benjamin_boom_boom.JPG', 'anime': False},
	{'name': 'Andre Boom Boom', 'image': 'andre_boom_boom.JPG', 'anime': False},
	{'name': 'L.A. Boom Boom', 'image': 'la_boom_boom.JPG', 'anime': False},
	{'name': 'Mrs. Robinson', 'image': 'mrs_robinson.JPG', 'anime': False},
	{'name': 'Oyecomova', 'image': 'oyecomov.JPG', 'anime': False},
	{'name': 'Sugar Mountain', 'image': 'sugar_mountain.JPG', 'anime': False},
	{'name': 'Scarlet Valentine', 'image': 'scarlet_valentine.JPG', 'anime': False},
	{'name': 'Jesus Christ', 'image': 'jesus.JPG', 'anime': False},
	{'name': 'Danny (Forma de Mouse)', 'image': 'danny_sbr.jpg', 'anime': False},
	{'name': 'Marco', 'image': 'marco.JPG', 'anime': False},
	{'name': 'Fritz von Stroheim', 'image': 'fritz_von_stroheim.JPG', 'anime': False},
	{'name': 'Urmud Avdol', 'image': 'urmud_avdol.JPG', 'anime': False},
	# JoJolion
	{'name': 'Josuke Higashikata', 'image': 'josuke_jjl.JPG', 'anime': False},
	{'name': 'Josuke Higashikata (Go Beyond)', 'image': 'josuke_go_beyond.JPG', 'anime': False},
	{'name': 'Tooru', 'image': 'tooru.JPG', 'anime': False},
	{'name': 'Yasuho Hirose', 'image': 'yasuho.JPG', 'anime': False},
	{'name': 'Rai Mamezuku', 'image': 'rai.JPG', 'anime': False},
	{'name': 'Joshu Higashikata', 'image': 'joshu.JPG', 'anime': False},
	{'name': 'Daiya Higashikata', 'image': 'daiya.JPG', 'anime': False},
	{'name': 'Tsurugi Higashikata', 'image': 'tsurugi.JPG', 'anime': False},
	{'name': 'Hato Higashikata', 'image': 'hato.JPG', 'anime': False},
	{'name': 'Mitsuba Higashikata', 'image': 'mitsuba.JPG', 'anime': False},
	{'name': 'Jobin Higashikata', 'image': 'jobin.JPG', 'anime': False},
	{'name': 'Kaato Higashikata', 'image': 'kaato.JPG', 'anime': False},
	{'name': 'Norisuke Higashikata IV', 'image': 'norisuke_higashikata_IV.JPG', 'anime': False},
	{'name': 'Kei Nijimura', 'image': 'kei.JPG', 'anime': False},
	{'name': 'Iwasuke', 'image': 'iwasuke.JPG', 'anime': False},
	{'name': 'Ojiro Sasame', 'image': 'ojiro.JPG', 'anime': False},
	{'name': 'Yotsuyu Yagiyama', 'image': 'yotsuyu.JPG', 'anime': False},
	{'name': 'Aisho Dainenjiyama', 'image': 'aisho.JPG', 'anime': False},
	{'name': 'Karera Sakunami', 'image': 'karera.JPG', 'anime': False},
	{'name': 'A. Phex Brother (Schott Key No.1)', 'image': 'a_phex_1.JPG', 'anime': False},
	{'name': 'A. Phex Brother (Schott Key No.2)', 'image': 'a_phex_2.JPG', 'anime': False},
	{'name': 'Yoshikaga Kira (JoJolion)', 'image': 'kira_jjl.JPG', 'anime': False},
	{'name': 'Holy Joestar-Kira', 'image': 'holy_kira.JPG', 'anime': False},
	{'name': 'Josefumi Kujo', 'image': 'josefumi.JPG', 'anime': False},
	{'name': 'Tamaki Damo', 'image': 'damo.JPG', 'anime': False},
	{'name': 'Milagro Man', 'image': 'milagro_man.JPG', 'anime': False},
	{'name': 'Dolomite', 'image': 'dolomite.JPG', 'anime': False},
	{'name': 'Urban Guerrilla', 'image': 'urban_guerrilla.JPG', 'anime': False},
	{'name': 'Doremifasolati Do', 'image': 'doremi.JPG', 'anime': False},
	{'name': 'Poor Tom', 'image': 'poor_tom.JPG', 'anime': False},
	{'name': 'Wu Tomoki', 'image': 'wu.JPG', 'anime': False},
	{'name': 'Dododo De Dadada', 'image': 'dododo.JPG', 'anime': False},
	{'name': 'Obladi Oblada', 'image': 'obladi_oblada.JPG', 'anime': False},
	{'name': 'Joseph Joestar (JoJolion)', 'image': 'joseph_joestar_jjl.JPG', 'anime': False},
	{'name': 'Radio Gaga', 'image': 'radio_gaga.JPG', 'anime': False},
	{'name': 'Flashback Man', 'image': 'flashback_man.JPG', 'anime': False},
	{'name': 'Bling Baby', 'image': 'bling_baby.JPG', 'anime': False},
	{'name': 'Taoka', 'image': 'pangea_land.JPG', 'anime': False},
	# The JoJoLands
	{'name': 'Jodio Joestar', 'image': 'jodio.JPG', 'anime': False},
	{'name': 'Dragona Joestar', 'image': 'dragona.JPG', 'anime': False},
	{'name': 'Paco Lovelantes', 'image': 'paco.JPG', 'anime': False},
	{'name': 'Usagi Alohaoe', 'image': 'usagi.JPG', 'anime': False},
	{'name': 'Meryl Mei Qi', 'image': 'meryl.JPG', 'anime': False},
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
	post_text = characters[first_character]['name'] + ' VS ' + characters[second_character]['name']
	if characters[first_character]['anime'] == False or characters[second_character]['anime'] == False:
		post_text = post_text + ' #JoJoVSManga'
	status = postMatchUp(post_text, 'characters/' + characters[first_character]['image'], 'characters/' + characters[second_character]['image'])

createMatchUp()