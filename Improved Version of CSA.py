#!/usr/bin/env python
# coding: utf-8

# # Improved Version of Customer Sales Analysis

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('sales_data_sample.csv', encoding='unicode_escape')
df


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.head().T


# In[6]:


df.info()


# <b style="color:blue; font-size:16px">Let's Check for Null Values</b>

# In[7]:


pd.isnull(df).sum()


# In[8]:


df.drop(columns=['ADDRESS_LINE2'], inplace=True)
# Shouldn't run this during analysis again, as this column is removed already


# In[9]:


df.shape


# In[10]:


df.columns


# In[11]:


df.describe()


# <b style="color:blue; font-size:16px">Let's Check for any Outliers</b>

# In[12]:


plt.figure(figsize=(7, 4))
plt.boxplot(df['SALES'])
plt.show()


# In[13]:


df.duplicated()


# In[14]:


df[df.duplicated()]


# In[15]:


# Rename column
df.rename(columns= {'PRICE_EACH':'UNIT_PRICE'}, inplace=True)


# In[16]:


df.columns


# - <b style="color:purple">MSRP - Manufacturer's Suggested Retail Price</b>

# <b style="color:blue; font-size:16px">Standardizing Order Date</b>

# In[17]:


# standardizing the 'ORDER_DATE' Column
def standardize_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except ValueError:
        return None
    
df['ORDER_DATE'] = df['ORDER_DATE'].apply(standardize_date)
df


# ## Date Handling

# <b style="color:blue; font-size:16px">Day of the Week</b>

# In[18]:


# Adding a column for the day of the week
df['DAY_OF_WEEK'] = df['ORDER_DATE'].dt.day_name()


# In[19]:


df['DAY_OF_WEEK']


# In[20]:


# Grouping and Summarizing
df.groupby('DAY_OF_WEEK')['SALES'].sum()


# In[21]:


sales_by_day = df.groupby('DAY_OF_WEEK', 
                          as_index=False)['SALES'].sum().sort_values(
    by='SALES', ascending=False)

sales_by_day


# In[22]:


# Analyzing if Sales are higher on certain Days
plt.figure(figsize=(7, 3))
plt.barh(sales_by_day['DAY_OF_WEEK'], sales_by_day['SALES'], color = '#94fc03')
plt.title('Total Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Sales')
plt.show()


# In[23]:


# Same as above
plt.figure(figsize=(7, 3))
sns.barplot(data = sales_by_day, x = 'DAY_OF_WEEK', y = 'SALES', color = '#94fc03')
plt.title('Total Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Sales')
plt.show()


# <b style="color:blue; font-size:16px">Seasonal Trends</b>

# In[24]:


def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['SEASON'] = df['ORDER_DATE'].dt.month.apply(get_season)
df[['ORDER_DATE', 'SEASON']].head()


# In[25]:


sales_by_season = df.groupby('SEASON', 
                          as_index=False)['SALES'].sum().sort_values(
    by='SALES', ascending=False)

sales_by_season


# In[26]:


# Analyzing if there are any Seasonal effects on Sales
plt.figure(figsize=(7, 3))
plt.barh(sales_by_season['SEASON'], sales_by_season['SALES'], color = '#94fc03')
plt.title('Total Sales by Season')
plt.xlabel('Season')
plt.ylabel('Total Sales')
plt.show()


# In[27]:


# Analyzing if there are any Seasonal effects on Sales (Same as Above)
plt.figure(figsize=(7, 3))
plt.fill_between(sales_by_season['SEASON'], sales_by_season['SALES'], 
                 color = '#94fc03', alpha = 0.5)
plt.plot(sales_by_season['SEASON'], sales_by_season['SALES'], 
         marker = 'o', color = 'g')
plt.title('Total Sales by Season')
plt.xlabel('Season')
plt.ylabel('Total Sales')
plt.show()


# ### Time Series Analysis

# In[28]:


df['SALES'].head()


# In[29]:


df['SALES'].head(3).mean()


# <b style="color:blue; font-size:16px">Rolling Average</b>

# In[30]:


df['SALES'].rolling(window=3).mean().head(10)


