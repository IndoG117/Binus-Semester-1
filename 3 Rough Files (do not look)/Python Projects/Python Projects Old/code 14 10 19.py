#%%

#imports python csv module
import csv
#imports python datetime module and assigns to dt
import datetime as dt
#imports python statistics module and assigns to st
import statistics as st
#imports python math plotting librabry and assigns to plt
import matplotlib.pyplot as plt

# designates activity.csv's identity as filename and its location in storage
filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\activity.csv'

#dictionary with dates as keys and a list of steps per interval per date as values
dict = {}
#dict with 5min interval as key, value is number of steps per instance of the 5min interval for the whole period
dictInterval = {}
#content of dictInterval minus dates considered as weekends
dictIntervalWeekDays = {}
#content of dictInterval but only with weekends
dictIntervalWeekEnds = {}

#withdraws the contents of the csv file into the program and assigns it as f
with open(filename) as f:
#invoking the python csv module's reader function and telling it to read the contents of the csv.file
    reader = csv.reader(f)
#tells the reader function to read the first row of the csv file
    headerRow = next(reader)
#instructs the reader to scan through the elements of the first row
    for row in reader:
#assigns content of the actual 'steps' column of the csv file to the variable date
        steps = row[0]
#tells program to ignore entries with missing values
        if (steps != "NA"):
#assigns content of the actual 'dates' column to the variable date
            date = row[1]
#converts the contents of the dates column into integer value so it can be processed by strptime..
#..using strptime to turn the integer into a date that can be processed by the datetime module...
#..and returning the day from the year-month-day format            
            date2 = int(dt.datetime.strptime(date,"%Y-%m-%d").day)
#assigns the content of the intervals column to the variable interval
            interval = int(row[2])
#tells python to set the dates of the dates column as keys for the dictionary dict
#setdefault will turn a nonexistent key into key (i.e. dates that havent been registered as a key yet)
#forces the date keys to be string and then prepares an empty list as the value for every date
            dict.setdefault(str(date),[])
#adds the steps in the steps column to the 
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))

            if (date2 % 7 == 0): 
                dictIntervalWeekEnds.setdefault(interval,[])
                dictIntervalWeekEnds[interval].append(int(steps))
            else:
                dictIntervalWeekDays.setdefault(interval,[])
                dictIntervalWeekDays[interval].append(int(steps))

               
listDate = []
listTotal = []
listAve = []

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))
    
plt.hist(listTotal)
plt.title("Total Steps per day")
plt.xlabel("Steps per day")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))
#plt.show()

print("Mean : ",st.mean(listTotal))
print("Median : ",st.median(sorted(listTotal)))


print(date2)



 

    


    


    



