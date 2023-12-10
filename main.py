import requests
import socket
from colorama import Fore
def check_proxy(ip, port):
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"https://{ip}:{port}",
    }

    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=2)
        if response.status_code == 200:
            print(f"Proxy {ip}:{port} Valid!")
        else:
            print(f"Proxy {ip}:{port} Invalid.")
    except requests.RequestException:
        print(f"Proxy {ip}:{port} Invalid.")

def read_proxy_list(file_path):
    try:
        with open(file_path, "r") as file:
            proxies = file.readlines()
        return [proxy.strip() for proxy in proxies]
    except FileNotFoundError:
        print("File Not Found.")
        return []

def main():
    print(Fore.GREEN +"""    
________$________
_______$_$_______
______$___$______
_____$_____$_____
____$_______$____
____$_______$____
____$_______$____
____$_______$____
____$_______$____
____$_______$____
____$_______$____
____$_______$____
____$_______$____
___$__$___$__$___
__$__$_$_$_$__$__
_$__$__$$$__$__$_
_$$$____$____$$$_
_$______$______$_
$_______$_______$
RexProxyChecker
    """)
    file_path = input(Fore.WHITE + "Proxy File Path: ")
    proxy_list = read_proxy_list(file_path)

    for proxy in proxy_list:
        try:
            ip, port = proxy.split(":")
            check_proxy(ip, port)
        except ValueError:
            print(f"Invalid proxy format: {proxy}")

if __name__ == "__main__":
    main()
