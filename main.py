import re, os, time
from func.dates import CHAT_ID,DEAD, APROVED,TEXT
from func.SendMsg import SendMsg ,scrapp_ccs,TOKEN,chk_bin
from telethon.sync import TelegramClient, events


# Obtener las variables del entorno
API_ID = 20230546
API_HASH = '687aa22188883fd3d995a41c928454fe'
PHONE_NUMBER = '+18298501406'

client = TelegramClient('new_session', API_ID, API_HASH)

# Iniciar sesión automáticamente con el código de verificación
client.start(phone=PHONE_NUMBER)

@client.on(events.MessageEdited())
async def handler(event):
    ini = time.perf_counter()
    class EventMsg:
        def __init__(self):
            self.getMsg = event.message.message.upper()  
            self.RexGex = r'\d{14,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}'
            self.ScrCss = re.sub(self.RexGex, r'<code>\g<0></code>', self.getMsg)

        def Run(self):
            if (re.search(self.RexGex, self.getMsg) and any(live in self.getMsg for live in DEAD) == True): 
                ccs = scrapp_ccs(self.ScrCss)
                return '[⌁] - Dead ❌'
            else:
                try:
                    if (re.search(self.RexGex, self.getMsg) and any(live in self.getMsg for live in APROVED) == True): 
                        ccs = scrapp_ccs(self.ScrCss)
                        bins = chk_bin(ccs[0][0:6])
                        fin = time.perf_counter() - ini
                        self.text = TEXT.format(
                            bins[0], bins[1], bins[2],
                            ccs[0], 
                            ccs[1], 
                            ccs[2], 
                            ccs[3],
                            ccs[0][0:6],
                            bins[3], bins[4], bins[5], bins[6],
                            f'{fin:0.4f}'
                        )
                        SendMsg().enviar(self.text)
                        return '[⌁] - Aprovada ✅'
                except Exception as e:
                    print(f"Error: {e}")

    ResP = EventMsg().Run()
    print(ResP)

os.system("clear||cls")

print('run scrapp sexo')

client.run_until_disconnected()
