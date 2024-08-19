import os
import subprocess
import requests

# ASCII Art
ascii_art = r"""
  _____  ____                 ____        ___        
 |  __ \|  _ \               |___ \      / _ \       
 | |__) | |_) |  ______   _ __ __) | ___| | | |_ __  
 |  _  /|  _ <  |______| | '__|__ < / __| | | | '_ \ 
 | | \ \| |_) |          | |  ___) | (__| |_| | | | |
 |_|  \_\____/ v.1.0.3   |_| |____/ \___|\___/|_| |_| by rootbakar
"""

# Print ASCII art
print(ascii_art)                                                    

def send_message(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

def send_document(bot_token, chat_id, document_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    files = {"document": open(document_path, "rb")}
    data = {"chat_id": chat_id}
    requests.post(url, files=files, data=data)

def run_command(command):
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def run_recon1(domain):
    run_command(f"echo {domain} | nuclei -silent -t ~/nuclei-templates/http/vulnerabilities/wordpress -o wpscann-{domain}-nuclei.txt")

def run_recon2(domain):
    run_command(f"echo {domain} | gau --subs --blacklist png,jpg,gif,jpeg,swf,woff,svg,pdf,css,webp,woff,woff2,eot,ttf,otf,mp4 | urldedupe -s | gf lfi redirect sqli-error sqli ssrf ssti xss xxe | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result1-{domain}.txt")

def run_recon3(domain):
    run_command(f"echo {domain} | gau --subs --blacklist png,jpg,gif,jpeg,swf,woff,svg,pdf,css,webp,woff,woff2,eot,ttf,otf,mp4 | urldedupe -s | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result2-{domain}.txt")

def run_recon4(domain):
    run_command(f"echo {domain} | waybackurls | urldedupe -s | gf lfi redirect sqli-error sqli ssrf ssti xss xxe | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result3-{domain}.txt")

def run_recon5(domain):
    run_command(f"echo {domain} | waybackurls | urldedupe -s | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result4-{domain}.txt")

def run_recon6(domain):
    run_command(f"echo {domain} | gauplus | urldedupe -s | gf lfi redirect sqli-error sqli ssrf ssti xss xxe | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result5-{domain}.txt")

def run_recon7(domain):
    run_command(f"echo {domain} | gauplus | urldedupe -s | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result6-{domain}.txt")

def run_recon8(domain):
    run_command(f"paramspider -d {domain} ")
    run_command(f"cat results/{domain} | urldedupe -s | gf lfi redirect sqli-error sqli ssrf ssti xss xxe | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result7-{domain}.txt")

def run_recon9(domain):
    run_command(f"paramspider -d {domain} ")
    run_command(f"cat results/{domain} | urldedupe -s | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result7-{domain}.txt")

def run_recon10(domain):
    run_command(f"echo {domain} | httpx -silent | katana -silent | urldedupe -s | gf lfi redirect sqli-error sqli ssrf ssti xss xxe | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result9-{domain}.txt")

def run_recon11(domain):
    run_command(f"echo {domain} | httpx -silent | katana -silent | urldedupe -s | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result10-{domain}.txt")

def run_recon12(domain):
    run_command(f"echo {domain} | httpx -silent | hakrawler -subs -u | urldedupe -s | gf lfi redirect sqli-error sqli ssrf ssti xss xxe | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result11-{domain}.txt")

def run_recon13(domain):
    run_command(f"echo {domain} | httpx -silent | hakrawler -subs -u | urldedupe -s | qsreplace FUZZ | grep FUZZ | nuclei -silent -t ~/nuclei-templates/dast/vulnerabilities -dast -o result12-{domain}.txt")

def run_recon14(domain):
    run_command(f"echo {domain} | nuclei -silent -t ~/nuclei-templates/http/exposures -o exposures-{domain}.txt")

def run_recon15(domain):
    run_command(f"echo {domain} | nuclei -silent -t ~/nuclei-templates/http/exposed-panels -o exposed-panels-{domain}.txt")

def run_recon16(domain):
    run_command(f"echo {domain} | nuclei -silent -t ~/nuclei-templates/http/default-logins/ -o default-logins-1-{domain}.txt")

def run_recon17(domain):
    run_command(f"echo {domain} | nuclei -silent -t ~/nuclei-templates/default-logins -o default-logins-2-{domain}.txt")

def run_generate(domain):
    run_command(f"cat wpscann-{domain}-nuclei.txt result1-{domain}.txt result2-{domain}.txt result3-{domain}.txt result4-{domain}.txt result5-{domain}.txt result6-{domain}.txt  result7-{domain}.txt result8-{domain}.txt result9-{domain}.txt result10-{domain}.txt result11-{domain}.txt result12-{domain}.txt exposures-{domain}.txt exposed-panels-{domain}.txt default-logins-{domain}.txt | anew final-result-{domain}.txt")
    run_command(f"mkdir {domain}")

def delete_temp_files(domain):
    run_command(f"rm -fR wpscann-{domain}-nuclei.txt result1-{domain}.txt result2-{domain}.txt result3-{domain}.txt result4-{domain}.txt result5-{domain}.txt result6-{domain}.txt  result7-{domain}.txt result8-{domain}.txt result9-{domain}.txt result10-{domain}.txt result11-{domain}.txt result12-{domain}.txt exposures-{domain}.txt exposed-panels-{domain}.txt default-logins-1-{domain}.txt default-logins-2-{domain}.txt output")
    run_command(f"rm -f results/{domain}.txt")
    run_command(f"mv final-result-{domain}.txt {domain}")

# Replace with your bot token
BOT_TOKEN = "xxx:xxxxxxxxxxxx"

# Replace with your chat ID
CHAT_ID = "xxxxx"

domain = input("Enter the domain (without http/https): ")

# Send initial message
send_message(BOT_TOKEN, CHAT_ID, f"Starting scann for {domain}, happy hunting...")

# SUBDOMAIN SCANNING
print("\n\033[92m[*] Start nuclei template /http/vulnerabilities/wordpress ...")
run_recon1(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with gau, gf, qsreplace) ...")
run_recon2(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with gau, qsreplace) ...")
run_recon3(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with waybackurls, gf, qsreplace) ...")
run_recon4(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with waybackurls, qsreplace) ...")
run_recon5(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with gauplus, gf, qsreplace) ...")
run_recon6(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with gauplus, qsreplace) ...")
run_recon7(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with paramspider and gf) ...")
run_recon8(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with paramspider) ...")
run_recon9(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with katana, gf, qsreplace) ...")
run_recon10(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with katana, qsreplace) ...")
run_recon11(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with hakrawler, gf, qsreplace) ...")
run_recon12(domain)

print("\033[92m[*] Start nuclei template /dast/vulnerabilities (with hakrawler, qsreplace) ...")
run_recon13(domain)

print("\033[92m[*] Start nuclei template /http/exposures ...")
run_recon14(domain)

print("\033[92m[*] Start nuclei template /http/exposed-panels ...")
run_recon15(domain)

print("\033[92m[*] Start nuclei template /http/default-logins ...")
run_recon16(domain)

print("\033[92m[*] Start nuclei template /default-logins ...")
run_recon17(domain)

# GENERATE FILE SUBDOMAIN SCANNING
print("\033[92m[*] Generate Final Nuclei Result ...")
run_generate(domain)

# Send subdomain scanning result message
send_message(BOT_TOKEN, CHAT_ID, f"Nuclei final result for {domain} finish and save to final-result-{domain}.txt")

# Send subdomain scanning result file
send_document(BOT_TOKEN, CHAT_ID, f"final-result-{domain}.txt")

# DELETE TEMP FILES
print("\033[92m[*] Deleting temp files...")
delete_temp_files(domain)

# SCAN FINISH
print("\033[92m[*] Scan is completed - Happy Hunting.")
send_message(BOT_TOKEN, CHAT_ID, f"Scanning for domain {domain} has been finished, happy hunting...")
