import os
import ctypes

# Define the URLs you want to redirect and their corresponding IP addresses
redirects = {
    "Xvideos.com": "127.0.0.1",
    "pornhub.com": "127.0.0.1",
    "xnxx.com": "127.0.0.1",
    "xhamster.com": "127.0.0.1",
    "realsrv.com": "127.0.0.1",
    "stripchat.com": "127.0.0.1",
    "spankbang.com": "127.0.0.1",
    "chaturbate.com": "127.0.0.1",
    "xhammster18.desi": "127.0.0.1",
    "onlyfans.com": "127.0.0.1",
    "twinrdsrv.com": "127.0.0.1",
    "livejasmin.com": "127.0.0.1",
    "dmm.co.jp": "127.0.0.1",
    "youporn.com": "127.0.0.1",
    "xhamsterlive.com": "127.0.0.1",
    "bongacams.com": "127.0.0.1",
    "eporner.com": "127.0.0.1",
    "xvideos2.com": "127.0.0.1",
    "for-j.com": "127.0.0.1",
    "noodlemagazine.com": "127.0.0.1",
    "nhentai.net": "127.0.0.1",
    "ixxx.com": "127.0.0.1",
    "redtube.com": "127.0.0.1",
    "cityheaven.net": "127.0.0.1",
    "missav.com": "127.0.0.1",
    "rule34.xxx": "127.0.0.1",
    "xnxx.tv": "127.0.0.1",
    "crjpgate.com": "127.0.0.1",
    "tnaflix.com": "127.0.0.1",
    "xlivrdr.com": "127.0.0.1",
    "xvideos.es": "127.0.0.1",
    "dlsite.com": "127.0.0.1",
    "hqporner.com": "127.0.0.1",
    "youjizz.com": "127.0.0.1",
    "txxx.com": "127.0.0.1",
    "xvideos3.com": "127.0.0.1",
    "xxxnewvideos.com": "127.0.0.1",
    "ok.xxx": "127.0.0.1",
    "xnxx115.com": "127.0.0.1",
    "nutaku.net": "127.0.0.1",
    "sxyprn.com": "127.0.0.1",
    "brazzenetwork.com": "127.0.0.1",
    "superchatlive.com": "127.0.0.1",
    "theporndude.com": "127.0.0.1",
    "fapello.com": "127.0.0.1",
    "hitomi.la": "127.0.0.1",
    "erome.com": "127.0.0.1",
    "kiynew.com": "127.0.0.1",
    "xhamster.desi": "127.0.0.1",
    "jerkmate.com": "127.0.0.1",
    "sex.com": "127.0.0.1"
}

# Define the path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Check if the current user has administrative privileges
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("This script must be run as an administrator.")
    exit()

# Open the hosts file in append mode
with open(hosts_path, "a") as file:
    # Add each URL and its IP address to the hosts file
    for url, ip in redirects.items():
        file.write(f"{ip}\t{url}\n")

# Flush the DNS cache to apply the changes
os.system("ipconfig /flushdns")

print("Hosts file updated successfully!")
