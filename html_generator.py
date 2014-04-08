import csv

file_name = 'ANONIMO_ID_131.csv'
name = 'anon131'
# section = 'c'
subtitles = csv.reader(file('subtitles/'+file_name, 'rb'))

html = ''

i=0

for subtitle in subtitles:
    if i>0:
        time_in = str((float(subtitle[3])/24))
        time_out = str((float(subtitle[4])/24))
        html = html + "<a id='thread_"+str(i)+"' class='thread "+name+"' data-in='"+time_in+"' data-out='"+time_out+"'>"+subtitle[6]+"</a>"
#        edits = csv.reader(file('edits/'+file_name, 'rb'))
#        for edit in edits:
#            print edit
#            print subtitle
#            if edit[0] == subtitle[0]:
#                print 'match'
#                html = html +"<a id='thread_"+str(i+54)+"' class='thread "+name+" "+section+" edited'>" + edit[1]+"</a>"
    i = i +1

print html
