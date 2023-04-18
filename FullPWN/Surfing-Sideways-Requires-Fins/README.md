# Surfing Sideways Requires Fins
## By: S1n1st3r

### Notes
 - Got SQLi to work through middlware, sqlmap cmd: sqlmap -u "http://172.22.160.1:8082/?id=1" --level 1  --risk 3 --time-sec=1 --dbms=SQLite -dbs


## Steps

1. SSRF through a vulnerable internet down detector
2. Use the SSRF to access the internal admin panel. Will need to format IP address without periods or localhost. (ex: 2130706433)
3. There is a SQL injection in the admin panel's url arguments and it is possible to get hashed passwords, if exploited through the SSRF.
4. Password is crackable by rockyou and the username is admin.
5. login through ssh as admin and get the user flag.
6. admin user can run /tmp/lister and its a setuid binary.
7. /tmp/lister is a binary that can be exploited through path injection, as it only calls ls and not the absolute path.
8. exploit to get root flag.


## Hints

1: The filter might only be checking for '.'s on the backend. Find a way to reach localhost without them
2: You might want to create a middleware to inject
3: There is more than one type of injection, and some can be used for privilege escalation

## Flags

User: SummitCTF{1nject10n_thr0u5h_55RF_1s_4w3s0m3} 

Root: SummitCTF{G00D_A7_CL1MB!N6_Y0U_@R3}
