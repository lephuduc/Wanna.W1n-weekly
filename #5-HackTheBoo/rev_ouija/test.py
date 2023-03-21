from pwn import *
import string
d = string.ascii_lowercase + string.ascii_uppercase
x = b'ZLT{Svvafy_kdwwhk_lg_qgmj_ugvw_escwk_al_wskq_lg_ghlaearw_dslwj!}'
#rot8 la ra
from Crypto.Util.number import long_to_bytes as ltb
print(ltb(1))