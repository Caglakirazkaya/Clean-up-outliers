
import pandas as pnd
price_list=pnd.read_csv("veriseti.csv",sep=';')
price_list.describe()

Q1=price_list.Price.quantile(0.25)
Q3=price_list.Price.quantile(0.75)

IQR_degeri=Q3-Q1

lower_limit=Q1-1.5*IQR_degeri
upper_limit=Q3+1.5*IQR_degeri


new_price_list=price_list[(price_list.Price>lower_limit) & (price_list.Price<upper_limit)]
new_price_list

