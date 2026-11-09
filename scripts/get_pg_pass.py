import win32cred
import base64
import sqlite3
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.decrepit.ciphers.modes import CFB8

padding_string = b'}'
iv_size = AES.block_size // 8

def pad(key):
    if isinstance(key, str):
        key = key.encode()
    key = key[:32]
    if len(key) in (16, 24, 32):
        return key
    return key.ljust(32, padding_string)

def decrypt(ciphertext, key):
    # If ciphertext is hex encoded string of base64
    if isinstance(ciphertext, str):
        try:
            raw = bytes.fromhex(ciphertext)
            ciphertext = raw
        except:
            ciphertext = ciphertext.encode()
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:iv_size]
    cipher = Cipher(AES(pad(key)), CFB8(iv), default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext[iv_size:]) + decryptor.finalize()

cred = win32cred.CredRead(TargetName="pgAdmin4", Type=win32cred.CRED_TYPE_GENERIC)
raw_blob = cred['CredentialBlob']
print("CredentialBlob raw length:", len(raw_blob))

db_path = os.path.expanduser(r"~\AppData\Roaming\pgAdmin\pgadmin4.db")
con = sqlite3.connect(db_path)
cur = con.cursor()
row = cur.execute("SELECT password FROM server WHERE id=1").fetchone()
encrypted_password = row[0]

# Try decoding blob in different ways
for enc in ['utf-8', 'utf-16', 'raw']:
    try:
        k = raw_blob if enc == 'raw' else raw_blob.decode(enc)
        d = decrypt(encrypted_password, k)
        print(f"Decrypted with {enc}: {d}")
    except Exception as e:
        print(f"Failed with {enc}: {e}")
