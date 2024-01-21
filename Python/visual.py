# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# url ="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
# df = pd.read_csv(url, header=None)
# headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style", "drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type", "num-of-cylindere","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
# df.columns = headers          
# x= np.random.randn(1000)
# plt.hist(x,100)
# plt.title("Histogram")
# plt.show() chọn vẽ histogram với x là trục x, 100 là trục y, title là tên đồ thị


# df.plot(kind='bar',x="price", y="engine-size")
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

# plt.show()

#pd.read_excel(url,sheetname="",skiprows=range(20),skip_footer=2)