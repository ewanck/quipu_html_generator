import csv

index = csv.reader(file('index.csv', 'rb'))

i = 0

html = ""

f = open('html/master.html','w')

colors = {"l_green":{"val":"25,189,101", "knot":"buttons/l_green.png"}, "l_blue":{"val":"78,191,191", "knot":"buttons/l_blue.png"}, "red":{"val":"225,27,75", "knot":"buttons/red.png"}, "yellow":{"val":"250,203,17","knot":"buttons/yellow.png"},"l_purple":{"val":"177,101,169", "knot":"buttons/l_purple.png"}, "d_purple":{"val":"125,54,150","knot":"buttons/d_purple.png"}, "d_green":{"val":"132,201,138", "knot":"buttons/d_green.png"}}

threadid = 0;

for item in index:
    if i>0:
        output = open("html/"+item[1]+ str(i)+".html","w")
        container = """<div id=\""""+item[0]+"""-thread-container" class="thread-container """+item[2]+""" """+item[3]+"""" data-name=\"""" + item[1] +"""" data-len=\""""+item[4]+"""" data-src="QUIPU_ARCHIVE/"""+item[8]+"""" data-color=\""""+colors[item[5]]["val"]+""""><p><img class="start-knot" src=\""""+colors[item[5]]["knot"]+""""/>"""

        subtitles = csv.reader(file('subtitles/'+item[6], 'rb'))
        ii = 0;
        thread = ""
        for subtitle in subtitles:
            if ii>0:
                time_in = str((float(subtitle[3])/24))
                time_out = str((float(subtitle[4])/24))
                thread = thread + "<a id='thread_"+str(threadid)+"' class='thread "+item[1]+"' data-in='"+time_in+"' data-out='"+time_out+"'>"+subtitle[6]+"</a>"
                threadid = threadid + 1
            ii = ii + 1

        output.write(container+thread+"""</p></div>""")
        html = html + container + thread + """</p></div>"""
        output.close()

    i = i +1

f.write(html)
f.close()
    