# - <p style="color:purple">In time series analysis, 
#     <b style="color:green">rolling(window=3).mean()</b> calculates the moving average over a specified window.</p>
# 
# - <p style="color:purple">Initially, there aren’t enough data points to fill the window. For example, with 
#     <b style="color:green">window=3</b>, the first two positions won’t have enough data to calculate the average, hence they’ll show 
#     <b style="color:green">NAN</b>. Once there are enough data points to fill the window, the moving average can be calculated, and we’ll start seeing values instead of 
#     <b style="color:green">NANs</b>. This is normal and expected in rolling calculations.
# </p>
# 
# - <p style="color:purple">Imagine it like a running average that slides along your data points, giving you a smoothed curve that can help you better understand the underlying patterns.</p>
# 
# - <p style="color:purple">
#     <b style="color:green">Rolling averages</b> smooth out the data to reveal the underlying trend. For example, in sales data, they help you see overall growth or decline without being distracted by daily ups and downs.</p>
#     
# - <p style="color:purple">It might not feel intuitive at first, but think of it like looking at a city's skyline: zoom out to see the overall shape, not just individual buildings.</p>
#     
# - <b style="color:green">Rolling averages help you zoom out.</b>

# <b style="color:blue; font-size:16px">Sales Over Time</b>

# In[31]:


sales_by_qtr = df.groupby('QTR_ID', 
           as_index=False)['SALES'].sum().sort_values(
    by='SALES', ascending=False)

sales_by_qtr


# In[32]:


plt.figure(figsize=(10, 4))
plt.plot(sales_by_qtr['SALES'], sales_by_qtr['QTR_ID'], 
         '*', ms = 10, ls = '-.', lw = 2, c = '#5604b5')
plt.title('Total Sales Quarterly')
plt.xlabel('Quarter')
plt.ylabel('Total Sales')
plt.show()


# <div style="color:purple; border:2px solid green; padding:5px; ">
# We can clearly see:
#     <ul style="color:green; font-weight:bold;">
#         <li>A trend in sales for the first two quarters, reaching the lowest point in the second quarter.</li>
#         <li>From there, sales steadily increase over the remaining quarters, showing a clear upward trajectory.</li>
#     </ul>
# This pattern suggests a mid-year slump with a recovery in the latter half of the year.
# </div>

# In[33]:


sales_by_month = df.groupby('MONTH_ID', 
           as_index=False)['SALES'].sum().sort_values(
    by='SALES', ascending=False)

sales_by_month


# In[34]:


plt.figure(figsize=(10, 4))
plt.plot(sales_by_month['SALES'], sales_by_month['MONTH_ID'], 
         'p', ms = 15, mfc = 'w', mec = '#05a30b', ls = '-', lw = 3, c = '#06d40a')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()


# <div style="color:purple; border:2px solid green; padding:5px; ">
# In this graph, sales fluctuate widely on a monthly basis. We observe:
#     <ul style="color:green; font-weight:bold;">
#         <li>An initial increase, reaching a peak around mid-year, followed by a sharp decline.</li>
#         <li>After the lowest point, sales start to recover and stabilize in the latter months, with a consistent upward trend toward the end.</li>
#     </ul>
# This indicates considerable variability in monthly sales, with some months performing significantly better than others.
# </div>

# In[35]:


sales_by_year = df.groupby('YEAR_ID', 
           as_index=False)['SALES'].sum().sort_values(
    by='SALES', ascending=False)

sales_by_year


# In[36]:


plt.figure(figsize=(10, 4))
plt.plot(sales_by_year['SALES'], sales_by_year['YEAR_ID'], 
        'H', ms = 10, ls = ':', lw = 2, c = '#0758fa')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()


# <div style="color:purple; border:2px solid green; padding:5px; ">
# We can clearly see:
#     <ul style="color:green; font-weight:bold;">
#         <li>A significant increase in total sales in 2004.</li>
#         <li style="color:red;">A sharp decline in total sales in 2005.</li>
#         <li style="color:blue;">A significant drop in total sales from the first year to the second year, followed by a gradual recovery in the final year.</li>
#     </ul>
# This V-shaped trend indicates that sales initially declined but started to bounce back. However, sales have not yet reached the initial peak observed in the first year.
# </div>

