#!/usr/bin/python
import cgi, os,commands
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)     #fn=function
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
else:
   message = 'No file was uploaded'


  
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)
print "<pre>"
print   commands.getoutput("sudo rsync -avu /var/ftp/pub/ /var/www/html/")
print   commands.getoutput("sudo rsync -avu /tmp/systemd-private-b93c208bbea9476aba1f52104eb5afaa-httpd.service-uPBWT1/tmp/ /var/www/html/")
print "</pre>"
#print os.system(rsync -avu /var/ftp/pub/ /var/www/html/)  ...same as commands.getoutput..line1
