import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def five_number_summary(datacolumn):
    sorted(datacolumn)
    Q1,med,Q3 = np.percentile(datacolumn , [25,50,75])
    return (datacolumn.mean())
    #return min(datacolumn), Q1, med, Q3, max(datacolumn)

#This next line makes our charts show up in the notebook

data = pd.read_csv("data.csv")

math_data_y = data[(data["Varsity athlete"] == "Yes")]
math_data_n = data[(data["Varsity athlete"] == "No")]

math_data = [math_data_y['Score'], math_data_n['Score'] ]
print(five_number_summary(math_data_n['Score']))
plt.boxplot(math_data)

locs, labels=plt.xticks()
new_xticks=['Yes', 'No']
plt.xticks(locs,new_xticks)
plt.title('Score vs. Varsity Sport')
plt.xlabel('Varsity Sport?')
plt.ylabel('Score')

#classes = ["AP Statistics - 10th Period", "AP Statistics - 3rd Period", "Math Modeling", "Precalculus"]

#fig, plots = plt.subplots(4, 1)

graph = 0
#for period in classes:
#    math_data_y = data[ (data["Math class"] == period)   &  (data["Varsity athlete"] == "Yes") ]
#    math_data_n = data[ (data["Math class"] == period)  &  (data["Varsity athlete"] == "No") ]
#    plots[graph].set_ylim([0,150])
#    math_data = [math_data_y['Score'], math_data_n['Score'] ]
#    print(period)
#    ##print (outlier_params(math_data_y['Score']))
#    print(five_number_summary(math_data_n['Score']))
#    plots[graph].boxplot(math_data, widths=(0.25, 0.25))
#    plots[graph].set_title(period)
#    plots[graph].set(xlabel='Varsity Sport?', ylabel='Score')
#    plots[graph].set_xticklabels(["Yes", "No"], rotation=0)
#    graph += 1

plt.show()




#fig, plots = plt.subplots(4, 2)

#math_data_y = data[ (data["Math class"] == "AP Statistics - 10th Period")   &  (data["Varsity athlete"] == "Yes") ]
#plots[0,0].set_ylim([0,150])
#plots[0,0].boxplot(math_data_y['Score']);

#print ("Mean % ", math_data_y.loc[:,"Score"].mean(), )


#math_data_n = data[ (data["Math class"] == "AP Statistics - 10th Period")  &  (data["Varsity athlete"] == "No") ]
#plots[0,1].set_ylim([0,150])
#plots[0,1].boxplot(math_data_n['Score']);


#plt.show()

