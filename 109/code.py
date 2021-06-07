import statistics
import pandas as pd
import csv


df = pd.read_csv("StudentsPerformance.csv")
read_list = df["reading score"].to_list()
mean = statistics.mean(read_list)
median = statistics.median(read_list)
mode = statistics.mode(read_list)

print("Mean Of this Data is",mean)
print("Median Of this Data is",median)
print("Mode Of this Data is",mode)

std_deviation = statistics.stdev(read_list)
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end   = mean - (3*std_deviation), mean+(3*std_deviation)

print("Standard Deviation of this data is",std_deviation)

list_of_data_within_1_std_deviation = [result for result in read_list if result> first_std_deviation_start and result< first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in read_list if result> second_std_deviation_start and result< second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in read_list if result> third_std_deviation_start and result< third_std_deviation_end]

print("{}% Of Data Lies Within 1 Deviation".format(len(list_of_data_within_1_std_deviation)*100/len(read_list)))
print("{}% Of Data Lies Within 2 Deviation".format(len(list_of_data_within_2_std_deviation)*100/len(read_list)))
print("{}% Of Data Lies Within 3 Deviation".format(len(list_of_data_within_3_std_deviation)*100/len(read_list)))

