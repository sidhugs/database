import pymongo
import webbrowser

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
mycol = mydb["customers"]

cust=[]

for x in mycol.find():
    a="<tr><td>%s</td>"%x["studid"]
    cust.append(a)
    b = "<td>%s</td>"%x['studname']
    cust.append(b)
    c = "<td>%s</td>"%x['studemail']
    cust.append(c)
    d = '<td>%s</td></tr>'%x['studcourse']
    cust.append(d)



def save():
    savebtn = webbrowser.Button(text= "Save", command=save)
    webbrowser.print(savebtn)


contents =  '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<link rel="stylesheet" type="text/css" href="css/template.css">
<title>Python Webbrowser</title>
</head>
<body>
<table>
 <td><tr>ID</tr><tr>Name</tr><tr>Email</tr><tr>Course code</tr>
%s
</table>
</body>
</html>
'''%(cust)


filename = 'database.html'

def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)

