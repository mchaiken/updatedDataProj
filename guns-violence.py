import flask from Flask, render_template

print "Content-type:text/html\n"

#setting up RANKINGS
c=open("scores.txt")
ranks=c.read()
c.close()
ranks=ranks.split("\n")

#MAKING RANKING LISTS
i=0
while i<len(ranks):
    ranks[i]=ranks[i].split(',')[1:]
    while '' in ranks[i]:
        ranks[i].remove('')
    i+=1
ranks=ranks[:len(ranks)-1]

#SETTING UP VCRIMES
c=open('crimes2.txt')
vcrimes=c.read()
c.close
vcrimes=vcrimes.split('\r')

#MAKING VCRIMES LIST
i=0

while i<len(vcrimes): 
    vcrimes[i]=vcrimes[i].split(',')
    while '' in vcrimes[i]:
        vcrimes[i].remove('')
    i+=1


#MAKING VCRIMES DICTIONARY TO SORT THEM
d={}

for x in vcrimes[1:]:
    d[x[1]]=x[0]

l=sorted(d)

vcrimes=[]
for x in l:
    vcrimes+=[[d[x],x]]

    
#MAKING TABLES    
crimest='<table border="1"><tr><th>'+vcrimes[0][0]+'</th><th>'+vcrimes[0][1]+'</th></tr>'
for x in vcrimes[1:]:
    crimest+='<tr><td>'+x[0]+'</td><td>'+x[1]+'</td></tr>\n'
crimest+='</table>'


rankst='<table border="1"><tr><th>'+ranks[0][0]+'</th><th>'+ranks[0][1]+'</th></tr>'
for x in ranks[1:]:
    rankst+='<tr><td>'+x[0]+'</td><td>'+x[1]+'</td></tr>\n'
rankst+='</table>'

#FINDING NATIONAL AVERAGES
ca=0
for x in l:
    ca+=float(x)
ca/=len(l)


ra=0

for x in ranks[1:]:
    ra+=float(x[1])
ra/=len(ranks)


#MAKING DICTIONARIES OF RANKS AND VCRIMES
crimesd={}
ranksd={}

for x in vcrimes:
    crimesd[x[0]]=x[1]
    
for x in ranks:
    ranksd[x[0]]=x[1]
ranksd['RHODE ISLAND ']=ranksd['\xc2\xa0RHODE ISLAND ']
ranksd.pop('\xc2\xa0RHODE ISLAND ')


#FINDING % OF STATES W/ RANKS BELOW AVERAGE
num=0.
d=0
for x in crimesd:
    if float(ranksd[x+' '])<=ra:
        d+=1
        if float(crimesd[x])<=ca:
            num+=1
            

percent=num/d*100


#FINDING % OF STATES W/ FAILING GRADES
failp=0.
for x in crimesd:
    if float(ranksd[x+' '])<=ra and 64<=ca:
            failp+=1
basicdata[['Gun Control Score',ra,d,d/.50],['Violent Crime Rate',ca,failp+1,failp+1/.5]]

failp/=.5


@app.route("/")
@app.route("/home");
def home():
    return render_template("home.html");


print '<html><head><title>Violence and Gun Control</title></head>'
print '<body><h1>Why?</h1>'
print '<h1>The Data</h1>'
print '<h4>Violent Crimes per 100,000 in 2007 (ordered)</h4>'
print crimest
print '<h4>State Scores for Gun control by the Brady Campaign in 2007</h4>'
print rankst
print '<h1>The Analasys</h1>'
print '<table><tr><th>Average Gun Control Score</th><td>'+str(ra)+'</td></tr>
print '<table><tr><th>Average Violent Crime Rate</th><td>'+str(ca)+'</td></tr>
print'</body></html>'
