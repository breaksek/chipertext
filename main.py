import os


# definisi wsrna
cyan = '\033[96m'
magenta = '\033[95m'
hijau = '\033[92m'
biru = '\033[94m'
reset = '\033[0m'

# banner tools

baru = f"""
  ┏━━━━━━⪻ RESULT ⪼━━━━━┓
  ┃ Plaintext   ┃ {plainttext}
  ┃ Kunci       ┃ {key_input}
  ┃ Chippert    ┃ {chippertext}
  ┗━━━━━━━━━━━━━━━━━━━━━┛
"""

banner = f"""{cyan}  ____ _     _                 _            _     _____           _       
 / ___| |__ (_)_ __   ___ _ __| |_ _____  _| |_  |_   _|__   ___ | |___   
| |   | '_ \| | '_ \ / _ \ '__| __/ _ \ \/ / __|   | |/ _ \ / _ \| / __|  
| |___| | | | | |_) |  __/ |  | ||  __/>  <| |_    | | (_) | (_) | \__ \  
 \____|_| |_|_| .__/ \___|_|   \__\___/_/\_\\\\__|   |_|\___/ \___/|_|___/  
              |_|                  {magenta}by breaksek{cyan}                            

{reset} [{hijau}info{reset}] Tools ini dibuat untuk tugas mata kuliah Keamanan Informasi      
 [{hijau}info{reset}] Tools ini menggunakan teknik vigenere angka                      
 [{hijau}info{reset}] Anggota : MUHAMMAD SYARIFUDDIN (2210651057) dan A.RIFALDI AMIN (2310651053)
"""


# function
def encrypt_vigenere_numbers(plaintext, key_numbers):
    ciphertext = ""
    key_len = len(key_numbers)
    key_index = 0

    plaintext = plaintext.upper()

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')
            k = key_numbers[key_index % key_len]
            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))
            key_index += 1
        else:
            # spasi atau karakter lain tetap, kunci tidak maju
            ciphertext += char

    return ciphertext

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    plaintext = input(f" [{biru}•{reset}] Masukkan plaintext : ")
    key_input = input(f" [{biru}•{reset}] Masukkan kunci (contoh: 2,8,15) : ")
    key_numbers = [int(x.strip()) for x in key_input.split(',')]
    ciphertext = encrypt_vigenere_numbers(plaintext, key_numbers)
    print(f" [{biru}•{reset}] Ciphertext :", ciphertext)
    print(baru)
