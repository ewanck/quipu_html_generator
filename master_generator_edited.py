import csv

#index = csv.reader(file('index_edited.csv', 'rb'))

i = 0

html = ""

f = open('html/master_edited.html','w')

threadid = 0;

subtitles = csv.reader(file('subtitles/ESPERANZA_A_spanish.csv', 'rb'))
ii = 0;
thread = "<p>"
name = "esperanza"
section = "a"


for subtitle in subtitles:
    if ii>0:
        time_in = str((float(subtitle[3])/24))
        time_out = str((float(subtitle[4])/24))
        thread = thread + "<a id='thread_a_"+str(threadid)+"' class='thread "+name+" "+section+"' data-in='"+time_in+"' data-out='"+time_out+"'>"+subtitle[6]+"</a>"
        threadid = threadid + 1
        edits = csv.reader(file('edits/ESPERANZA_A.csv', 'rb'))
        for edit in edits:
            print edit[0]
            print ii
            if edit[0]==str(ii):
                print "write"
                thread = thread + "<a id='thread_z_"+str(threadid)+"' class='thread edited "+name+" "+section+"'>"+edit[1]+"</a>"
    ii = ii + 1
        
#    output.write(container+thread+"""</p></div>""")
#    html = html + thread + """</p></div>"""
#    output.close()

f.write(thread)
f.close()
    
