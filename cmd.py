
#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import html
import subprocess as sub



var=cgi.FieldStorage()
username=var.getvalue("uname")
password=var.getvalue("pass")
cmd=var.getvalue("command")
if cmd!= None:
    if "help" in cmd:
        print("help ")

    print('<body style="background-color:lightblue">')
    print('<div style="color:green;width:400px;margin:auto">')
    print('<h2>Entered command by user:{}</h2>'.format(cmd))
    print("<br/>")
    out=sub.getoutput(cmd)
    out=out.replace('\n','<br/>')
    out=out.replace(' ','&nbsp;&nbsp;')
    
    print('<h2>your output is:</h2>',out)
    print('<div style="color:red;background-color:lightgray;width:400px;margin:auto">')
    print('<form action="/cgi-bin/cmd.py">')
    print('<h3 style="display:inline">Enter your command:</h3>')
    print('<input type="text" name="command">')
    print('<input type="submit" value="Run">')
    print('</form>')
    print('</div>')
    print('<body>')

if "niraj" in username and "kumar" in password:
    
    print('<body style="background-color:lightblue">')
    print('<h2 style="color:green;position:fixed;width:400px;margin:auto;">My command Line</h2>')
    print("<br/>")
    print('<div style="color:red;background-color:lightgray;width:400px;margin:auto">')
    print('<form action="/cgi-bin/cmd.py">')
    print('<h3 style="display:inline">Enter your command:</h3>')
    print('<input type="text" name="command">')
    print('<input type="submit" value="Run">')
    print('</form></div>')
    print('</body')

else:
    print('<body style="background-color:lightblue;">')
    print('<h3 style="color:green;width:500px;margin:auto;margin-top:300px">Wrong username or password</h3>')
    print('</body>')


























