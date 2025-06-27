Step 1: Import Libraries and read CSV file.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()
data = pd.read_csv("medical_records.csv")

Step 2: Exploring the Data and Understanding the Data Structure
print("First few rows:")
print(data.head()) 

print("Column names:")
print(data.columns)

#Display the first few rows of the dataset
#List the names of all columns in the DataFrame

Step 3: Understanding the Statistics
print("\nSummary statistics:")
print(data.describe(include='all'))

Step 4: Filtering Data for Stroke Patients
stroke_data = data[data['Disease_Category'] == 'Stroke']
print("Stroke data summary:")
print(stroke_data.describe(include='all'))

Step 5: Grouping and Analyzing by Disease Category
disease_stats = data.groupby('Disease_Category').describe(include='all')
print("Statistics by Disease Category:")
print(disease_stats)

Step 6: Exploratory Data Analysis
#1. Visualizing Age Distribution by Disease Category (Box Plot)
sns.boxplot(
    x = "Disease_Category",
    y = "Age",
    data=data
)
plt.title('Distribution of Age by Disease Category')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)  
plt.show()

#2. Visualizing Age Distribution by Disease Category (Violin Plot)
sns.violinplot(
    x = "Disease_Category",
    y = "Age",
    data=data
)
plt.title('Distribution of Age by Disease Category (Violin Plot)')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()


