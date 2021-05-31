import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

#line plot
def get_plot1(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('items vs price')
    # w = [1,2,3,4,5]
    plt.plot(x,y)                                  
    # cols = ['c','m','r','g','b','y']
    # plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0.1,0,0.1),autopct='%1.1f%%')
    plt.xticks(rotation=90)
    plt.xlabel('item')
    plt.ylabel('price')
    # plt.legend(x)
    l = 'price'
    plt.legend(l)   
    plt.tight_layout()
    graph = get_graph()
    return graph

#pyplot with 'o' 
def get_plot2(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('items vs price')
    plt.plot(x,y,'o')
    plt.xticks(rotation=90)
    plt.xlabel('item')
    plt.ylabel('price')
    l = 'price'
    plt.legend(l)   
    plt.tight_layout()
    graph = get_graph()
    return graph

#bar graph
def get_plot3(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('items vs price')
    plt.bar(x, y,width=0.5,label="price",color='c')
    plt.xticks(rotation=90)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

#bar graph
def get_plot4(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('Quality of food items')
    plt.bar(x,z,width=0.5,label="review",color='g')
    plt.xticks(rotation=90)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

#histogram-1
def get_plot5(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('rating vs price')
    plt.hist(z,y.sort(),histtype='bar') 
    plt.xticks(rotation=90)
    plt.xlabel('rating')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

#histogram-2
def get_plot6(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('price vs rating')
    plt.hist(y,z.sort(),histtype='bar') 
    plt.xticks(rotation=90)
    plt.xlabel('price')
    plt.ylabel('rating')
    plt.tight_layout()
    graph = get_graph()
    return graph

#scatter plot-1
def get_plot7(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('price vs rating')
    plt.scatter(y, z) 
    plt.xticks(rotation=90)
    plt.xlabel('price')
    plt.ylabel('rating')
    plt.tight_layout()
    graph = get_graph()
    return graph

#scatter plot-2
def get_plot8(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title('rating vs price')
    plt.scatter(z, y) 
    plt.xticks(rotation=90)
    plt.xlabel('rating')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

#pie chart
def get_plot9(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,7))
    # plt.title('items vs price')
    plt.plot(x,y)                                  
    cols = ['c','m','r','g','b','y']
    plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=(0.2,0.1,0,0.1,0,0.1,0,0.1,0,0.1,0,0.1),autopct='%1.1f%%')
    plt.xticks(rotation=90)
    # plt.legend(x)  
    plt.tight_layout()
    graph = get_graph()
    return graph