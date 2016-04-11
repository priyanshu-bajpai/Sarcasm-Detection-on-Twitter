from sklearn import svm 
import csv

print "Training SVM"
clf = svm.LinearSVC()
tariningFile = open("output.csv","r") 
reader = csv.reader(tariningFile)

X=[]
Y=[]
for row in reader:
	X.append(row[0:len(row)-1])
	Y.extend(row[len(row)-1:])
clf.fit(X,Y)
