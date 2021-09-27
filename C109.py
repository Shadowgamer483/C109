from os import name
import random
from re import S
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
#calculating mean and standard deviation
mean=sum(dice_result)/len(dice_result)
stdv=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
firstsd_start,firstsd_end=mean=stdv,mean+stdv
secondsd_Start,secondsd_End=mean-(2*stdv),mean+(2*stdv)
thirdsd_Start,thirdsd_End=mean-(3*stdv),mean+(3*stdv)
print("The mean is",mean)
print("The mode is",mode)
print("The median is",median)
print("The StandardDevision is",stdv)
fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[firstsd_start,firstsd_start],y=[0,0.17],mode="lines",name="standarddivision1"))
fig.add_trace(go.Scatter(x=[firstsd_end,firstsd_end],y=[0,0.17],mode="lines",name="standarddivision1"))
fig.add_trace(go.Scatter(x=[secondsd_Start,secondsd_Start],y=[0,0.17],mode="lines",name="standarddivision2"))
fig.add_trace(go.Scatter(x=[secondsd_End,secondsd_End],y=[0,0.17],mode="lines",name="standarddivision2"))



fig.show()














