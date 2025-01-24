#-------------CUENTA DE TELEGRAM-------------
API_ID   = 28891042
CHAT_ID  = -1002236856232
NUMERO   = "+52 4343113586"
API_HASD = "ea8c8d3861826dce706fa5a5017b38d2"
TOKEN    = "7887415954:AAFtY_A4XkG9nEKStYhK-DGp1pCqPTTmHUg" 

DEAD = ['❌']
#--------------PALABRAS CLAVES PARA EL SCAM---------------
APROVED = [
    ' CVV2 Mismatch'
    'Approved',
    'Charged $1',
    'Transaction approved.0 - Authorised',
    'Transaction declined.24 - CVC Declined',
    'Transaction declined.12 - Not enough balance',
    ' Approved! ✅',
    'CVV_FAILURE',
    '𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅',
    'APPROVED',
    '𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫',
    '𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 𝑪𝑪𝑵 ✅',
    '2010 Card Issuer Declined CVV',
    '𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅',
    'avs_and_cvv: Gateway Rejected: avs_and_cvv',
    ' CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number. CVV: [N] | AVS: [NNN]',
    '𝑪𝑽𝑪 -» unavailable - ⚜️ 𝑨𝑽𝑺 -» unavailable',
    'Approved! ✅',
    'Approved (1000)',
    'AA : AVS NOT MATCH: ZIP',
    'Card Issuer Declined CVV (2010)',
    '20051: Insufficient Funds',
    'C2 : CVV2 DECLINED',
    '[ APPROVED 🟩 ] ',
    ' Approved!🟩 ',
    'Charged $49.71',
    'Verified (85: NO REASN TO DECL) CVV: [M] | AVS: [XXN]',
    'cardCvv (INVALID_SECURITY_CODE)',
    'CVV2 Mismatch',
    'Security code was not matched by the processor',
    'Charged $5.31',
    'AVS check failed CVV: N | AVS: N'
    'Not Funds \ Transaction Normal - Insufficient Funds',
    "Your card's security code is incorrect.",
    'Verified',
    ' 𝑪𝒉𝒂𝒓𝒈𝒆𝒅 9$ ✅',
    'The transaction has been declined because of an AVS mismatch. The address provided does not match billing address of cardholder.(27)',
    'credit card zip code mismatch',
    'succeeded',
    'Subscription Complete',
    'APPROVED! ✅',
    '𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅',
    'APPROVED! ✅',
    'APPROVED AUTH✅',
    'APPROVED',
    '𝒔𝒕𝒂𝒕𝒖𝒔 = 𝒔𝒖𝒄𝒄𝒆𝒆𝒅𝒆𝒅 '
    ' ↯ [ insufficient funds ✅ ]'
    'insufficient funds ✅'
    'insufficient funds ✅'
    ]

#--------------PLANTILLA DEL SCRAPPER--------------

TEXT = '''[⌁] 𝗡𝗲𝘄 𝗖𝗮𝗿𝗱  <code>{}|{}|{}</code>

 𝗖𝗰 :         <code>{}</code>
 𝗙𝗲𝗰𝗵𝗮 :   <code>{}/{}</code>
 𝗖𝘃𝘃 :        <code>{}</code>

 𝗘𝘅𝘁𝗿𝗮 :   <code>{}xxxx</code>
 𝗦𝘁𝗮𝘁𝘂𝘀 :  <b>APPROVED! ✅</b>

 𝗕𝗿𝗮𝗻𝗱: <code>{} | {}</code>
 𝗟𝗲𝘃𝗲𝗹: <code>{}</code>
 𝗕𝗮𝗻𝗸: <code>{}</code>

 𝗧𝗶𝗺𝗲:   <code>{}(sg)</code>
 𝗢𝘄𝗻𝗲𝗿 𝗜𝗗:  <code>-7572963291-</code>
 𝗢𝘄𝗻𝗲𝗿 :  @Umbrlla_Chk'''