# ## Deeper Analytical Insights

# ### Product-level Analysis

# <b style="color:blue; font-size:16px">Discounts</b>

# In[37]:


# Adding a discount column
df['DISCOUNT'] = ((df['MSRP'] - df['UNIT_PRICE']) / df['MSRP']) * 100
df['DISCOUNT'] = round(df['DISCOUNT'].apply(lambda x: max(x, 0)), 2)


# In[38]:


# Categorize Discounts
bins = [0, 10, 20, 30, 50, 100]
labels = ['0-10%', '10-20%', '20-30%', '30-50%', '50-100%']
df['DISCOUNT_CATEGORY'] = pd.cut(df['DISCOUNT'], bins=bins, labels=labels, right=False)


# In[39]:


sales_vol_by_discount = df.groupby('DISCOUNT_CATEGORY', 
                                   observed=False)['QUANTITY_ORDERED'].sum().reset_index()
sales_vol_by_discount


# In[40]:


# Sales vs. Discounts
plt.figure(figsize=(10, 4))
sns.barplot(data = sales_vol_by_discount, x = 'DISCOUNT_CATEGORY', y = 'QUANTITY_ORDERED', 
            hue = 'DISCOUNT_CATEGORY', palette = 'gist_rainbow')
plt.title('Sales Volume by Discount Category')
plt.xlabel('Discount Category')
plt.ylabel('Sales Volume')
plt.show()


# <p style="color:purple">The 
#     <b style="color:green">0-10%</b> discount category has the highest sales volume, indicating that smaller discounts are perhaps more frequent or applied to popular items. Sales volume decreases with higher discounts, peaking the lowest in the 
#     <b style="color:green">50-100%</b> category.</p>

# <b style="color:blue; font-size:16px">Product Categories</b>

# In[41]:


sales_by_prod_cat = df.groupby('PRODUCT_LINE')['SALES'].sum().reset_index()
sales_by_prod_cat


# In[42]:


# Sales by Product Category
plt.figure(figsize=(10, 4))
sns.barplot(data = sales_by_prod_cat, x = 'SALES', y = 'PRODUCT_LINE',
            hue = 'PRODUCT_LINE', palette = 'gist_rainbow')
plt.title('Sales by Product Category')
plt.xlabel('Sales')
plt.ylabel('Product Category')
plt.show()


# - <p style="color:purple">
#     <b style="color:green">Classic Cars</b> are the top performers with the highest sales, followed by 
#     <b style="color:green">Vintage Cars</b>. 
# </p>
#     
# - <p style="color:purple">
#     <b style="color:red">Trains</b> lag far behind. 
# </p>
# 
# <p style="color:purple">This visual highlights which product lines drive the most revenue and which might need re-evaluation. Strategic focus on high performers like 
#     <b style="color:green">Classic Cars</b> could maximize profitability.
# </p>

# <b style="color:blue; font-size:16px">Customer Analysis</b>

# In[43]:


# Customer distribution by COUNTRY
customer_distribution = df.groupby('COUNTRY')['CUSTOMER_NAME']. \
                        nunique().sort_values(ascending=False).head(7)
customer_distribution


# In[44]:


cmap = plt.get_cmap('Greens_r')
colors = cmap(np.linspace(0, 1, len(customer_distribution)))

plt.figure(figsize=(5, 5))
plt.pie(
    customer_distribution.values,
    labels = customer_distribution.index,
    startangle = 180,
    colors=colors,
    autopct='%1.1f%%',  # Shows percentage with 1 decimal place
    pctdistance=0.85,   # Position of the percentage labels
)
plt.title('Customer Distribution by Country')
plt.show()


# - <p style="color:purple">
#     <b style="color:purple">Dominance of the US Market</b>: The most significant portion of the customer base is concentrated in the United States, accounting for a substantial 
#     <b style="color:green">51.5%</b> of the total customers. This indicates a strong presence and customer traction in the US market. 
# </p>
# 
# - <p style="color:purple">
#     <b style="color:purple">European Presence</b>: European countries like France, UK, Spain, Germany, and Finland collectively represent a significant portion of the customer base. This suggests a considerable presence and customer engagement in the European market.
# </p>
# 
# - <p style="color:purple">
#     <b style="color:purple">Australian Market</b>: Australia contributes 
#     <b style="color:green">7.4%</b> to the overall customer distribution, indicating a notable presence in the Australian market.
# </p>
# 
# <b style="color:purple">The US market holds the most significant share, emphasizing the importance of this market for the business.</b>

