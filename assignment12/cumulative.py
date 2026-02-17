import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    with  sqlite3.connect("db/lesson.db") as conn: 
        sql_statement = """SELECT line_items.order_id, SUM(line_items.quantity*products.price) as total_price
        FROM line_items JOIN products ON products.product_id = line_items.product_id 
        GROUP BY line_items.order_id;"""
        df = pd.read_sql_query(sql_statement, conn)
except sqlite3.Error as e:
    print("Error:", e)

def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df.plot(x="order_id", y='cumulative', kind="line", title="Order ID vs. Cumulative Revenue")
plt.show()