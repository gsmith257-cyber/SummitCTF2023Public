# KOTH Machine 2: Caesar's Mountain Part 1
## Created by: QAZWSX

## Paths
1: Unrestricted file upload on port 80

2: Mysql user/user login has access to a table containing Caesar's creds

3: Backdoor in /admin/backdoor.html which returns a www-data connection on port 8081

4: Weak ssh password for user mountaineer (brute forceable)

PrivEscs:

 - vi can be run as root
 - /tmp/script.py can be edited and run as python

### Flags (all flags in base64 to make find command harder)
Flag 1 (/var/www/html/flag.txt):
FhzzvgPGS{1_y0i3_gu3_z0hag41a5}
SummitCTF{1_l0v3_th3_m0unt41n5}

Flag 2 (/var/www/html2/admin/flag.txt):
FhzzvgPGS{o4px_fg4oo3q_4t41a}
SummitCTF{b4ck_st4bb3d_4g41n}

Flag 3 (/tmp/flag.txt):
FhzzvgPGS{u1tu3fg_0a_p4rf4ef_z0hag41a}
SummitCTF{h1gh3st_0n_c4es4rs_m0unt41n}

Flag 4 (/home/mountaineer/flag.txt):
FhzzvgPGS{1_j1yy_a3i3e_s0et3g_gu1f}
SummitCTF{1_w1ll_n3v3r_f0rg3t_th1s}

Flag 5 (/home/caesar/user.txt):
FhzzvgPGS{p4rf4ef_y0fg_u1f_u0z3}
SummitCTF{c4es4rs_l0st_h1s_h0m3}

Flag 6 (/root/root.txt):
FhzzvgPGS{gu3_z0hag41a_1f_z1a3}
SummitCTF{th3_m0unt41n_1s_m1n3}

Flag 7 (mysql)
FhzzvgPGS{Zl5DY_15_4j3f0z3}
SummitCTF{My5QL_15_4w3s0m3}