import re, os, time
from telethon.sync import ( TelegramClient,
                            events )

from func.SendMsg import ( 
                            SendMsg,
                            scrapp_ccs,
                            chk_bin
                             )

from func.dates import ( 
                         API_HASD,
                         API_ID,
                         NUMERO,
                         APROVED,
                         DEAD,
                         TEXT,
                         )


client = TelegramClient(f'ScrapAproved', API_ID, API_HASD)
client.start(NUMERO)


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


os.system("clear")
banner = """   

 _   _           _              _ _         _____                    
| | | |         | |            | | |       |_   _|                   
| | | |_ __ ___ | |__  _ __ ___| | | __ _    | | ___  __ _ _ __ ___  
| | | | '_ ` _ \| '_ \| '__/ _ \ | |/ _` |   | |/ _ \/ _` | '_ ` _ \ 
| |_| | | | | | | |_) | | |  __/ | | (_| |   | |  __/ (_| | | | | | |
 \___/|_| |_| |_|_.__/|_|  \___|_|_|\__,_|   \_/\___|\__,_|_| |_| |_|
                                                                     
                                                                     

 User:  
 Code by: 
"""

print(banner)

client.run_until_disconnected()
