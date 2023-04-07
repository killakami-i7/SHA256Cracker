from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid Arguments!")
    print(f">> {sys.argv[0]} <sha256sum>")

uncracked_hash = sys.arg[1]
print(f"Attempting to crack {uncracked_hash}")

password_file = "rockyou.txt"
attempts = 0

with open(password_file, "r", encoding="latin-1") as pwd_lst:
    for pwd_attempt in pwd_lst:
        pwd_attempt = pwd_attempt.strip("\n").encode("latin-1")

        pwd_hash = sha256sumhex(pwd_attempt)

        if pwd_hash == uncracked_hash:
            print(f"Cleartext Passwd: {pwd_attempt}")
            exit(0)
    print("Passwd Not Found")
    exit(1)
