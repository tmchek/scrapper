import requests,re, time
from func.dates import ( CHAT_ID,
                            TOKEN,
                          )

class SendMsg:
    def __init__(self):
        self.chat_id = CHAT_ID
        self.token   = TOKEN
        self.photo   = 'https://imgur.com/a/glNoeSE' #FOTO AL ENVIAR LA IMAGEN
        
    def enviar(self,texto: str = None):
        self.url = 'https://api.telegram.org/bot'+self.token
        self.psot = self.url+ f'/sendPhoto?chat_id={self.chat_id}&photo={self.photo}&caption='+texto+'&parse_mode=HTML'
        self.req = requests.get(self.psot)
        return True



def scrapp_ccs(text):

    if "|" in text:
        x = re.findall(r'\d+', text)

        if len(x[0]) < 16 :
            x.remove(x[0])
            if len(x) == 0:
                print(f'[⌁] - No Detectada ❌')
                return
            if len(x) == 1:
                print(f'[⌁] - No Detectada ❌')
                return
            elif len(x) == 2:
                print(f'[⌁] - Incomplet ccs ❌')
                return
            elif len(x) == 3:
                print(f'[⌁] - CVV Incomplet ❌')
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return

            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:
                print(f'[⌁] - Invalid Ccs ❌')
                return
            if len(yy) == 2:
                yy = '20'+yy

        
            return [cc, mm, yy, cvv]
        else:
            
            if len(x) == 0:
                print(f'[⌁] - No Detectada ❌')
                return
            if len(x) == 1:
                print(f'[⌁] - No Detectada ❌')
                return
            elif len(x) == 2:
                print(f'[⌁] - Incomplet ccs ❌')
                return
            elif len(x) == 3:
                print(f'[⌁] - CVV Incomplet ❌')
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return

            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:
                print(f'[⌁] - Invalid Ccs ❌')
                return
            if len(yy) == 2:
                yy = '20'+yy

        
            return [cc, mm, yy, cvv]


def chk_bin(bin):

    rs = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()
    if 'not found.' in rs: return None
    else:
        con = rs['country']
        country = rs["country_name"]
        flag = rs["country_flag"]
        bank = rs["bank"]
        brand = rs["brand"]
        type = rs["type"]
        level = rs["level"]

        return con,country, flag, brand, type, level,bank
