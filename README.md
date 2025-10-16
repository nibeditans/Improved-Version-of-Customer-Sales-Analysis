# Improved Version of Customer Sales Performance Analysis

## Overview
The objective of the project was to analyze customer sales data to identify trends and patterns in purchasing behavior, across different regions and product categories. The main goal was to uncover which customer segments were driving the most revenue, how seasonality impacted sales, and to highlight underperforming products or regions. I also aimed to provide recommendations for improving overall sales strategy — like where to focus marketing efforts or which products to upsell.

The Improved Customer Sales Analysis project enhances the original analysis by leveraging advanced data cleaning techniques and comprehensive insights into sales performance. This project aims to provide actionable insights for strategic decision-making in sales optimization.

- Previous One: [Customer Sales Analysis](https://github.com/nibeditans/Customer-Sales-Analysis)
- Improved Version: [Customer Sales Analysis](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/Improved%20Version%20of%20CSA.ipynb)

Here are the SQL and Power BI parts as well:
- Analysis in SQL: [CSA in MySQL](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/CSA%20in%20MySQL.sql)
- Visualization in Power BI: [CSA Report](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/CSA%20Report.png)

![CSA Report](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/CSA%20Report.png)

You can check out the complete articles I have written on this Project: 

- [Customer Sales Analysis — Python Version (Part-1)](https://nsworldinfo.medium.com/customer-sales-analysis-python-version-part-1-60e5a50be351)
- [Customer Sales Analysis — SQL Version (Part-2)](https://nsworldinfo.medium.com/customer-sales-analysis-sql-version-part-2-648b9a15c184)
- [Customer Sales Analysis — Power BI Version (Part-3)](https://nsworldinfo.medium.com/customer-sales-analysis-power-bi-version-part-3-433c21feb1e7)


This dataset has 2823 sales records and 25 features. Key columns include `ORDER_NUMBER`, `SALES`, `QUANTITY_ORDERED`, `PRODUCT_LINE`, `CUSTOMER_NAME`, `COUNTRY`, and `ORDER_DATE`. I started with data cleaning — there were some missing values in non-essential columns like `ADDRESS_LINE2`, which I dropped, and I standardized the `ORDER_DATE` format.

I also created new features like `Day_of_the_Week` to explore time-based trends. There were no duplicate records, but I did check for outliers using boxplots, especially in the `SALES` column — there were several, but they often reflected high-value transactions, not errors. So instead of removing them, I analyzed them further for potential business insights.

Once the data was cleaned, I started by looking at sales trends across time. I created a `Day_of_the_Week` feature and found that Fridays consistently had the highest sales, likely due to pre-weekend purchases or end-of-week promotions.

I also analyzed seasonal trends, and found that sales peaked during the Fall, suggesting a strong Q4 — possibly due to holiday shopping. To get a broader view, I broke the data down quarterly. Sales were lowest in Q2, but then showed a steady upward trend into Q3 and Q4, indicating possible year-end push strategies or consumer demand cycles.

These initial insights helped me frame deeper questions about product categories and regional performance.

To measure sales performance, I tracked a few key metrics that aligned with business goals.

- First was total revenue (`SALES` column) — that was my primary metric to evaluate overall sales output.
- Then I used average order value (AOV), which I calculated as total sales divided by the number of orders. It helped me understand the average spending per customer.
- I also looked at quantity ordered, which gave me insights into product demand trends.
- To get deeper, I analyzed sales by region, by product line, and over time — like monthly and quarterly sales — to find high-performing segments.

These KPIs helped me identify not just how much was being sold, but where and what was selling the most — which is crucial for business decisions.

## Key Features
- **Data Cleaning**: Enhanced processes, including outlier detection and standardization of date formats.
- **Sales Analysis**:
    - Total sales per product and top-selling products.
    - Seasonal trends analysis with a new "SEASON" column.
    - Average order value per customer.
- **Advanced Visualizations**:
    - Boxplots for outlier detection.
    - Bar charts and line/area charts to illustrate trends.
    - Heatmaps for sales distribution.
 
## Improvements Over Previous Analysis
- **Outlier Detection**: Identified extreme values in sales data using boxplots.
- **Seasonal Insights**: Added seasonal analysis to uncover trends based on the time of year.
- **Customer Segmentation**: Implemented RFM analysis for deeper understanding of customer behavior.
- **Comprehensive Visualization**: Improved data representation using Matplotlib and Seaborn, enhancing the interpretability of findings.

## File Formats:
- [Improved Version of CSA (Jupyter Notebook)](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/Improved%20Version%20of%20CSA.ipynb)
- [Improved Version of CSA (Python)](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/Improved%20Version%20of%20CSA.py)
- [Improved Version of CSA (HTML Doc)](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/Improved%20Version%20of%20CSA.html)

- Presentation in PowerPoint: [View the Presentation PDF](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/Customer%20Sales%20Performance%20Analysis%20Presentation.pdf)
- Analysis in SQL: [CSA in MySQL](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/CSA%20in%20MySQL.sql)
- Visualization in Power BI: [CSA Report](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/Customer%20Sales%20Analysis.pbix)
- CSA Screenshot: [CSA Report](https://github.com/nibeditans/Improved-Version-of-Customer-Sales-Analysis/blob/main/CSA%20Report.png)

One of the most impactful insights came from calculating Customer Lifetime Value (CLV). I used AOV, Purchase Frequency, and Customer Lifespan to estimate how much revenue a customer contributes over time. This gave the business a clearer picture of how much to invest in retaining different customer segments.

Additionally, when analyzing regional sales, I found that over 50% of total sales came from the US, followed by France at around 17%. This suggests that focusing marketing or expansion efforts in these regions could significantly boost overall revenue.

## Conclusion
This project serves as a robust foundation for understanding customer sales dynamics and can be further expanded upon for more intricate analyses. The insights derived from this improved version provide valuable guidance for business strategies and decision-making.

Wanna explore more Projects and Fun Programs? Check out the [Data Analytics Projects Collection](https://github.com/nibeditans/A-Few-Data-Analytics-Projects) Page.😄
