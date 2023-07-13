#Import all modules here:
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#data of marks of 1000 students in a math test and then we plotted it:
#Reading the file:
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#plotting the graph:
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()

#Standard deviation and sampling mean of 100 students 1000 times and plotted it:
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of population:- ",mean)
print("Standard deviation of Population:- ", std_deviation)

##Plotting the trace of sampling mean on the graph:
#Code to find the mean of 100 data points 1000 times
#Function to get the mean of the givn data samples
#pass the number of data points you want as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
        
    mean = statistics.mean(dataset)
    return mean

#Pass the number of time you want the mean of the data points as a parameter in range function in fro loop
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(1000)
    mean_list.append(set_of_means)
    
##Calculating mean and Standard_deviation of the sampling deviation.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ", mean)

#Plotting the mean of the sampling:
fig = ff.create_distplot([mean_list], ["reading time"], show_hist = False)
fig.add_trace(go.Scatter(go.Scatter(x = [mean,mean], y=[0,0.20]), mode = 'lines', name = "MEAN"))
fig.show()

##Comparating the population mean and sampling mean and standard deviation 
##and found that followed the properties of sampling distribution:
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of population:- ", mean)
print("Standard Deviation of Population:- ", std_deviation)

##Calculating mean and Standard_deviation of the sampling distribution
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print('mean of sampling distribution:- ', mean)
print('Standard deviation of sampling distribution:- ', std_deviation)

##Founding 1std, 2std,3std:
first_std_deviation_start, first_std_deviation_end =mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(2*std_deviation)
print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2",  second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

#plotting the graph with traces:
fig = ff.create_distplot([mean_list],["reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, first_std_deviation_start],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, first_std_deviation_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

#Plotting the sample mean and saw in which deviation it lies
##finding the mean of the Second data (STUDENTS WHO HAD EXTRA CLASSES) and plotting it on the plot.
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ", mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample2, mean_of_sample2], y = [0,0.17], mode = 'lines',name = "MEAN OF SAMPLES" ))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode ="lines", name = "STANDARD DEVIATION END 2"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = 'lines', name = "STANDARD DEVIATION END 3"))
fig.show()

