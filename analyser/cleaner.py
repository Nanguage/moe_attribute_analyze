from bs4 import BeautifulSoup
import os

file_list = os.listdir("../datas")
files_num = len(file_list)
if not os.path.exists("./cleaned_datas"):
    os.mkdir("./cleaned_datas")
count = 0
for file_name in file_list:
    count += 1
    print("[INFO]cleaning %s(%d/%d)"%(file_name, count, files_num))
    file = open("../datas/"+file_name, "r")
    content = file.read()
    file.close()
    soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
    try:
        for script in soup.find_all("script"):
            script.replace_with("")
    except:
        print("[INFO]junk(script) not found!")
    try:
        soup.find("div", class_="searchaux").replace_with("")
    except:
        print("[INFO]junk not found!")
    cleaned_file = open("./cleaned_datas/"+file_name, "w")
    cleaned_file.write(str(soup))
    cleaned_file.close()
print("Done! :)")