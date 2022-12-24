#navbar replacer in html files
import os


path = os.getcwd() + "/"
navbar_source = "reusableElements/navbar.html"

NAVBAR_START = "<!-- nav -->"
NAVBAR_END = "<!-- /nav -->"

def read_navbar(path):
    file = open(path + navbar_source)
    return file.readlines()

def replace_navbar(navbar, filename):
    #replaces everything between <nav id="navbar> and </nav> with the "nav" string
    #ignores whitespaces

    #I am going to read the file line by line and lines one by one as well
    #files are short, so it shouldn't be too problematic to read them whole
    #into memory and rewriting them.

    file = open(filename)

    #0 means looking for "<nav"
    #1 means looking for "</nav"
    #2 means wrapping up
    state=0

    newfile_list = []
    for line in file.readlines():
        if state==0 and line.strip() == NAVBAR_START:
            print("Found start!")
            state=1
        elif state==1 and line.strip() == NAVBAR_END:
            print("Found end!")
            newfile_list+=navbar
            state=2
        elif state==0 or state==2: #state==0
            newfile_list+=[line]

    file.close()
    
    newfile = open(filename, "w")
    #newfile = open("copy_"+filename, "x")
    newfile.writelines(newfile_list)
    return

def list_navbar_files(path):
    lst = os.listdir(path);
    retlst=[]
    
    for f in lst:
        if(f.endswith(".html")):
            retlst+=[f]
    return retlst


for f in os.listdir(path):
    print(f)

print("\n\nTrimmed list:")
for f in list_navbar_files(path):
    print(f)

navbar_code = read_navbar(path)
for l in navbar_code:
    if(l.strip() == NAVBAR_START):
        print(l)
    if(l.strip() == NAVBAR_END):
        print(l)



for f in list_navbar_files(path):
    if f == navbar_source or f.startswith("copy"):
        continue
    print("Starting to process file: "+f)
    replace_navbar(navbar_code, f)
    print("Finished processing file: "+"copy_"+f)



