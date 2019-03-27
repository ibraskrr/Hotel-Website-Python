from flask import Flask, render_template
from flask import request
import csv

app = Flask(__name__)

def scriptfile(aList, aFile):
    with open(aFile, 'w', newline='') as outFile:
      writer = csv.writer(outFile) 
      writer.writerows(aList)      
    return
	#this where the program callss up the fyle and links it to csv
def callfile(aFile):
    with open(aFile, 'r') as inFile: 
      reader = csv.reader(inFile) 
      aList = [row for row in reader] 
    return aList

def scriptfile(aList, aFile):
    with open(aFile, 'w', newline='') as outFile:
      writer = csv.writer(outFile) 
      writer.writerows(aList)      
    return  

#linking all the navbars together 
@app.route('/')
def index(): 
    return render_template('index.html')

def callfile(aFile):  
	with open(aFile, 'r') as inFile: 
		reader = csv.reader(inFile) 
		file = [row for row in reader] 
	return file
	
@app.route('/Bookingpage')
def bookingpage():
    return render_template('Bookingpage.html')

@app.route('/localattraction')
def localattraction():
    return render_template('localattraction.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')	

#this is where you call up the csv and to print out the exectured code into 
@app.route('/addBooking',methods=['POST'])
def addBooking():
    with open('static\\booking.csv','r') as inFile:
        
                    reader = csv.reader(inFile)
                    bList = [row for row in reader]
        
                    firstname = request.form[('firstname')]
                    surname = request.form[('surname')]
                    email = request.form[('email')]
                    phone = request.form[('phone')] 
                    country = request.form[('country')]
                    indate = request.form[('indate')]
                    roomNumber = request.form[('roomNumber')]
                    meals = request.form['meals']
                    outdate = request.form['outdate']
                    newBooking = [indate,outdate,roomNumber,firstname,surname,email,phone,country,meals]
                    bList.append(newBooking)

    with open('static\\booking.csv','w', newline='') as outFile:
                        writer1=csv.writer(outFile)
                        writer1.writerows(bList)
    return render_template('Bookingpage.html',bList=bList)


@app.route('/reviews')
def reviews(): 
    return render_template('reviews.html')    
#this is where you program the code to call up the csv file then from there you send the requests from the user to the cvs file through python then it reads the results at the bottom. 
@app.route('/addreviews', methods = ['POST'])
def addreviews():
    with open('static\\list.csv','r') as inFile:
        reader = csv.reader(inFile)
        cList = [row for row in reader]
        firstname = request.form[('firstname')]
        
    surname = request.form[('surname')]
    review = request.form[('Review')]
    rating = request.form[('Rating')]
						
    newComment = [firstname, surname, review, rating]
    cList.append(newComment)
						
    with open('static\\list.csv','w',newline='') as outFile:
        writer1=csv.writer(outFile)
        writer1.writerows(cList)
    return render_template('reviews.html',cList=cList) 
    
@app.route('/siteview')
def siteview():
	return render_template('siteview.html')



if __name__ == '__main__':
    app.run(debug = True)
