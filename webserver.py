from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from datetime import datetime
import cgi
import requests
hostName = "localhost"
serverPort = 4040

def writelog(info):
    log=open('log.txt','a+')
    log.write(str(datetime.now())+'\n')
    for subdet in info:
        log.write(subdet+'\n')
    log.write('------------------------------------------------------------\n\n')
    log.close()
class MyServer(BaseHTTPRequestHandler):
    '''def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Check your phone number</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><h1>The Directory</h1>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))'''


    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes('<!DOCTYPE html> <html> <head><title>Wedding Planner</title> </head> <body> <h1 >Add Event Details</h1> <br> <br> <hr> <br> <form method="POST"  enctype="multipart/form-data" action="/"> <label for="fname">Name:</label> <input type="text" id="fname" name="fname"  required> <br> <br> <br> <label for="p number">Phone no.:</label> <input type="tel" id="p number" name="p number" value="+91" > <br> <br> <br> <label for="area">Address:</label> <input type="text" id="area" name="area"> <br> <br> <br> <label for="fm member">Date:</label> <input type="date" id="fm member" name="fm member"> <br> <br> <br> <input type="submit" value="Submit"> <input type="reset" value="Clear"> </form> </body> </html>', "utf-8"))
        #self.wfile.write(bytes("<form method='POST' enctype='multipart/form-data' action='/'><input name ='mob' type='number'><input type='submit' value='Enter number'></form>", "utf-8"))
        #self.wfile.write(bytes("<h5>DM me at asterisk#7864 on Discord</html>", "utf-8"))

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary']=bytes(pdict['boundary'], 'utf-8')
        postvars = {}
        try:
            if ctype == 'multipart/form-data':
                length = int(self.headers.get('content-length'))
                #postvars = cgi.parse_qs(self.rfile.read(length)),
                        #keep_blank_values=1)
                fields=cgi.parse_multipart(self.rfile,pdict)
                addr='Address : '+fields.get('area')[0]
                naam='Name : '+fields.get('fname')[0]
                num='Number : '+fields.get('p number')[0]
                dat='Event Date: '+fields.get('fm member')[0]
                deta=[addr,naam,num,dat]
                print(deta)
                '''username=new[0]
                assert postvars.get('foo', '') != ['simulate error']
            def infos(username):
                url = "https://api.penpencil.xyz:443/v1/oauth/token"
                headers = {"Authorization": "Bearer undefined", "Content-Type": "application/json"}
                json={"client_id": "system-admin", "client_secret": "KjPXuAVfC5xbmgreETNMaL7z", "grant_type": "password", "latitude": 0, "longitude": 0, "organizationId": "5eb393ee95fab7468a79d189", "password": "123456", "username": username}
                json2={"client_id": "system-admin", "client_secret": "KjPXuAVfC5xbmgreETNMaL7z", "grant_type": "password", "latitude": 0, "longitude": 0, "organizationId": "5eb393ee95fab7468a79d189", "password": "password", "username": username}
                yoop=requests.post(url, headers=headers, json=json)
                yop=yoop.json()
                if yop['success']==True:
                    #zee=(yop['data'])['user']
                    #return f"{zee}"
                    return f"{yop}"
                elif yop['success']==False:
                    yoop=requests.post(url, headers=headers, json=json2)
                    yop=yoop.json()
                    if yop['success']==True:
                        #zee=(yop['data'])['user']
                        #return f"{zee}"
                        return f"{yop}"
                    else:
                        return f"{yop}"'''
            body = bytes(('<html><body><h1>Your requests has been sent successfully</h1><h3>Redirecting you now</h3><script>function ap(){window.location.replace("..")};setTimeout(ap,2500)</script></body></html>'),'utf=8')
            self.send_response(200)
            self.send_header("Content-type", "text")
            self.send_header("Content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            writelog(deta)
        except:
            self.send_error(500)
            raise
        return deta
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