# <b style="color:blue; font-size:16px">Order Analysis</b>

# In[45]:


# Quantity ordered vs. ORDER_LINE_NUMBER
qty_ordered_per_line = df.groupby('ORDER_LINE_NUMBER')['QUANTITY_ORDERED'].sum()
qty_ordered_per_line


# In[46]:


sns.set(rc = {'figure.figsize':(12, 4)})
sns.barplot(data = qty_ordered_per_line, color = '#04b509')

plt.title('Total Quantity Ordered by Order Line Number')
plt.xlabel('Order Line Number')
plt.ylabel('Total Quantity Ordered')
plt.show()


# - <p style="color:purple">The chart clearly shows a descending trend in the total quantity ordered as the order line number increases. This suggests that the first few order lines typically have a higher demand compared to later ones.
# </p>
# 
# - <p style="color:purple">The order line number likely corresponds to specific products or item variations. The initial peak for order line numbers
#     <b style="color:green">1</b> or <b style="color:green">2</b> suggests that these products are either highly popular or heavily promoted.
# </p>
# 
# <p style="color:purple">This information can be valuable for demand forecasting and planning purposes.</p>

# In[47]:


plt.get_cmap('prism')


# In[48]:


# Relationship between QUANTITY_ORDERED and SALES.
colors = np.linspace(0, 1, len(df['QUANTITY_ORDERED']))

plt.figure(figsize=(10, 4))
plt.scatter(df['QUANTITY_ORDERED'], df['SALES'], c = colors, cmap='prism')
plt.title('Relationship between Quantity Ordered and Sales')
plt.xlabel('Quantity Ordered')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()


# - <p style="color:purple">
#     <b style="color:purple">Positive Correlation</b>: The overall trend suggests a positive correlation between the quantity ordered and sales. As the quantity ordered increases, the sales tend to increase as well. This indicates that higher order quantities generally lead to higher sales.
# </p>
# 
# - <p style="color:purple">
#     <b style="color:purple">Clustering</b>: The data points seem to cluster in certain areas, with denser clusters occurring in the lower quantity and sales ranges. This might suggest that a significant portion of the orders and sales are concentrated in the lower end of the spectrum.
# </p>
# 
# - <p style="color:purple">
#     <b style="color:purple">Outliers</b>: There are a few data points scattered towards the higher quantity and sales ranges. These could be considered outliers as they deviate significantly from the majority of the data points.
# </p>
# 
# <b style="color:purple">The outliers in the higher quantity and sales ranges represent potential opportunities for further analysis. These could be high-value customers or products that could be further targeted for growth.</b>

# ### Customer Segmentation

# <b style="color:blue; font-size:16px">Let's do RFM Analysis</b>
# 
# - <p style="color:purple">When their last purchase was - <b style="color:green">Recency</b></p>
# - <p style="color:purple">How often they purchase - <b style="color:green">Frequency</b></p>
# - <p style="color:purple">How much they spend - <b style="color:green">Monetary</b></p>

# In[49]:


recency = df.groupby('CUSTOMER_NAME', 
                     as_index=False)['ORDER_DATE'].max().sort_values(
    by='ORDER_DATE', ascending=False)

frequency = df.groupby('CUSTOMER_NAME', 
                       as_index=False)['ORDER_NUMBER'].count().sort_values(
    by='ORDER_NUMBER', ascending=False)

monetary = df.groupby('CUSTOMER_NAME', 
                      as_index=False)['SALES'].sum().sort_values(
    by='SALES', ascending=False)


# In[50]:


# Merging the metrics into a single DataFrame
rfm = recency.merge(frequency, on='CUSTOMER_NAME').merge(monetary, on='CUSTOMER_NAME')

