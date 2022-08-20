import sqlite3
import sys

notepad = False

def reg():
     def enter_(a, c, b):
          if a == "" or a == " " or a == "  ":
               print(b, "can't be left empety")
               return enter_(input(c), c, b)
               
          else:
               return a     
     conn = sqlite3.connect("company.db")
     print("Opened database successfully")
     cursor = conn.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS password_store
              (NAME           TEXT    NOT NULL,
              PASSWORD            TEXT     NOT NULL,
              ENTERED       TEXT      NOT NULL);''')
     print("Table created successfully")
     
     e_name = enter_(input("Name: "), "Name: ", "Name ")
     e_pass = enter_(input("Pasword: "), "Password: ", "Password")
     info = note(e_name, e_pass)
     
     cursor.execute('''INSERT INTO password_store (NAME, PASSWORD, ENTERED)VALUES (?,?,?)''', (e_name, e_pass, info))
     conn.commit()
     
def log():
     try:
          con = sqlite3.connect("company.db")
          namec = input("Name: ")
          name = ""
          cur = con.cursor()
          abc = True
          abd = True
          for row in cur.execute('SELECT * FROM password_store'):
               print(row)
               name = row[0]
               passw = row[1]
               enter = row[2]
               if namec == name:
                    passwc = input("Password: ")

                    if passwc == passw:
                         print("Account Found")
                         print("Your Text")
                         print(enter)
                         abc = False
                         break                         

                    else:
                         print("Incorrect Password")
                         continue
                    
               else:
                    abd = True
          con.close()
          if abc == True and abd == True:
               print("No Such Account Found Named", namec)
          else:
               pass
     except:
          print("unable to found (Database), please try to login first")

def note(name, passw):
     print("YOU ENTERED PERSONAL WRITEPAD")
     print("    (Write 'q' to [q]uit)")
     texte = ""
     while True:
          entry = input(">")
          if entry.lower() == "q":

               break
          texte = (texte +"\n >    " + entry)
     print(texte)
     return texte
     
while True:
     che = input("Press 'L' to [L]ogin or 'R' to [R]egister or 'E' to [E]xit \n")
     if che == 'l' or che == 'L':
          log()

     elif che == 'r' or che == 'R':
          reg()

     elif che == 'e' or 'E':
          sys.exit()
     else:
          print("Unknown Keyword, Please Try Again")

