import translators as ts
import time
import re

#[SETTINGS]
service = "google" #example: Google, Bing, Yandex, Baidu, Alibaba
translate_to = "fr"
#modes:
# - non_latin_alphabet_only (example: will translate all messages in Cyrillic to the desired language.)
# - all_messages (all messages will be translated but you will reach the per-hour translation limit of the chosen API more quickly.)
mode = "non_latin_alphabet_only"
cs2_path = 'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\console.log'


#Translation
def translate(player, message):
    if mode == "non_latin_alphabet_only":
        if re.search(r"[\u0400-\u04FF]", message):
            print(player, ":", ts.translate_text(message, translator=service, to_language=translate_to), "[translated]")
        else:
            print(player, ":", message)
    else:
        print(player, ":", ts.translate_text(message, translator=service, to_language=translate_to))

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for line in reversed(lines):
            if " : " in line:
                message = line.split(" : ", 1)[1].strip()

                if "] " in line:
                    player = line.split("] ", 1)[1].split(" : ", 1)[0].strip()
                
                global already_translate
                if f"{player} : {message}" != already_translate:
                    already_translate = f"{player} : {message}"
                    translate(player, message)
                    return
                else:
                    return

    except FileNotFoundError:
        print(f"Console.log not found.")
    except Exception as err:
        pass

open(cs2_path, 'w').close()
already_translate = ""

#Loop
while True:
    try:
        read_file(cs2_path)
        time.sleep(1)
    except Exception as err:
        pass