# Renaming columns for clarity
rfm.columns = ['CUSTOMER_NAME', 'LAST_ORDER_DATE', 'FREQUENCY', 'MONETARY']

# Top 5 Customers sorted by Frequency
rfm.sort_values(by='FREQUENCY', ascending=False).head()


# In[51]:


rfm['R_SCORE'] = rfm['LAST_ORDER_DATE'].rank(ascending=False)
rfm['F_SCORE'] = rfm['FREQUENCY'].rank(ascending=True)
rfm['M_SCORE'] = rfm['MONETARY'].rank(ascending=True)

# Combine the RFM scores into a single score
rfm['RFM_SCORE'] = rfm['R_SCORE'] + rfm['F_SCORE'] + rfm['M_SCORE']

rfm.head()


# <b style="color:purple;">Higher RFM scores indicate higher customer engagement.</b>
# <p style="color:purple;">Customers with high scores are typically 
#     <b style="color:green;">the most recent and frequent buyers who spend the most</b>, signaling strong engagement and loyalty.</p>

# <b style="color:blue; font-size:16px;">Customer Lifetime Value (CLV)</b>
# 
# - <p style="color:purple">Average Order Value - <b style="color:green">AOV</b></p>
# - <p style="color:purple">Purchase Frequency - <b style="color:green">PF</b></p>
# - <p style="color:purple">Customer Lifespan - <b style="color:green">CLS</b></p>
# 
# <b style="color:black; border:2px solid green; 
#           padding:5px; background-color: yellow;">CLV = 
#     <b style="color:red;">AOV</b> × 
#     <b style="color:red;">PF</b> × 
#     <b style="color:red;">CLS</b>
# </b>

# In[52]:


aov = round(df['SALES'].sum() / df['ORDER_NUMBER'].count(), 2)
aov


# In[53]:


unique_orders = df['ORDER_NUMBER'].nunique()
unique_customers = df['CUSTOMER_NAME'].nunique()
pf = round(unique_orders / unique_customers, 2)
pf


# In[54]:


# First and last order dates
first_order = df.groupby('CUSTOMER_NAME')['ORDER_DATE'].min()
last_order = df.groupby('CUSTOMER_NAME')['ORDER_DATE'].max()

# Let's merge to get customer lifespan
cls = (last_order - first_order).dt.days
avg_ls_years = round(cls.mean() / 365, 2)
avg_ls_years


# In[55]:


clv = round(aov * pf * avg_ls_years, 2)
clv


# <p style="color:purple;">With this CLV value, we can now estimate the value each customer brings over their lifetime. This is crucial for strategic planning and resource allocation.</p>

# <b style="color:blue; font-size:16px;">Profit Analysis</b>

# In[56]:


# Assuming cost is 70% of the unit price (As it's not available in our data)
df['COST'] = df['UNIT_PRICE'] * 0.7  

df['PROFIT'] = df['SALES'] - (df['COST'] * df['QUANTITY_ORDERED'])

profit_by_product = df.groupby('PRODUCT_LINE', 
                               as_index=False)['PROFIT'].sum().sort_values(
    by='PROFIT', ascending=False)

profit_by_product


# In[57]:


sns.set(rc = {'figure.figsize':(10, 4)})
sns.barplot(data = profit_by_product, x = 'PRODUCT_LINE', y = 'PROFIT', 
            hue = 'PRODUCT_LINE', palette = 'gist_rainbow')
plt.title('Profit by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Profit')
plt.show()


# <p style="color:purple;">From the above Analysis, we can identify 
#     <b style="color:green;">Which Product Lines</b> are the 
#     <b style="color:green;">Most Profitable</b>, allowing us to focus on 
#     <b style="color:green;">High-Margin Products</b>.
# </p>
# 
# - <b style="color:purple;">So, from our graph, we can clearly see that 
#     <b style="color:green;">Classic Cars</b> are the Most Profitable. While, 
#     <b style="color:red;">Trains</b> are at the lower end of the spectrum.</b>

# In[58]:


# Profit over Time
profit_over_qtr = df.groupby('QTR_ID')['PROFIT'].sum().reset_index()
profit_over_qtr


# In[59]:


