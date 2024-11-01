import base64

a = ['esOZTiPDsg==', 'bzfCkFfCtA==', 'ZmzDjHcn', 'PxLCm3LDvA==', 'IcKlVy9pw57DgMK3w6kmwpvCiUnDhcOKw4A=', 'LMKnwqECawEeEMOZQsK7wrLCscKpSG1AwqvDvjnDpMKhOSDCqQ…KVR/CgMK4w7PCukbCv8O8woNHXcK7SsOmMhHDnUEJw4lsw6g=', 'wrTDnltl', 'UMOXHRs=', 'Tz0lw48=', 'O8K0w5JcwrA=', 'w5DCpnx/LA==', 'HsKrS8KVQw==', 'dcKvfnkhUQ3DncOFIsOew5lHwr7CjcKYAsOuwrc3UjhfwopNwq…CnSIdw5jDtsKyWFBMwq4YMQvDhRrCrlBlw71LUR5HGMKwEBs=', 'w4RAw5xg', 'RkQSNA==', 'SsOsQztv', 'wonDvMOwwow=', 'wovDlMKvw5nCog==', 'w73Ch8K5VcK/', 'wpN7HsOMwpI=', 'w5/CuMKDacOKPcKoB3jDomQ=', 'wpnDvMOhwo0=', 'wp4xwrvDvA==', 'H1LDrhc=', 'wo86woHDm37Dow==', 'woY4wobDmg==', 'wr/CgMKQNcOo', 'ecOlUSF2S3fCsMKbGQ==', 'E3nCrcKe', 'w5d5w6HDnsOFw7RcRFjDosKsZ8OHEcOv', 'QMOXDBrCrcKLwp3DvA==', 'w5fDsiPDrsOf', 'V3c3A0Q=', 'E8OjwpNaP1lDTMKXcsO5', 'G08JPDZMw5s8w4ITw54dEMKAwps=', 'wo8pwoXDnmg=', 'wpo5wqvDoMOQw6Jd', 'bH4+TyM=', 'RcOhTDV1Ew==', 'McOVwqpRBg==', 'c8K/w43DvcK8', 'SsOrTCF1CVDCgcKLEsKc', 'NsK/w4Bc', 'G1TDpwk=', 'AcKtwqfDlW7Dsw==', 'e3kkcQJfwoNFDEU9', 'QMOXDBo=', 'w5bCsWlh', 'eWY6bg8=', 'FnbDoEvDtl1LUkB7w4Q=']
for i in range(len(a)):
    try:
        print(base64.b64decode(a[i]).decode('utf-8'))
    except:
        pass