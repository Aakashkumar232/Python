import matplotlib.pyplot as plt

    #  -: LINE PLOT :-

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
color = 'red'
plt.plot(x,y,color)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()



x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
color = 'red'
plt.plot(x,y,color,marker ='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()



x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
color = 'red'
plt.plot(x,y,color,marker = 'o')
plt.plot(x,marker = '>')
plt.plot(y,marker = '<')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()


#   -:  SCATTER PLOT :-

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
color = 'black'
plt.scatter(x, y , color )
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
colors = 'black','red','yellow','purple','magenta'
plt.scatter(x, y , color = colors )
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()



x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
colors = 'black','red','yellow','purple','magenta'
plt.scatter(x, y ,color = colors,s = 150  )
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()


#    -: HOSTOGRAM PLOT :-

data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]

# Plot
plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

    #    -: PIE CHART :-

    
x = [30, 20, 15, 35]
y  = ['A', 'B', 'C', 'D']

# Plot
plt.pie(x, labels = y)
plt.title('Pie Chart')
plt.show()



x = [30, 20, 15, 35]
y  = ['A', 'B', 'C', 'D']

# Plot
color = "magenta","brown","black","red"

plt.pie(x, labels = y,colors = color)
plt.title('Pie Chart')
plt.show()



x = [30, 20, 15, 35]
y  = ['A', 'B', 'C', 'D']

# Plot
color = "magenta","brown","black","red"

plt.pie(x, labels = y,colors = color)
plt.title('Pie Chart')
plt.legend()
plt.show()


    #   -: BAR PLOT :-

categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 20]

# Plot
colors = 'green'
plt.bar(categories, values, color = colors, width = 0.5)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()



categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 20]

# Plot
colors = 'green','yellow','black','red'
plt.bar(categories, values, color = colors)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()



categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 20]

# Plot
colors = 'red'
plt.barh(categories, values, color = colors,height = 0.5)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()


    # SECOND DAY OF THE MATPLOTLIB LIBRARY:- 

    #   FIND THE SAME IMAGE:-

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

fname = r'C:\Users\Advance Laptop\Downloads\shiva2.jpg'

image = Image.open(fname).convert("RGB")              # opening image using pil:-

plt.imshow(image)                               # show the same color image:-
plt.show()


    # FIND THE DIFFERENT COLOR OF IMAGE:-

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname = r'C:\Users\Advance Laptop\Downloads\shiva2.jpg'

image = Image.open(fname).convert('L')          # opening image using pil:-

plt.imshow(image,cmap = 'rainbow')                 # different color mapping image to rainbow or more color scale:-
plt.show()


        #    WRITE THE TITLE OF IMAGE:-

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname = r'C:\Users\Advance Laptop\Downloads\shiva2.jpg'

image = Image.open(fname).convert('L')          # opening image using pil:-

plt.imshow(image,cmap = 'rainbow')                 # different color mapping image to rainbow or more color scale:-
plt.title("lord shiva") 

plt.show()




import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname = r'C:\Users\Advance Laptop\Downloads\shiva2.jpg'

image = Image.open(fname).convert('L')          # opening image using pil:-

plt.imshow(image,cmap = 'rainbow')                 # different color mapping image to rainbow or more color scale:-
plt.title("lord shiva") 
plt.xlabel("width")
plt.ylabel("height")
plt.grid()

plt.show()








    # -:SINE AND COSE FUNCTION WAVE:-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Sin Function')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Cos Function')

plt.tight_layout()
plt.show()


#    3D PLOTTING :-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, linestyle='--', linewidth=2, color='green', marker='o', markersize=5, label='Sin(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Sin Plot')
plt.legend()
plt.grid(True)
plt.show()

    
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x_data = np.linspace(0, 2*np.pi, 100)
y_data = np.sin(x_data)
line, = ax.plot(x_data, y_data)

def update(frame):
    line.set_ydata(np.sin(x_data + frame/10))
    return line,

ani = FuncAnimation(fig, update, frames=range(100), interval=50)
plt.show()



