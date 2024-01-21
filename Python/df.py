import pandas as pd

url ="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style", "drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type", "num-of-cylindere","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers          
# df.to_csv("D:\data_ana\df.csv")
# df.dtypes xem kiểu dữ liệu của các cột
# df.drop(1)


#df.describe() xem thống kê của các cột có thể tính được
#df.describe(include="all") show full
#df.info show 30 dong dau va 30 dong cuoi
#df["price"] = df["price"]+1 tang gia tri moi price len 1

#df.dropna(subnet=["price"], axis = 0, inplace=true) 0 la bo theo hang, 1 la bo theo cot
# df.fillna(130, inplace = True)
#df.dropna(how='all') Xoa khi tat ca cac hang trong
#df.replace({"?": np.nan, "--": np.nan})
#df["price"].replace(np.nan, mean)

# df["city-mpg"]=235/df["city-mpg"]
# df.rename(columns={"city-mpg":"city-L/100km"}, inplace=True)

#df["price"] = df["price"].astype("int") chuyen kieu du lieu

# chia thành các khoảng

# bin = np.linspace(min(df["price"], max(df["price"]), 4)
# group_name=['low', 'medium', 'high']
# df["priced-bined"]=pd.cut(df["price"], bin, labels=group_name, include_lowest=True)

# pd.get_dummies(df["fuel"])
# print(df.loc[1,["price"]])
# print(df["drive-wheels"].value_counts().to_frame()) đếm số lần xuất hiện mỗi giá trị trong cột

# df_grp= df.groupby(['drive-wheels', 'body-style'], as_index=False).mean() nhóm theo 2 cột và tính trung bình các cột còn lại
# df.pivot(index='drive-wheels', columns='body-style') tạo pivot table 

#df.is_na() lấy các giá trị missing
#df.is_na().any() Hiện các cột có giá trị n/a