qtr_labels = {1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'}

plt.figure(figsize=(10, 4))
plt.plot(profit_over_qtr['QTR_ID'], profit_over_qtr['PROFIT'], 
         'p', ms = 15, mfc = 'w', mec = '#05a30b', ls = '-', lw = 3, c = '#06d40a')
plt.title('Total Profit Quarterly')
plt.xlabel('Quarter')
plt.ylabel('Total Profit')

plt.xticks(ticks=profit_over_qtr['QTR_ID'], 
           labels=[qtr_labels[q] for q in profit_over_qtr['QTR_ID']])

plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# <p style="color:purple">From this graph, we can see the overall trend of profits across each quarter. There's an indication of profit fluctuation from one quarter to the next.</p>
# 
# - <b style="color:purple">Specific quarters with peaks or dips might point to seasonal or operational factors impacting profitability, providing an opportunity to investigate underlying causes in low-performing quarters and leverage strategies in high-performing ones.</b>

# In[60]:


# Distribution of PROFIT
plt.figure(figsize=(10, 4))
plt.hist(df['PROFIT'], bins=20, color='#06d40a', edgecolor='black', alpha=0.7)
plt.title('Distribution of Profit')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()


# <div style="color:purple; border:2px solid green; padding:5px; ">
# From this graph, we observe:
#     <ul style="color:green;">
#         <li><b>Shape:</b>The distribution is right-skewed. This indicates that a majority of the observations have lower profit values, with a few outliers on the higher end.</li>
#         <li><b>Central Tendency:</b>The distribution seems to be centered around the 1000-2000 profit range. This could be the typical profit range for this dataset.</li>
#         <li><b>Spread:</b>The distribution is fairly spread out, with values ranging from 0 to over 8000. This suggests variability in the profit levels.</li>
#     </ul>
# This histogram suggests that most of the profits are concentrated in the lower range, with a few instances of significantly higher profits. This could be due to various factors like product demand, pricing strategies, or operational efficiency.
# </div>

# ### Visual Enhancements

# <b style="color:blue; font-size:16px;">Heatmaps</b>

# In[61]:


sales_by_month_and_product = df.pivot_table(
    index='MONTH_ID', columns='PRODUCT_LINE', values='SALES', aggfunc='sum')
sales_by_month_and_product


# In[62]:


plt.figure(figsize=(12, 5))
sns.heatmap(data = sales_by_month_and_product, cmap = 'gist_rainbow', 
            annot = True, fmt = '.1f')

plt.title('Sales by Month and Product Line')
plt.xlabel('Product Line')
plt.ylabel('Month')
plt.show()


# <p style="color:purple;">The heatmap displays the 
#     <b style="color:green;">total sales</b> for each 
#     <b style="color:green;">product line</b> across different 
#     <b style="color:green;">months</b>. The intensity of the color in each cell represents the 
#     <b style="color:green;">sales volume</b>, with darker shades indicating 
#     <b style="color:green;">higher sales</b>. By visually examining this heatmap, we can quickly identify seasonal trends and patterns in product performance.</p>
#     
# <p style="color:purple;">For instance, we can see which months have peak sales for specific product lines, aiding in targeted sales strategies and inventory management.</p>

# ### Conclusion
# 
# <p style="color:purple;">In this project, we enhanced the 
#     <b style="color:green;">Customer Sales Analysis</b> by meticulously cleaning and transforming the dataset, revealing crucial insights into sales patterns and trends. Through various visualizations, including 
#     <b style="color:green;">boxplots</b>, 
#     <b style="color:green;">bar charts</b>, and 
#     <b style="color:green;">time series analysis</b>, we identified 
#     <b style="color:green;">outliers</b>, 
#     <b style="color:green;">seasonal effects</b>, and 
#     <b style="color:green;">customer distribution</b> across regions. The addition of new metrics like 
#     <b style="color:green;">Discounts</b> and 
#     <b style="color:green;">Customer Lifetime Value</b> further deepened our understanding of sales dynamics. Overall, this improved analysis not only showcases the effectiveness of data visualization techniques but also provides actionable insights for strategic decision-making in sales optimization.</p>

# ---------------
