# KOTH Machine 1: Everest
## Created by: S1n1st3r

## Notes

## TODO
 
 - Ensure raw data on 56789 works [x]
 - Ensure HTTP works [x]
 - Ensure SMB works [x]
 - Hide txt file with npurja plaintext password (or a new user)
 - Add unrestricted file upload vuln to success.php [x]
 - Restrict access to success.php to those who logged in [x]
 - ensure config.php cant be reached from external through browser [x]
 - Hide more flags [x]
 - Add more priv esc routes [x]

## Paths
1: https://github.com/itsecurityco/CVE-2022-22965 on port 8080

2: Find file share with user login to get into login page that has unrestricted file upload (need to add the vuln here)

3: raw data has id-rsa private key on port 54321 for user npurja

4: (Need to do) hide plaintext password somewhere for npurja. It already is in config.php

5: plaintext user and pass in environment variables for user npurja (can view in info.php)

6: Guess the correct number 1-20 on port 11111 to get a shell as root

PrivEscs:

 - /tmp/suidney - setUID
 - /var/ps - path injection
 - can run /usr/bin/gdb without password with sudo
 - Guess the correct number 1-20 on port 11111 to get a shell as root

### Flags
Flag 1 (success.php):
SummitCTF{W3lc0me_T0_7he_b3g1nn1ng!!}

Flag 2 (envs):
SummitCTF{Alw4ys_st4y_ch3ck1ng_7he_env1ronm3nt_v4r14bl3s!}

Flag 3 (user.txt):
SummitCTF{Whos_th33_K1ng_N0w?!?}

Flag 4 (/var/log):
SummitCTF{y0r_g00d_a7_H1de_n_S33k}

Flag 5 (/root/root.txt):
SummitCTF{I_4m_gROOT!!}

Flag 6 (/root/.flg):
SummitCTF{H1d1ng_in_pl8n_s1ght_h3h3}
