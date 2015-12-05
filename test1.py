import os
import base64
import Algorithmia
from html.parser import HTMLParser

i=0
class MyHTMLParser(HTMLParser):
    def __init__(self):
       HTMLParser.__init__(self)
       self.recording = 0
       self.isp = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'pre' or tag == 'p':
            self.recording = 1
        if tag == 'p':
            self.isp = 1
    def handle_endtag(self, tag):
        if tag == 'pre' or tag == 'p':
            self.recording -= 1
        if tag == 'p':
            self.isp = 0;
    def handle_data(self, data):
        if self.recording:
            file = open("newfile%s.txt" %i, "a")
            file.write(str(data)+'\n')
            file.close()
    def excise(self,filename, start, end):
        with open(filename) as infile, open(filename + ".out", "w") as outfile:
            for line in infile:
                if line.strip() == start:
                    break
                outfile.write(line)
            for line in infile:
                if line.strip() == end:
                    break
            for line in infile:
                outfile.write(line)
            
            #d = file.readlines()
            #file.seek(0)
            #for i in d:
            #    if i != "The review above was posted...":
            #        file.write(str(data)+'\n')
            #f.truncate()
            #f.close()
        #if self.isp:
         #   file = open("newfile%s.txt" %i, "a")
         #   input = str(data)
         #   client = Algorithmia.client('sim0Msfwf+ITgS1ZUBm6dB5X5dw1')
         #   algo = client.algo('nlp/SentimentAnalysis/0.1.1')
         #   file.write(str(algo.pipe(input))+'\n')
         #   file.close()
    
                
#os.path.dirname(os.path.realpath(__file__))
for files in os.listdir(os.getcwd()):
    if files.endswith(".html"):
        file = open("html_list.txt", "a")
        file.write("%s\n" % files)
        file.close()
f = open('html_list.txt')
for line in iter(f):
    print(line)
    line = line.strip('\n')
    f1=open(line,"r")
    s=f1.read()
    parser = MyHTMLParser()
    parser.feed(s)
    fileName = "newfile{}.txt".format(i)
    parser.excise(fileName,"The review above was posted to the","index of all rec.arts.movies.reviews reviews")
    i+=1
f.close()



