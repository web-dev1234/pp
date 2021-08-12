import matplotlib.pyplot as plt
import folium
import pandas
left=[1,2,3,4,5]
height=[10,24,36,40,150]
tick_label=['one','two','three','four','five']
plt.bar(left,height,tick_label=
tick_label,
       width=0.9,color=['red','blue','green','yellow','pink'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My bar chart!')
plt.show()
