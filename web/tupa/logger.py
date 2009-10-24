from django.conf import settings
from xml.dom.minidom import parse, parseString
import os.path
import re
lokkeri=None
from django.shortcuts import get_object_or_404
from duplicate import kisa_xml
#coding: latin-1


#recorder middleware:

class PostDataRecorder:
        """
        Nauhoittaa post requestit record.xml tietokanta tiedoston loppuun mikali se on olemassa ja settings.RECORDING==True
        """
        def process_request(self, request) : 
                if settings.RECORDING==True: 
                        if request.method == 'POST':
                                posti=request.POST
                                address=request.path
                                
                                kisa_haku = re.search("^/tupa/(.*?)/.*$",address)
                                if not kisa_haku:
                                        return None
                                kisa_nimi = kisa_haku.group(1)

                                data = None
                                if os.path.isfile("record.xml"):
                                        data = parse('record.xml')
                                else:
                                        return None

                                post_test = data.createElement('post_request')
                                post_test.setAttribute("address", address )

                                for n,v in posti.iteritems():
                                        elem = data.createElement('input')
                                        elem.setAttribute("name", n )
                                        elem.setAttribute("value", v )
                                        post_test.appendChild(elem)
                                        data.childNodes[0].appendChild(post_test) 
                                
                                FILE = open("record.xml","w")
                                FILE.write(data.toxml(encoding="utf-8") )
                return None

if settings.LOGGING==True :  
  class Logger:
    """
    Logger Class 
    """
    def __init__(self) :
        self.stack=[""]
        self.file="log.log"
    def setFileName(self,fileName) :
        self.file=fileName
        return self
    def setMessage(self,message) :
        if message :
                self.stack[-1]=message
        else:
                self.stack[-1]="None"
        return self
    def push(self) :
        self.stack.append("")
        return self
    def pop(self) :
        if len(self.stack) > 1 :
           self.stack.pop()
        return self
    def clearStack(self) :
        self.stack=[""]
        return self
    def clearLog(self) :
        
        log = open(self.file, "w")
        log.write("")
        log.close()
        return self
        
    def logMessage(self) :
        log = open(self.file, "a")
        for r in self.stack:
           log.write(unicode(r).encode('ascii', 'ignore'))
        log.write("\n")
        log.close()
        return self
  lokkeri=Logger()
else :
  
  class Logger:
    def setFileName(self,fileName) :
        return self
    def setMessage(self,message) :
        return self
    def push(self) :
        return self
    def pop(self) :
        return self
    def clearStack(self) :
        return self
    def clearLog(self) :
        return self
    def logMessage(self) :
        return self
  lokkeri=Logger()

lokkeri.setFileName("laskenta.log")


