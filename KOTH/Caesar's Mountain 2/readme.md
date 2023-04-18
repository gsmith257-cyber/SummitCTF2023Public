# KOTH Machine 2: Caesar's Mountain Part 2
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
FhzzvgPGS{u3tu_huu1i_4z4a4pg4_z0hag41af}
SummitCTF{h3gh_uhh1v_4m4n4ct4_m0unt41ns}

Flag 2 (/var/www/html2/admin/flag.txt):
FhzzvgPGS{0a3_s00g_q34c_1a_4t41a}
SummitCTF{0n3_f00t_d34p_1n_4g41n}

Flag 3 (/tmp/flag.txt):
FhzzvgPGS{gu3_g0c_u1yy_0s_p4f4ef_z0hag41a}
SummitCTF{th3_t0p_h1ll_0f_c4s4rs_m0unt41n}

Flag 4 (/home/mountaineer/flag.txt):
FhzzvgPGS{ge41a3q_s0e_l3nef_1a_gu3_p0z1a9_e41a}
SummitCTF{tr41n3d_f0r_y3ars_1n_th3_c0m1n9_r41n}

Flag 5 (/home/caesar/user.txt):
FhzzvgPGS{u15g0el_j111_a0g_s0et3g_u1f_q3fg1al}
SummitCTF{h15t0ry_w111_n0t_f0rg3t_h1s_d3st1ny}

Flag 6 (/root/root.txt):
FhzzvgPGS{gu1f_fhzz1g_1f_z1y3f_no0i3_gu3_e3fg}
SummitCTF{th1s_summ1t_1s_m1l3s_ab0v3_th3_r3st}

Flag 7 (mysql)
FhzzvgPGS{Zl5DY_15_P001}
SummitCTF{My5QL_15_C001}