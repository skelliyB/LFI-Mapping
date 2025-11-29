import requests
import os
import platform
from colorama import Fore, init
import argparse


init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description='to use -u is your url and -p is your payload if you need more help do --help or -h :)')
    parser.add_argument('-u', '--Url',help="your site that your using")
    parser.add_argument('-p', '--payload', help="your payload (WHOLE file directory :3 )")
    args = parser.parse_args()

    print(rf''' _                                                                         _ 

|_|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_|
| |                                                                          
| |                                                                          
| |                                                                          
| |Site is [ {args.Url} ]                                                                          
|_|--------------------------------------------------------------------------                                                                          
| |                                                                          
| |                                                                          
| |Payload is [{args.payload}]                                                                          
| |--------------------------------------------------------------------------                                                                          
|_|                                                                          
| |                                                                          
| |                                                                          
| |                                                                          
| |                                                                          
|_|                                                                          
| |                                                                          
| |                                                                          
| |                                                                          
| |_____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____   
|_|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|  
|_____|_____|_____|_____|_____|    ''')

    
    avrg_size = []

    payloads = []




    if args.payload:
        try:
            with open(args.payload, 'r', encoding='utf-8', errors='replace') as f:
                payloads = [line.strip() for line in f if line.strip()]

        except FileNotFoundError as e:
            print(f' error file not found {args.p}')
            return
    
    if args.Url:

        for payload in payloads:
            fullurl = args.Url.rstrip('/') + '/' + payload

            try:
                responses = requests.get(fullurl, timeout=5)
                size_byte = len(responses.content)
                avrg_size.append(size_byte)

                if avrg_size:
                     avg = sum(avrg_size) / len(avrg_size)
                     if abs(size_byte - avg) > 50:
                         print(Fore.LIGHTBLUE_EX + f"{payload} ({size_byte}) looks different! :3")
                avrg_size.append(size_byte)


                if responses.status_code == 200:
                    print( Fore.LIGHTGREEN_EX + f'{payload}, {size_byte}')
                else:
                    print(Fore.RED + 'couldnt get to the site :(')

                

            except:
                print('ctrl + c stopped fuzzing :3')
                return

        



def banner():
    print(Fore.LIGHTGREEN_EX + r''' _     _____ ___ 
| |   |  ___|_ _|
| |   | |_   | | 
| |___|  _|  | | 
|_____|_|   |___|''')
    
    print(Fore.RED +''' _                __     
| |  _            \ \    
| |_| |_ _____ ____\ \   
| |_   _|_____|_____\ \  
| | |_|              \_\ 
|_|                    __
| |  _                / /
| |_| |_ _____ _____ / / 
| |_   _|_____|_____/ /  
| | |_|            /_/   
|_|                      ''')
    
    print(Fore.CYAN + '''--The size matters if its different than the other packets then thats most likely your file''')




if __name__ == "__main__":
    banner()
    main()
