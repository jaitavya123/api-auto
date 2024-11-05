from configparser import ConfigParser

def read_var12():
 fetch_var= ConfigParser()
 fetch_var.read('C:/Users/LENOVO/VScodeProjects/addBook_api/universal_var/var1.ini')   # eith full path or ../f1/va.ini
 #print(fetch_var['API']['url'])
 return fetch_var

#read_var1()