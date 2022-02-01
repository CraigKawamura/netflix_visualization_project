{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')\n",
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date          Open          High           Low         Close  \\\n",
      "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "\n",
      "      Adj Close      Volume  \n",
      "0  19864.089844  6482450000  \n",
      "1  20812.240234  6185580000  \n",
      "2  20663.220703  6941970000  \n",
      "3  20940.509766  5392630000  \n",
      "4  21008.650391  6613570000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')\n",
    "print(dowjones_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the data is from 2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#netflix stock and the dow is represented with monthly data and the netflix_stocks_quarterly is daily.\n",
    "#netflix stock is a single stock pricing vs the dow is a tracking multiple stocks, and the netflix_stocks_quarterly is tracking a single stock by day.\n",
    "#the netflix_stocks_quarterly has an additional column named quarter."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)\n",
    "dowjones_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#dowjones_stocks.head()\n",
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEWCAYAAACJ0YulAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAABMh0lEQVR4nO3deXwU9fnA8c+z2dwhkBDuI+GWQ0BA1LYqVSsoWO+zVal4Vova2lZ7/bQ/9adWe3i19cQTD0QRUMFaT8ADUURU5Jb7DuRONvv8/phJWMIm2SR7Js/79dpXdmdmv/Nkdneemfl+5/sVVcUYY4wB8MQ6AGOMMfHDkoIxxphalhSMMcbUsqRgjDGmliUFY4wxtSwpGGOMqWVJoR4i8i8R+WOYyuotIsUikuS+fkdELg1H2W55r4vIxeEqrwnrvVVEdorI1mivO9ZEZJCIfCYiRSIyVUSmicit7ryjRWRFrGNsiIisE5ETIlDuAd/1SAvc7iY82mRScH8QZe4PulBEForIlSJSuz1U9UpV/d8Qy2rwx6Wq36lqlqpWhyH2m0Xk6Trln6SqT7S07CbG0Qv4FTBEVbsGmX+kiLwpIrtFZIeIvCgi3QLmi4jcKSK73MddIiIB8/9XRJaJiE9Ebq5T9u/cHU/No0xE/CKSV0+s60Rkm4hkBky7VETeCfF/Dbbj+Q3wjqq2U9V7A2eo6vuqOiiUsoOs6wfu93Gvu+0WiMjh7rzJIvJBc8ptCRFRESlxt/UmEflrfTv9cH7Xo839Tv5aRFa636nvROR2EUmJ4DoP+j3HWptMCq5TVLUdkA/cAfwWeDTcKxERb7jLjBP5wC5V3V7P/BzgIaDAXbYIeDxg/uXAacAIYDgwCbgiYP4qnB3v3LoFq+rt7o4nS1WzgDtxdtA7G4jXC1zb+L8VsnxgeRjLQ0SygTnAfUAu0AO4BagI53qaaYS7rY8HLgAuq7tAK/iu34vzvbwIaAecBJwAPBeJlYVje0Vkm6tqm3sA64AT6kwbC/iBYe7racCt7vM8nB9rIbAbeB8noT7lvqcMKMbZiRUACkwBvgPeC5jmdct7B/g/4GNgLzALyHXnjQM2BosXmABUAlXu+pYGlHep+9wD/AFYD2wHngTau/Nq4rjYjW0n8PsGtlN79/073PL+4JZ/gvs/+904poWwzUcBRQGvFwKXB7yeAnwY5H1PAzc3UK4Aq4GLG/m8b3Q/uw7utEtxEknNMocAb7rLrADOcadf7m7vSvd/nQ38F6gGyt1pA+t8X2o/Q6CfW+Yo93V3d7uPCxLnGKCwnv9hsLu+anedhQ19RgHvuwz4GicpfxUQxzrc34D7v68Fzqtn3Qr0D3j9InA/oX3Xc3EOBjYDe4BXAsqZBHyO87taCAwPmPdbYJMb9wrg+Hpimwb8y/3sioB3gXx33gPAPXWWnw1cF6ScAe62HVtnei+cpHxs3d+a+3oy8EHA638AG4B9wKfA0QHzbgZm4Hyn9wHXEPz33B7nAHWLuw1uBZIC1rcA+BvO9+rWcO4bVdWSQp3p3wFXBXzZan7k/+d+8ZLdx9GABCsr4EfxJJAJpAf5obzjftjD3GVeAp52542jnqQQ8MV6us782i8qcAnOUXZfIAuYCTxVJ7aH3bhGuF/4wfVspydxElY7973fAlPqi7ORbX4dATt9nGR4RMDrMQQkjYDpjSWFY9wfVFZjn7e7LWo+09qk4H4GG4Cf4ZxRjMLZcQ+t+10Its2DfF8O2Dbs3zFnAPOAu+uJMxvYBTyBc5SaU2f+ZAJ2QCF8Rme737PDcZJnf/bvMGu2ySic7/2kBrZfbVIAhgBbcRJBzfepoe/6XOB5nDPHZPbvXEfhHLQcASThHKisA1KBQe7n0T3ge9uvntim4SSDY9z3/qNmG+Ec6G3GTZI4B3elQJcg5VwJrK9nHe8Ct9XzuR/wmQA/BTrifI9+5W6rtIDfbhXOGbLH3V43c/Dv+RXg3+427Yxz8HhFwPp8wC/cdaSH+hsM9dGWLx8FsxnnyKauKqAbzg+qSp1rxo11GnWzqpaoalk9859S1S9VtQT4I3BOmCrnfgL8VVXXqGoxcBNwXp3TzFtUtUxVlwJLcZLDAdxYzgVuUtUiVV0H3ANc2NSARGQ48Cfg1wGTs3ASQ429QFZgvUKILgZmuP9rY/4E/EJEOtWZPglYp6qPq6pPVZfgJOqzmhhLUKr6MLAS+Ajne/T7epbbB/yA/Yl7h4i8KiJdgi0fwmd0KXCXqn6ijlWquj6giKOBV3HOsuY08m8sEZE9OEfaj3DgpcCg33W3Dukk4EpV3eP+dt51Z18G/FtVP1LVanXqxCqAI3GO2FOBISKSrKrrVHV1A7HNVdX3VLUCZ9seJSK9VLXmTPx4d7nzcA4EtgUpIw/nyDyYLUDd70xQqvq0qu5yv0f3sD/J1Vikqq+oqj/YvsH9rE/COZspUefy7N/c2GtsVtX73HXUt39pNksKB+qBc0pW119wjr7ni8gaEbkxhLI2NGH+epyjqKAVpU3U3S0vsGwvELhjCWwtVIqzg64rD0gJUlaPpgQjIv2B14FrVfX9gFnFOEfGNbKB4hCSbWDZ6ThHwyFVsqvqlziXAet+fvnAEW6jg0IRKcRJrgdVoLfAwzhnhve5O6/6YvxaVSerak93+e7A3+tZvLHPqBfOpbX6XAksVNW3Q4h/lKrmqGo/Vf2DqvoD5tX3Xe8F7FbVPUHm5QO/qrPNe+GcHazCObO8GdguIs+JSPcGYqtdv3twsBtnu4Hz3fip+/ynOJd8g9mJk7CD6YZzea5RIvIrEfnabShQiHMpKPB33dh+IR9nX7AlYLv8G+eMIdQyWsSSgstt4dEDOKh1h3sU9itV7QucAvxSRGqOPurbiTW2c+sV8Lw3ztnITqAE5zJDTVxJHHiU0li5m3G+WIFl+4BgR0cN2enGVLesTaEWICL5wH+A/1XVuj/G5Rx4hjKCplfcnoGzA3inCe/5H5yj1MDktgF4V1U7BDyyVPUqd37IiSoYEcnC2bE/CtwsIsHORg+iqt/gXB4ZVk8cjX1GG3DqNOpzJdBbRP4WSjwNhVrP9A1Aroh0qGfebXW2eYaqTgdQ1WdV9Qc4/5viNCaoT+1vyd3WuTi/A3AuP54qIiNw6mVeqaeM/wK9RGRs4ES3ld2ROJeQoM7vk4ADBxE5Gqcu5BycS38dcM5UAs9+626ruq834Jwx5QVsl2xVHdrAe8KqzScFEckWkUk4LQyeVtVlQZaZJCL93Usb+3BOb2ua3G3DuX7fVD8VkSEikgH8GecSSDXONeE0EZkoIsk4FYepAe/bBhRIQPPZOqYD14tIH/cHcjvwvKr6mhKcG8sLwG0i0s7dwf8S50fWKBHpgfNDe0BV/xVkkSdxkmsP9yjwVzg7wJr3J4tIGs531CsiaUEur10MPNmUswv3KPR5YGrA5DnAQBG50F1vsogcLiKD3fnN/Yxr/AP4VFUvxbnGHmx7ICKHuEeaPd3XvYDzgQ8D4uhZ00QyhM/oEeAGERntNrfs7y5Towin8cIxInJHC/6/oFR1C85Z4oMikuNu12Pc2Q8DV4rIEW5sme53vp0494AcJyKpOJXrZez/vQVzsjhNeVOA/wU+UtUNbgwbgU9wzhBequ9yi6p+i/O5PCNOc+okERmKcxlxIc7BDTgV42eISIZ7FjwloJh2OAdgO3C+s3/iwLPhYA74PbvbbD5wj7tv8ohIPxE5tpFywqc5FRGJ/sCp0CrD+VHsBRYBV+PW8Ov+CqyaisPr3feUABuBPwYsdypORV0hcAN1Ktp0f0VZ3YrmmtZH+3Cu0+YFLD8Z5zrmdrfMdeyvaO6IczazB1gSUF5g66M/4Rxx7MDZQeQEi6Pue4Nspxz3/Tvc8v7E/kq7cTRQ0YxzRK44l4lqHwHzBbgL50h/t/tc6mx/rfOYHDC/B84PsH99MdT5vAMbA/TC2dm8EzBtEM4OewdOZe9/gZHuvAHsbyXzSrDtRv2tj07FOXKvaV2WhXMp8idB4uyBs5PfhPNd24Rz6SDbnZ/ixrgb2NnYZ+TOvxKn9U4x8CVwWN1tgnNkvRTnjC7Y9qutaK4zPdj36YBpbtlP4Oz89gAzA5adgLPDLsT5vr+Is2MdjvPbKHL/1zm4lc5BYpjG/tZHxTgtoPrUWeanbkw/bOR74sE50l+Fc7SubkztA5bJw9lpF+G0ArqZ/RXbSThng/vc/+c3NN5IJNjvuT3wT5x9zV7gM9yWYQRpbBDuR00LGmOMaZXcs5OngQI9sC6ksff9Gael0DGqWhiZ6OKPJQVjTKvlXoJ9DucegD834/3XAKtU9Y2wBxenLCkYY1olt05oMc6lsQnqNPk1jbCkYIwxplabb31kjDFmv4TuwCovL08LCgpiHYYxxiSUTz/9dKeqBr1LO6GTQkFBAYsXL451GMYYk1BEZH198+zykTHGmFqWFIwxxtSypGCMMaaWJQVjjDG1LCkYY4ypZUnBGGNMLUsKxhhjallSMMaYMGkN3QZZUjDGmDAoLi7m5JNP5oEHHoh1KC1iScEYY8Jg69atlJSU8Pzzz8c6lBaxpGCMMWGwe/fuWIcQFpYUjDEmDLZs2VL7PJHrFiwpGGNMGKxevbr2eWCCSDSWFIwxJgy+WLqUDPf5smXLYhpLS1hSMMaYFtq2bRtr1q7le0CWx8OCBQtiHVKzWVIwxpgWeu211wA4FBjq97Pggw8oLCyMaUzNZUnBGGNaoLi4mBkvvshAIBdhLODz+RK2aaolBWOMaYFHH32U4uJijnNfd0Y4FHjh+efZsGFDLENrFksKxhjTTIsWLeKll15iLLAUeA2nKeoEwOv3c8vNN1NRURHLEJvMkoIxxjTD6tWrueXmm+kmwonAFvcB0A7hdL+fb1eu5Pbbb8fv98cw0qaxpGCMMU20Zs0arr/uOrwVFVygSgpy0DKDcZLF22+/zR133EF1dXX0A20GSwrGGNMES5cu5Zqrr6a6qIjJfj8dgiSEGkcj/BB44403+NOf/kR5eXn0Am2miCUFEeklIm+LyNcislxErnWn54rImyKy0v2bE/Cem0RklYisEJHxkYrNGGOaY/bs2Vx/3XWklZZxmd9PpwYSQo3jEE4GPnj/fa65+mq2bdsW+UBbIJJnCj7gV6o6GDgSuFpEhgA3Am+p6gDgLfc17rzzgKE49TQPikhSBOMzxpiQlJWVcfvtt/OXv/yF/Go/l6ufnBASQo2jEC4Avlu1iik/+xmLFi2KXLAtFLGkoKpbVHWJ+7wI+BroAZwKPOEu9gRwmvv8VOA5Va1Q1bXAKmBspOIzxphQrFixgksvuYR5b7zBOOAilPQmJIQahyBcoUpmSQm//e1vuffee+OyZVJU6hREpAA4DPgI6KKqW8BJHEBnd7EeQGCj3o3uNGOMiTqfz8cTTzzBlVdcwd4tW5gMHI/gaUZCqJGHcJkqRwIzZszg0ilTWLFiRbhCDouIJwURyQJeAq5T1X0NLRpk2kH9z4rI5SKyWEQW79ixI1xhGmNMrdWrV3PlFVfw6KOPMsTv52q/n74tSAaBkhEmIlwM7Nm4kSuuuIKHH36YysrKsJTfUhFNCiKSjJMQnlHVme7kbSLSzZ3fDdjuTt8I9Ap4e09gc90yVfUhVR2jqmM6deoUueCNaQN2794d9xWf0VRVVcVjjz3GpVOmsGn1as4DzkHICFNCCNQf4Rq/nxF+P0899RRTLrmE5cuXh309TRXJ1kcCPAp8rap/DZj1KnCx+/xiYFbA9PNEJFVE+gADgI8jFZ8xbZ2qctppp3H22WezZ8+eWIcTc19//TWXXnIJ06ZNY6jfzy/8foZGIBkESkc4A+FCoHDjRn7+859z//33x7TpaiTPFL4PXAgcJyKfu4+TgTuAH4nISuBH7mtUdTnwAvAV8AZwtaomxt0exiSgsrKy2ufbt29vYMnWraKign/9619cdeWV7NqwgZ8CZyNkRjghBBronjWMUeWFF15g8kUXsXTp0qitP5A3UgWr6gcErycAOL6e99wG3BapmIwx++3du7f2+b59DVX3tV6rVq3iz7fcwrr16xkNTFAlLYrJIFAawo+BQ1Fe2b6dqVOncu6553LppZeSkpIStTjsjmZj2qjAgeZby6DzoVJVZs2axRWXX86uDRu4EDgNiVlCCNQH4efuWcNzzz3Hz6+6KqrDe1pSMKaNCmy915Za8lVXV3PPPfdwzz33UODzcbXfz8A4SAaBUhF+jHA+sGHVai6bMiVqQ3xaUjCmjQpsdbR169YYRhI9qsodd9zBq6++yg+An0JY6g5eQ2t7SX0Ure1Cu6WGIFyhfpJLS/nlddfx5ZdfhqXchlhSMKaN2rRpE5IikAsbN26MdThRMXPmTObNm8dxwPgW3ogWaAtQ4T7Wsb8L7XDoiHCp309WdTW/v+mmiNf/WFIwpo1at24d2k7xt/OzZt2aWIcTcRUVFTz6yCP0B8bFOpgmykI41++ncO9eXnzxxYiuy5KCMW2QqrJy1Ur82X5oD4W7CxN2oPlQrVy5kuKSEg4HJM7qEELRDaEX8OnixRFdjyUFY9qgLVu2UFJcAjmgOc7173jrgyfcPB5nd5c4Y6AdTBGc+4Ijx5KCMW1QTYWldlTIAYSoVGLGUv/+/clp356PAH+YKoJrlAPp6emcddZZpKenE4n7kTegbEA54sgjI1D6fpYUjGmDlixZ4lQytweSgRxY8tmSWIcVUSkpKVx2xRWsA/4b5rLLgYkTJzJ16lQmTpwY9qRQhPKix0OnvDzOOOOMMJd+oIjd0WyMiU+qykcff4S/k7+2zwF/Zz/Lly+nuLiYrKys2AYYQRMnTmT58uXMnTsXD8oPCU/9Qhowd+5ccP+2b3GJ++1FeUI8lCUn84/bbov452NnCsa0MStXrmTXzl1ot/2XULSb4q/289FHH8UwssgTEW644QZOOukk3sbphbM6DJeS0nD6kpoxYwZlZWWktbhEx1aUhzweilNT+MvddzN48OAwlVw/SwrGtDHvvPMOCGj3gJ1hR5B0cea1cklJSdx4441ceOGFLAaeRigPcx1DOKxEeUSElA4dePCf/2TEiBFRWa8lBWPaEL/fz/w356OdFVIDZghU96hm4cKFFBUVxSy+aBERLrvsMn7zm9+wxiM8JkJxHCWGz1GeBnr26cO/H36Yfv36RW3dlhSMaUM+++wztm/bjhYcvAPUfKWqqor//jfc1bDxa9KkSdx5553s9np53OOhJA4Sw2coLwEjDzuMBx58kGgPJmZJwZg2ZNasWUiqoD2C7PxyQDoIL7/yMqqx3zlGyxFHHMFdd99NYVIS00XCUsfQXGtRXgFGjRrFnXfdRUZGRtRjsKRgTBuxfft23nv/ParzqyEpyAIC1X2rWbN6DV988UXU44ulww47jBtvuon1qrwfoxgqUF7yeOjRsye33XYbqampjb8pAiwpGNNGvPTSS/j9frR//UfCmq9IqvDcc89FMbL4cMIJJ3DMMcfwgQhlMThb+ATY6/dz4003kZmZGfX117CkYEwbUFRUxMuvvIy/px8a2t94nbOFBQsWsG7dumiFFzcuuOACKlT5JgbrXioeDh02jEMPPTQGa9/PkoIxbcDMmTMpLytHD2n8CFgHKOIVnnrqqShEFl8OOeQQMtPTiXZH4pUoW9XP2COOiPKaD2ZJwZhWrqSkhOeef865Wa3DgfPkc0E+r3NHb6pztvCf//yHDRs2RC3OeODxeOjStSvRHrG6phFwly5dorzmg1lSMKaVmzFjBiXFJfiHHNw/qBQKUnhwNw86SCEJpk2bFoUI40tKaiq+KK+zZn2xqlwOZEnBmFasqKiI6c9Nd84ScpvwxrT9Zwvr16+PWHxxSTVmoy3EQ1NgSwrGtGIvvvgipSWl+Ic1fRSBmrOFxx9/PAKRxS+PxxP1MRdqUkHNmA+xFPsIjDERsW/fPp5/4XnnRrUOzSggDar7V/P222+zdu3acIcXt7Lbt6c0wgPZ1FXq/m3Xrl1U1xuMJQVjWqkZM2ZQVloWtC4hVDpQwQtPPPFEGCOLb71792YnUNWEexW64XQllQoUuK+bYov7Nz8/v4nvDD9LCsa0QsXFxS07S6jhtkR6++23+e6778IVXlw7/PDDqVLl2ya852SEbjjJYArCyU2slVguQkF+Pnl5eU16XyRYUjCmFZo9e7ZzljC45VfHdaCCB6ZPnx6GyOLf6NGj6dqlC++KhH3YzmBWo2xQ5cennhrxdYXCkoIxrYzP5+OFF1+AzjjjL7dUGlTnVzNv/jwKCwvDUGB883q9XHHllWxRZUGE11WO8qrHQ/euXTnllFMivLbQWFIwppVZsGABu3buonpAddjK1AGKr8rHnDlzwlZmPDvuuOM49phj+A+wKkJnC36UGUAh8Ls//CEu7lEASwrGtDpz5s5BMqTptZ0NyQY6OWXHQ1v6SBMRbvrd7yjo04fpInwX5sTgR5kFrACuvfZahg8fHtbyWyKkpCAi6SIyKNLBGGNaprCwkE8+/oTqXtWE+w4sf76fzZs28803seguLvoyMjK4+5576NS1K0+KsC5MiaHaHTNhCTB58mROP/30sJQbLo0mBRE5BfgceMN9PVJEXo1wXMaYZli4cKHTPXav8B/Naw+nwvm9994Le9nxKi8vj3vvv5/O3bvzpAjftjAx+FBeAD4DLrnkEi655JKwxBlOoZwp3AyMxbn0hap+jtMU1xgTZz7++GMkXVrWDLU+KUBH+PiTjyNQePzq1KkT9z/4IPl9+/IMwhfNTAwVKE8jfAVcc801TJ48OaxxhksoScGnqnsjHokxpsWWLltKdV5ol47kc3EO9QrB847n4N5Sg/B38rNq5SrKyspaGmpCycnJ4b777+fQ4YcyA1jcxMRQhvKkCGs9wk033cQ555wTmUDDIJSk8KWIXAAkicgAEbkPWBjhuIwxTbR371527dgVcjNUKRSkyn3sCN5bal2ao6gqq1evbmG0iSczM5O777mHsWPHMovQE0O5mxA2ezzccsstnHTSSZENtIVCSQq/AIYCFcCzwF7gugjGZIxphk2bNgGg7SLYOqjdgetqa1JTU7nt9tsZO3YsrwJfNZIYqlGmI2wW4ZY//5ljjz02OoG2QKNJQVVLVfX3qnq4+/iDqpZHIzhjTOh27tzpPEmP4ErS66yrDUpJSeHWW29l0KBBvCTCjgYSwzxgDcpvf/tbjj766OgF2QKhtD56U0Q6BLzOEZF5EY3KGNNkJSUlzpPkCK4kCRAoLS1tdNHWLC0tjdv/7/9Iz8ripXq6w1iDsgg488wz4/6SUaBQLh/lqWphzQtV3YNzA32DROQxEdkuIl8GTBspIh+KyOcislhExgbMu0lEVonIChEZ38T/wxhTI5K9PovzaAs3sDUmLy+PqdddxyZVvqgzT1HeEKFr585ceeWVMYmvuUJJCn4R6V3zQkTyIaQalmnAhDrT7gJuUdWRwJ/c14jIEOA8nLqLCcCDIpIUwjqMMa7kZPcUIXy9WxzM7zxSUlIiuJLEcfzxx9MnP5+FdcZfWAtsUWXyJZfETfcVoQolKfwe+EBEnhKRp4D3gJsae5OqvgfsrjsZ54Z5gPbAZvf5qcBzqlqhqmuBVTj3RhhjQtS+fXvnSUUEV1Lp/MnOzm54uTbC4/Ew8ZRT2KJ6wLjOXwJpqakcf/zxsQqt2byNLaCqb4jIKOBInJPH61W1ubVM1wHzRORunIT0PXd6D+DDgOU2utOMMSHq3Nm5qiulgkaqy2e32qJLly6RKT8BjR3rHL+WA1nutPUeDyMPOyzhzhKggTMFETnE/TsK6I1zVL8J6O1Oa46rcJJKL+B64NGa1QVZNui3WkQud+sjFu/YsaOZYRjT+nTr1s0Z47cocuuQIuen2qOHHbPV6NWrF8leb81JFH6UnX4//fr1i2lczdXQmcIvgcuBe4LMU+C4ZqzvYuBa9/mLwCPu841Ar4DlerL/0tKBK1Z9CHgIYMyYMVbbZYwrJSWFHj178F3hd5E7U9gL3mQvPXv2jEz5CSgpKYmOubkUbd8OOCdTfvafuSWaes8UVPVyEfEAf1DVH9Z5NCchgLOjr7l74zhgpfv8VeA8EUkVkT7AAKBtdbBiTBgMGTyEpMKk0JqCVEF6ejpnnXUW6enpUNX4Wzx7PAwYMACvt9Erz21K+w4dqBnjrqaxbm0dT4JpsKJZVf3A3c0pWESmA4uAQSKyUUSmAJcB94jIUuB2nDMRVHU58ALwFU5vrFeraiTbUBjTKg0dOhR/mb/22n+DqmDixIlMnTqViRMnNp4UqkF2C8OGDgtHqK1KVrt2tUmhpp4/MzMzVuG0SCjpfr6InAnM1CY0TlbV8+uZNbqe5W8Dbgu1fGPMwUaMGAGA7BA0q5GfazLMnTsXcP82Vie6B7Ra42pAmHiRmZl5UFLIyMiIVTgtEkpS+CWQCfhEpBynUlhV1dqkGRNnCgoKyG6fTeH2QujTyMLJUFZYxowZM5zXWQ0vLtsFEWHkyJFhiLR1aRdwplBz+ShRm+2G0vdRO1X1qGqKqma7rxPzvzWmlRMRRo8ajXenN7R6hSbw7PDQt1/fhL1WHkm5ubm19wzWXLnLyQmxu9o401CT1AEiMktEvhSRZ0XE2qAZkwDGjBmDv9Qf3qapPpCdwpjRY8JYaOvRqVMnADridCOdmpJCu3btYhpTczV0pvAYMAc4E2f0uPuiEpExpkVGjXJuI5LtYewEaReoXxk9OmiVYJvXrVs3AEbidOPQrWtXRCLZCVXkNJQU2qnqw6q6QlX/gg3BaUxC6N69O3md8iCM93bKdsHj8Vglcz1q7tvYBez2eOjZu3fDb4hjDSWFNBE5TERGuXcwp9d5bYyJQyLCqMNG4d0VvnoFz04PAwYOSNgWNZHWpUsXvF4v24FdqvRO4KTQUOujLcBfA15vDXjd3DuajTFRcOihhzJ//nyn1rORVkWN8oPsEUYcNyIcobVKXq+Xnt27s/K776hurUlBVX8YzUCMMeEzdOhQwLnZrNH7FRpT6NyfMGyY3bTWkF75+bz/3XfO8169Glk6foXSdbYxJsEUFBSQnJJ8cOf1zSB7nArTQw45pOWFtWKB/UElct9QlhSMaYW8Xi99+/RF9oahBUwhZGRmWHfZjejatWvt8w4dOsQukBaypGBMK9WvXz+Silo+gKFnn4d+/folbBPLaMnLy6t9nsjbqtGkICJ/rvM6SUSeiVxIxphwyM/PdzrHq2x82YZ4ijwU5BeEJabWLDc3N9YhhEUoZwq9ReQmABFJBV5mf5fXxkSVquL3+xtf0Oyv7GzJnc2V4K/wJ3TFabQkal9HdYWSFH4GHOomhtnA26p6c0SjMqYed911J+PGjeP111+PdShxr2Z0NClpwaUMtyOf7t27hyGi1i0vL48unTszZcqUWIfSIvU2Sa1zg9o/gH8DC4B3RWSUqi6JdHDG1LXk008BWLp0KSeddFKMo4lvtRXDoYytUB/3vYGVqCa49PR0XqzpcTaBNXTzWt1hOPcAQ9zpdvOaibry8nK2bnOGPFy3bm2Mo4l/GRkZZGZlUlTa/OtHUuqcZVhSaDvs5jWTMFauXImq0jm9mtWrVuHz+WxYyEZ06dKF4tLi5o/ZXAopqYnb46dpulBaH90uIh0CXueIyK0RjcqYIJYsca5YTswvp6Kyiq+//jrGEcW/rl264ilrfstzKRM6deqU0E0sTdOE8m05SVULa16o6h7g5IhFZEw9Fi5cQN/2fo7sUkWSwIIFC2IdUtzr3LkzUtb8HbqUCl272KWjtiSUpJDkNkUFQETSaXw0V2PCatOmTXz99TeM6VROZrIyJLeKt/7zpjVPbUSXLl3wV/ihqnnv95R57E7mNiaUpPA08JaITBGRS4A3gSciG5YxB5o9ezYege93de7EOqZbBdu272Dx4sUxjiy+1VYQlza8XFDV4C/z1w4gY9qGUMZovgu4FRiM0/rof91pxkRFaWkps1+dxei8SjqmORWmYzpX0SEVnntueoyji2+1O/TiZry5pE4Zpk0ItQbqM+Bd4B33uTFRM3PmTIqKS5hUUF47LdkDE3qVsnjxpyxfvjyG0cW3mt46pbgZ9QrFB5Zh2oZQWh+dA3wMnAWcA3wkImdFOjBjAIqKipj+7DOMyKuiX/vqA+ad0LOC7FR46KF/oxqmIcZamezsbNplt2tWVxdS5CQS6+KibQnlTOH3wOGqerGqXgSMBf4Y2bCMcTz55JMUF5dwTr+yg+aleeG0/FI+++xzFi1aFIPoEkOfgj549h38U9cOiia7j06KdqiTWPdB+w7t7R6FNiaUpOBR1e0Br3eF+D5jWmTDhg28NGMGx3SvIL9dddBljutZQbdM5YH77qOqqplNbFq5vn37Okf9dfb5OlKhA9AB/OP8zusASfuS6N+vf7TCNHEilJ37GyIyT0Qmi8hkYC5gvZGZiHvggfvxip+zg5wl1PB64IIBxWzYtImXX345itEljn79+qGV2rQWSH5gL/Tvb0mhrQml9dGvcTrDGw6MAB5S1d9EOjDTti1evJiFCxdxakEJHVL3H8E+tSKdp1akH7DsyI4+hnf08fhjj1JYWBjlSOPfwIEDnSd7mvCmfc64zAMGDIhITCZ+hVLRfKeqzlTVX6rq9ar6sojcGY3gTNtUXV3N/ffdS6cMmNC74oB564uSWF9nNDER+MmAEsrKypg2bVoUI00M/fr1IykpqXas5VDYuMxtVyiXj34UZJr1WWwi5s0332TN2nWc07eY5BBrr3pk+RnXvYJZs15h06ZNkQ0wwaSkpNC3X19kdxOape6G9Ix0a47aBtX7kxORq0RkGTBIRL5wH8tEZC3wRfRCNG2Jz+dcBirI9nNEl6ZVHJ/et4wklMcffzxC0SWuYUOH4dnjOaiyuT5Je5IYOmQoHo+1KWlrGvrEnwVOAV51/54CTAJGq+pPoxCbaYPmzZvHlq3bOLNvCZ4m3m+Vk6qc0LOM/7z5Jhs2bIhMgAlq6NChaJXC3hAW9oEWKkOHDo14XCb+NJQUqoBNqnq+qq4H0oAzgHHRCMy0PdXV1Tz79NMUZPsZ2dHXrDJO7l1OkijPPvtsmKNLbEOGDAFAdoWQaXcDuv89pm1pKCm8ARQAiEh/YBHQF7haRO6IfGimrVmwYAEbNm1iUu9Smtt9f4dU5ZhuFcyf9wa7du0Kb4AJrEePHs6dzbsbX7am7sGSQtvUUFLIUdWV7vOLgemq+gucSuaJEY/MtDnPTX+WThlweOeW3YR2Un45Pl81M2fODFNkiU9EGDZ0GEl7khpfdpfQvWd32rdvH4XITLxpKCkEVkkdh9NlNqpaiXNrizFhs2zZMr5c/hUTepaS1MK6za4ZfkZ3quSVl2dSWtqcPqNbpyFDhqB7teGxFdSpZB42ZFjU4jLxpaGf3xcicreIXA/0B+YDBA7NaUy4TH/2WTJThGO7VzS+cAgm5pdTVFzCnDlzwlJeazB48GDnSUM3sZU5YyjULmvanIaSwmXATpx6hRNVteaQawhwd4TjMm3I6tWr+WDBAk7sUUqaNzxlDuhQzSE5PqY/+wwVFeFJNImu5s7mBm9icxPGoEGDohCRiUf1JgVVLVPVO1T1WlVdGjB9oao+1VjBIvKYiGwXkS/rTP+FiKwQkeUiclfA9JtEZJU7b3xz/yGTeB577DHSvcL43uHdeZ/Wp4xdu/cwe/bssJabqDp06EDHTh2hsP5lpFAQEevzqA2L5J0p04AJgRNE5IfAqcBwVR2Ke8YhIkOA84Ch7nseFJHGa8RMwlu+fDnvv/8+J/UuJSs5vGMiDM3xMTjHx5NPTKOkpCSsZSeqgf0HkrS3/p+W7BW6de9GWlpaFKMy8SRiSUFV3+PgBnBXAXeoaoW7TE2X3KcCz6lqhaquBVbhjNtgWjFV5f777qN9qnN/QbiJwHn9Syncu49nnnkm7OUnor59+6JFWm9TEc8+j3WX3cZF+x72gcDRIvKRiLwrIoe703sAgbegbnSnHURELheRxSKyeMeOHREO10TSf/7zH5Z/9RVn9y0JW11CXf3aV/P9rhU8//xzbN68OTIrSSAFBQVOQgg2ZrMftFidZUybFUovqbNF5NU6j6dE5FoRaeo5phfIAY4Efg28ICICBKv5CnotQVUfUtUxqjqmU6dOTVy9iRelpaU8+MD99M32c0z3yoiu69z+ZSRpNffdd29E15MIaofWDJYUigG14TfbulDOFNbgfF0edh/7gG04R/0PN3F9G4GZ6vgY55glz50e+E3sCdhhXSv25JNPsmv3Hi4aVNzkPo6aKjdNOa2ghAULFvLRRx9FdmVxrnv37gBIcZCN7la79OgR9CTdtBGhJIXDVPUCVZ3tPn4KjFXVq4FRTVzfKzg3wiEiA4EUnGavrwLniUiqiPQBBgAfN7FskyA2b97Miy88z9HdKujfPvgwm8E8tSK9djyFWxdnHTTYTkPG966ga6Zy373/wOdrXr9KrUH79u1JTUsNOgqblDiJomvXrlGOysSTUJJCJxHpXfPCfZ7nvqz3vF9EpuP0lzRIRDaKyBTgMaCv20z1OeBi96xhOfAC8BVOn0tXq2roewuTUB555BFEGx5mM5j1RUmUVXsoq/bwTWHyQYPtNCTZA+f1K+G7DRt54403mhpyqyEidO7cGSkNcqZQCklJSeTm5kY/MBM3Qqne+xXwgYisxrn23wf4uYhkAk/U9yZVPb+eWUG73VbV24DbQojHJLANGzbw1ltvMbF3Gblp4W2C2pjRnaro176aJ5+YxoQJE/B6I1S7Hec6d+rMhnVBuhYvh9yOuTaGQhsXyhjNr+FczrnOfQxS1bmqWqKqf49odKbVmTlzJkminBSBJqiNEYFT8svYum07CxYsiPr640XHjh3xVBz805dyoWNuxxhEZOJJqIcEo3FuLBsOnCMiF0UuJNNa+Xw+3pw/jzGdKmmfGt2zhBqH5VWRkwbz5rXdS0gdOnRAyw/e/p5KDzk5OTGIyMSTRs+fReQpoB/wOVBznV+BJyMXlmmNvv76a/YVFTO2ILJNUBuS5IExeeW8/8knVFVVkZycHLNYYiU7Oxv16f5fs0sqxbrLNiHVKYwBhqhqbA7tTKvx1VdfATAoJ7atfwbl+HhzYyVr1qxpkx2/ZWVlOU/qdKGtlbp/nmmzQrl89CVgbdRMi23atInMZKF9SmyPL7plOH08bNmyJaZxxErQpKCgVUpmZmZMYjLxI5SkkAd8JSLzAu9qjnRgpvUpKysjvQWd3pX5hPT0dM466yzS09Mp8zXvrrcMrxNDWx2AJz3dvb8j8ITNvZSUkZER9XhMfAnl8tHNkQ7CtA0pKSlUVTf/9uVSnzBx0kSmTp0KwLtznm9WOZX+/fG0RbU9oAYmBfd5ampq1OMx8aXRpKCq70YjENP6de7cmb0VSrmPZnWAl+FV5s6dC8DcuXPp7G3eWcf2Mk9tPG1R7Y4/sKK5us4802bVe/lIRD5w/xaJyL6AR5GI7IteiKa1qBn5a/W+5t00lu5VysrKmDFjhnMpqplJYfVeLyJCv379mvX+RFd7hhTYfXYbP3sy+9X761TVH7h/20UvHNOajRgxAm9SEp/tTGZobuxaIH22M5Uhgwe32UrV2ma4QZJCW2yiaw4UStfZ/UQk1X0+TkSmikiHiEdmWp2MjAyOPOooFm5Lo6qeQV4izelQz8PxJ5wQmwDiQE33HuIPqN/xHzjPtF2htD56CagWkf7Aozh9Hz0b0ahMq3XaaaexrwIWbInNZYrX1qeSlprC+PFtdxjw2h2/nSmYIEJJCn5V9QGnA39X1euBbpENq/VYvnw5p5zyYx566KFYhxIXDj/8cAYNHMAr6zKpjHI/uBuKPSzalsppp59Bu3Zt96pobVIIrJJxk4J1hmdC+QZUicj5wMXAHHeaHU6E6NNPP2Xv3kLmz38z1qHEBRHhyqt+zs4yeG199AaHV4Wnv80kIyODn/zkJ1FbbzxKSnK7HA88U3AThF0+MqEkhZ8BRwG3qepadxCcpyMbVuvxzTffALBz5442e7NUXaNHj+bYY49l1voMtpZG58h04dYUlu/2culll7f5/n0aOlOwpGBC6Tr7K+AGYJmIDAM2quodEY+sFaisrOTTT5fgT22H3+/n008/jXVIcWPq1Kkkp6bx2NeZ+CPc68W+SuHplZkMHnwIp556amRXlgBqzxQCt7vWmWfarFBaH40DVgIPAA8C34rIMZENq3V4//33KSsrpTL/KCQlnbmvvRbrkOJGp06duPrqa/hqj5e3N0W20vnJFRmUVSdx44032U6Phi8f2fYxoZy73wOcqKrHquoxwHjgb5ENK/H5fD6mPfEEpHegukMvKjodwsIFC1ixYkWsQ4sbkyZNYvSoUTy3Kovd5c3v/qIhS3Yk8+G2FC6ePJk+ffpEZB2JpqHWR3b5yISSFJJVtXZPpqrfYhXNjZo+fTrr162jvOdoEKGq66FISgZ33nUXlZWxG08gnogIv/7Nb6gWL09/G/6O2Cqq4clvs+hTkN/mK5cDBUsK4vZJZXc0m1CSwmIRedS9cW2ciDwM2MXxBnz44Yc88sgj+Dr2pTqnwJnoTaEs/3usWrmSe+65BxuewtG9e3cuvOgiPt6eworC8F66eH19GjvL4Ppf/sqOgAN4PB5ne9iZggkilKRwFbAcmApcC3wFXBnJoBLZokWL+P3v/4A/syMVfX7gDAzsqs4toLLHYbz++uv89a9/pbo6yg3149S5555Lbk4HZq4J39lCmQ9e25DOD77/fUaOHBm2cluL5JRk6xDPBBVK66MKVf2rqp6hqqer6t9UtSIawSUSVeX555/npptuojIlm9KBEyAphZT1i0hZv6h2uaoeo6jsNpxZs2bx2xtvZN8+61swLS2Ns885l+W7vWwqqf8rmd+umvQkP+lJfg7pUEV+u/qT6oKtKZRWwU8vvDASISe8lNSUoOMp1HarbdqshnpJXSYiX9T3iGaQ8W7r1q3ccMMNPPDAA1S270Xp4ImQ7Py4PCW78JTs2r+wCFW9x1JR8H0++WQxF150MQsXLoxR5PHjpJNOQkT4cGv917QvHFRGfrtq8ttV84cxxVw4qKzeZT/clkpBfj6DBw+ORLgJLz0t3cZTMEE1dAFxUtSiSFBlZWU8//zzPPX00/iqlYqC7+HrPPiAS0b18XUZTGlWJ3TNu9x444187/vf5+qf/5xevXpFIfL4k5uby8CBA/h6+1dAeYvKqvLDyr1ezpnwPSSEz6ItysjIQEoDto3POXuwJqmmoaSQDHRR1QWBE0XkaGBzRKOKc2VlZcyePZunnn6GvYV78OUUUJl/JJratEHP/Zl5lAw9jeStX7Loo4/5cNEiJkyYwIUXXkiPHj0iFH38GjhwEO+uW9nicraXeqj2Q//+/cMQVevUrl072Aua4zZ4qIKMTBuK0zScFP4O/C7I9DJ33ikRiCeu7dq1i1mzZjHjpZkUF+2jOrsblUMm4W/XtfmFepKo6j6Cqk4DSNm8lNffmMfrr7/OuHHjOOeccxg6dGj4/oE4l5ubS1GF4lfwtOAAf2+lp7Y8E1y7rHZ4fB58I53rRp6FHrIym3ZQY1qnhpJCgaoeVHegqotFpCByIcUXVeWLL77glVde4Z133qG62o8vpxdVQ45pWTKoKzmDyvyjqOo2Au/WL3nn/YW8/fbbDBw0iDNOP53jjjuu1VcCJiUlEY6Gun67O7dR2dnZSGVA5q2C9p3adp9QxtFQUmhoD5Qe7kDize7du5k3bx6z58xh44YNiDeVyrxDqOo6BE2L3I9HUzKo6j2Wqh6H4d2xkm83fM0dd9zBP/5xL+PHn8jEiRMZOHBgq7xWXlFRQZKnZWcJAClJTlawmwTrl52djVbuT8GeSg8dOnSIXUAmbjSUFD4RkctU9eHAiSIyhVZ685rP52PRokW89tprLPrwQ/zV1fjbdaGq7zH4cvtAUhRv5E5Kxtd1CL4ug/EUbaNqxzfMenUOr7zyCgV9+jDx5JM58cQTycnJiV5MEbZv3z6yklue7DLdsZuLiopaXFZr1b59e9SnTqsjL0iltPneY42joaRwHfCyiPyE/UlgDJCCM+BOq7FmzRrmzp3LvHnz2bdvL5KSQUXnIfg6DUTTY7zTFcGf3ZXK7K5U5lfg3bWGtTtW8sADD/DPf/2Lo448ipNPPomjjjoq4e9GLSoqIjO55ReQasrYu3dvi8tqrWoPJiqAJPCX+1vVAYZpvnr3Iqq6DfieiPwQGOZOnquq/41KZBFWXl7Of//7X155ZRbffPM1eDz42vfGN/AIqjv0BInDEai8qfi6DMbXZTBSugfvzm9Z+MkSFiz4gA45OUyaOJFTTjmFbt0Sc2C80tJS0jwtv8s73T1TKCur/z6Gtq42AZTjtDP0Y0nBAA2fKQCgqm8Db0chlqjYuXMnM2bMYNarsykpLoKMDlT0PgJfXn9IDm9VScr6RXhKnRvX0r6agz+zI5X5R4WlbM3Ioar3EVT1PJykvRvYtf0bnn7mGZ555hm+//3vc/7553PooYeGZV3R4vf7Q7nFo1E1RVj/UvWrbZlVkxSw1lrGkdjXG5qgsLCQJ554gldmzaK6uhpfh3yqBrstiCJUaesp2YVUVwGQVLQ1IuvA46E6J5/qnHykohjv9q9Z8NFiPvjgA4aPGMFVV16ZMM1aMzMz2Vzd8hZDpT7n88zIsHb39alJAFIuqHu5rWPHjrEMycSJNpEU5s+fz9/+/ndKSkqoyhtIVfcRaFp2rMMKO03NoqrX4VR1H4l3xwqWff0FV111FaeccgrXXHMN6enx3WisW7duLCgFnx+8Lbh6t7U0qbY8E1xOTo7Tgq0cxOskUUsKBtpAUnjssceYNm0a/nZdKB82Hs1oA9dNk5LxdR1GcadBJG9awuw5c/hmxbfc+4+/k5mZGevo6jVkyBB8flizL4mBHZpft/DNHudrbf0e1c/r9ZKVncXe8r21ewGrUzAQWtfZCevzzz9n2rRpVOUNoGzwxLaREAIlJVPV+wjKB5zAypXf8s9//jPWETVozJgxJCd7WdRAp3iNUYUPt6cyZPBga3ffiLyOeUiZc7aQnJxMVpbd0WxaeVJYuHAhiIfKPt+PTWui6krS09M566yznEs31bG5mao6Jx9fTgEfLFjQ+MIxlJWVxbHHjuODremUVDWvnuerPV42FnuYOMn6c2xMXsc8pMJJCjm5Oa3yhkjTdK06KXTp0gXUT9K+CFXyNkJ8lUycOJGpU6cyceJExBejO2x9lXhLd9G1axi75YiQ888/nzKf8tr6pnfhrAovrcmgY24OJ554YgSia11yc3PxVHiQciEvLy/W4Zg4EbGkICKPich2EfkyyLwbRERFJC9g2k0iskpEVojI+HDEcNJJJ9G7dz7pq94iaedqZ68RRepNYe7cudx7773MnTsX9UZ//Fsp20vGN3PxVBZz5RVXRH39TTVgwACOP/54XtuQwfaypn09P9yWzLeFSVwy5VIbFyAEubm5aJniqfTQMdcqmY0jkmcK04AJdSeKSC/gR8B3AdOGAOcBQ933PCgiLW6bmJGRwT/+8XcOGTSAtNVvk/btfKR0d0uLDV1SCmVlZcyYMcO5kSopiknBV0nyhsVkfvkymZRzxx13JMywlFdddRVJ3hSeWJERch4vqRKeWZXFwAH9OfnkkyMbYCvRoUMH1K9QhNW/mFoRSwqq+h4QbA/8N+A3cECHmKcCz7lDf64FVgFjwxFHx44deeD++7n66qvJqtxNxrKZpH77Jp6irVE/c4gGqSwhecMnZC19npTNn/PDccfw9FNPceSRR8Y6tJB17tyZSy+7jKU7k/lwW2j9TT2/Kp19FcINv/6N9Y4aoppEoNVqScHUimqTVBH5MbBJVZfWqdTqAXwY8HqjOy1YGZcDlwP07t07pPV6vV7OPfdcJkyYwIwZM5jx0kuUfDUHzcyjsvMh+Dr2je5RfLip4tm3heTtX+Pdsx5BOfroY7jwwp8yaNCgWEfXLGeeeSZv/edNnvx2BcNyC2mXUn8C/3qPl/9uSuXcc8/hkEMOiWKUiS0wEVhneKZG1JKCiGQAvweC1QAGa/YQdC+gqg8BDwGMGTOmSYf67du3Z8qUKVxwwQXMnz+fl2bOZN3aD0j77iMqc/vg6zQQf1aXiN3hHG5SUYx350pSdq6E8n1kZmUx8eyzOP300xN+5LakpCR+89sbufTSKUxfmc7lQ0sByG934P0LVX547JssunXtwpQpU2IRasJq165d7fPs7NZ3M6dpnmieKfQD+gA1Zwk9gSUiMhbnzCBwcOKeRHDIz/T0dE499VR+/OMfs3z5cubOnct/3nqLih3fQno2lbn98XUagKa2a7ywaKuuwrt7Hd5dK0na62yikSMPY9KkiRx77LGtqoK1X79+nHPOuUyfPp0f9qhgQIdqLhx0YCd3r69PY0uJ8Jebb2j1gxCFW2BSCHxu2raoJQVVXQZ0rnktIuuAMaq6U0ReBZ4Vkb8C3YEBwMeRjklEGDZsGMOGDWPq1Km89957vPbaa3z22RJSNi2hOrsbvryB7lgKMbz5WxVP8Ta8O74lZc9a1FdFl65dOfmMnzF+/Hi6d+8eu9gi7OKLL2b+vDd4emU1N4/Zd8BJ3N4K4dX1Gfzg+9/jiCOOiF2QCSowEcTzne4muiK2pxOR6cA4IE9ENgL/o6qPBltWVZeLyAvAVzjDflytqi3vQ7kJ0tPTGT9+POPHj2fr1q3MmzePua+9ztY175L23SIqc/tS1WUwmhF60z1/ZsfaXlL9GR3xZzax2V9VOd6dK0ndsQLKCklNTeP4E3/EhAkTGD58OB5Pq77NBHBakE259DLuuusuluxMZnSnqtp5s9elUekXrvr5z2MYYeIKTAR2N7OpEbGkoKrnNzK/oM7r24DbIhVPU3Tt2pWLL76Yiy66iKVLlzJ79mzeeeddqrZ/4wx402Uo1Tn5jd4lXZl/FJ4SJymUDwn9Dlsp3UPy1i9J2bUa9fsYMmQIP/7xlYwbN65N9vw5YcIEnnryCeasr65NCsVVwtub0znhhBPo1atXIyWYYFJS9jeuaIvfKxNcq+8QryVEhJEjRzJy5EiuvfZaXnvtNWa89BLbV74F6R0o7z6C6o79w1YxLaW7SNm4BO+e9SSnpDBh4kmcccYZ9OvXLyzlJyqv18tZZ5/Dfffdx/qiJPLbVfPBlhQqqpXzzjsv1uElrMAWgPHeg66JHksKIcrOzua8887j7LPP5t133+WJJ59k7ep30a3LKS/4Hv6szo0XUp+qclI2fEzyjpVkZGZwzuTJnHnmmdZMMMD48eP554MPsmBLCvntyvhgaxqDBg6gf//+sQ6tVWhNDRRMy1hSaKKkpCSOO+44xo0bx1tvvcUDDz7I7q9mU9l9JFU9RjX5rMGzbwsZa95BfOWcfe45XHTRRdYSJIjs7GzGHD6GT7/4iPG9y1m3z8NVPzkh1mG1GoGXkkzb1vprKiPE4/Hwox/9iGefeYbxJ55IyqbPSFnzXpPukk7as570Fa/TvVMuDz/0EFdffbUlhAaMHXsE20rhvc2p7uuw3PTeptVcQvJ67fjQOOyb0EIZGRn87ne/o1u3bs5gPpkd8XUd1uj7pLyI9NXvMGDAAP72179aMghBzZjTb3yXSmZGOn369IlxRInvscceo7i4ONZhmDhiSSEMRISf/exnLPvyS5YsXUpx5yHQSHPR5C1f4PUIt916qyWEEPXp0wePx0OJD0YMHdAmmuRGWltvxGAOZr+qMBERJp58MlpVhpQXNrp8cvE2xowZ7Yz5YEKSkpJCt65OhX7v3vkxjsaY1smSQhglJzs9eor6G11W8FuLj2bI7dgJwJKpMRFiSSGMli9fDuLBn9Z4U9Kq1A58+eVy/P7GE4jZr6ZiNDc3N8aRGNM6WVIIk6qqKubNf5Pq9j0gqfExAHy5BezcuYMlS5ZEIbrWo6ZrBuvV05jIsKQQJm+++SZ7du+iqsuQkJavzi1AUjJ49tnpEY6sdZk8eTKTJk1ixIgRsQ7FmFbJWh+Fgd/v56mnn0YzO1LdvueB8+rrBM/jpaLLUBYv/oRvvvnGBocJ0eDBgxk8eHCswzCm1bIzhTD48MMP2bRxIxXdhh90R3Nl/lFU5h8V9H1VnQcj3hRefPHFaIRpjDGNsqQQBm+88QaSkkF1ThNvpvKmUNmxP++88y6lpaWRCc4YY5rAkkILqSqffLKYyvY9G71hLRhfTj5VVZUsW7YsAtEZY0zTWFJooX379lFSUow/vXlNJP0Zzvs2btwYzrCMMaZZLCm0kNZ0gNfsMRWc99n9CsaYeGBJoYWys7NJS0/HU1bYrPd7yvYA0K1btzBGZYwxzWNJoYU8Hg9jRo8mpXA9+Js+rLR391qSvF5rd2+MiQuWFMLgxz/+MVpZinfnyia9TypLSdm5kuOPO856SjXGxAVLCmFwxBFHMHTYMNI2fQpV5SG/L+W7j/DgZ/LkyZELzhhjmsCSQhiICDf86ldIdSWp6xaGNPpa0u71eHet5sILL6Rnz56NLm+MMdFgSSFM+vXrx5RLLsG7ew3enasaXFYqS0hf9z79+vfnwgsvjFKExhjTOEsKYXTBBRcwfPhw0r5biJTvC76QKqlr3iPZo9z8P/9TOwaDMcbEA0sKYZSUlMQf//hH0lJSSFvzLgQZbMe7bTlJezcx9Re/ID/fRg8zxsQXSwph1qVLF371y+vxFG3Du+2rA+ZJRRFpGz/liCOO5JRTTolRhMYYUz9LChHwox/9iDFjDidt02cHtEZK+e5jkr0ebrjhV7UjiBljTDyxpBABIsIvfnENVFeSvMXp6M5Tsgvv7rVccP75Nr6wMSZuWVKIkD59+nDMMceQuvMb8PvwbltOamoaZ599dqxDM8aYellSiKDTTjsNraogafdaUvas5fjj7c5lY0x8s+E4I2jkyJFkZrXD/90nqK+KcePGxTokY4xpkJ0pRFBSUhKHjRyBp6oUEWH48OGxDskYYxpkSSHCBg4cCEBeXicyMjJiHI0xxjTMkkKEde/eHYCUFLtz2RgT/ywpRFjNXcujRo2KcSTGGNM4q2iOsEGDBvHiiy/SsWPHWIdijDGNsqQQBXazmjEmUdjlI2OMMbUilhRE5DER2S4iXwZM+4uIfCMiX4jIyyLSIWDeTSKySkRWiMj4SMVljDGmfpE8U5gGTKgz7U1gmKoOB74FbgIQkSHAecBQ9z0PikhSBGMzxhgTRMSSgqq+B+yuM22+qvrclx8CNeNQngo8p6oVqroWWAWMjVRsxhhjgotlncIlwOvu8x7AhoB5G91pBxGRy0VksYgs3rFjR4RDNMaYtiUmSUFEfg/4gGdqJgVZTIO9V1UfUtUxqjqmU6dOkQrRGGPapKg3SRWRi4FJwPGqWrPj3wj0ClisJ7A52rEZY0xbJ/v3yxEoXKQAmKOqw9zXE4C/Aseq6o6A5YYCz+LUI3QH3gIGqGp1I+XvANZHJvqwygN2xjqIVsS2Z3jZ9gyfRNmW+aoa9FJLxM4URGQ6MA7IE5GNwP/gtDZKBd50h6P8UFWvVNXlIvIC8BXOZaWrG0sIAPX9U/FGRBar6phYx9Fa2PYML9ue4dMatmXEkoKqnh9k8qMNLH8bcFuk4jHGGNM4u6PZGGNMLUsK0fFQrANoZWx7hpdtz/BJ+G0Z0YpmY4wxicXOFIwxxtSypGCMMaaWJYUwE5GeIjJLRFaKyBoRuV9EUkWko4i8LSLFInJ/rONMBA1syx+JyKcissz9e1ysY00EDWzPsSLyuftYKiKnxzrWRFDf9gyY39v9vd8QyzibypJCGIlz88VM4BVVHQAMANKBu4By4I9AQn1BYqWRbbkTOEVVDwUuBp6KWaAJopHt+SUwRlVH4vRS/G8RsQG4GtDI9qzxN/b375YwLCmE13FAuao+DuDegHc9cBFOpf4HOMnBNK6hbblSVWu6QVkOpAUeoZmgGtqenoDei9Oop98xc4B6t6eIZInIacAanO9nQrGkEF5DgU8DJ6jqPmAd0D8WASWwULflmcBnqloRvdASUoPbU0SOEJHlwDLgyoAkYYJraHuOAH4L3BL9sFrOkkJ4CcGPsoL1Amsa1ui2dPvMuhO4IlpBJbAGt6eqfqSqQ4HDgZtEJC2awSWghrbnLcDfVLU4uiGFhyWF8FoOHNDviYhkA12AFTGJKHE1uC1FpCfwMnCRqq6OQXyJJqTvpqp+DZQAw6IaXeJpaHu2B+4SkXXAdcDvROSaaAfYXJYUwustIENELgJwhxS9B7hfVctiGlniqXdb4nSqOBe4SVUXxC7EhNLQ9uxaU7EsIvnAIJzLIKZ+Df3WD1fVAlUtAP4O3K6qCdPi0JJCGLnjQ5wOnCUiK4FdgN/t7A/3yOGvwGQR2eiOTW2CaGRbXoNTr/DHgKaUnWMYbtxrZHv+AFgqIp/jnH39XFUTofvnmGnst57IrJuLCBKR7wHTgTNU9dPGljf1s20ZXrY9w6s1bU9LCsYYY2rZ5SNjjDG1LCkYY4ypZUnBGGNMLUsKxhhjallSMBEhItUBvW4ucVtnNKecK2vagkeTiFwuIt+4j8UiMi6MZReIyAXhKq9O2X8WkROasHy9Pc6KyGh3+ioRudftBA4ROcb9TH0iclbA8j8MaCL8uYiUu30AmQRirY9MRIhIsapmuc/HA79T1WNjHFZIRGQSTlcF41V1p4iMAl4FjlDVTS0s24tzX8ANqjqpCe9LcjtdCysROQzYpqqbRWQYME9Ve7jzPgauBT4EXgPuVdXXRaQAyMbp8fdVVZ0RpNxcYBXQU1VLwx23iRw7UzDRkA3sARCRcSIyp2aG2wf9ZPf5HSLylYh8ISJ3u9NurumPXkTeEZE7ReRjEflWRI52pyeJyF9E5BP3vVe407uJyHvuUeuXInK0u+w09/UyEbk+SLy/BX5dcwOXqi4BHgeudstdJyJ57vMxIvKO+3ysiCwUkc/cv4Pc6ZNF5EURmQ3MB+4Ajnbjur6B+MeJMwbHs8AyEckUkbnu2deXInJu3cDd/+2sgDhvcY/ql4nIIXWXV9XPgvU4KyLdgGxVXeTeqPUkcJr7nnWq+gXgb+AzPwt43RJC4rE+002kpLt3yKYB3XC6Gq6Xe2R5OnCIqqqIdKhnUa+qjhWRk4H/AU4ApgB7VfVwcbrQXiAi84EzcI58bxOnG4IMYCTQQ1WHuesNtp6DesAEFgM/a/hf5hvgGFX1uZdwbsfpxRXgKGC4qu52L0XVnimIyOX1xA8wFhimqmtF5Exgs6pOdN/XvpF4AHaq6igR+TnOkf2lDSxb2+OsiPQANgbM2wj0CGF9Nc7DuXvfJBhLCiZSytxBWxCRo4An3csT9dmHM9bEIyIyF5hTz3Iz3b+fAgXu8xOB4QHXt9vjDHryCfCYiCTjDIbyuYisAfqKyH04/SfNJzSh9HTbHnhCRAbg9KCZHDDvTVXdXc/76ou/EvhYVde605cBd4vIncAcVX0/hJgCt9cZ9S0k+3ucPbFmUpDFQrrW7J5lHArMC2V5E1/s8pGJOFVdBOQBnQAfB37v0txlfDhHxS/hXKZ4o57iasZNqGb/QY0Av1DVke6jj6rOV9X3gGOATcBTInKRqu7B6e/+HZzLQY8EWcdXwOg600bhnC1Q538I7GL6f4G33bOQU+rMK6nn/6k3/rrvU9Vv3biWAf8nIn9qoMwawbbXgSsP3uPsRqBnwGI9gc1131uPc4CXVbUqxOVNHLGkYCLOvZadhNNp2HpgiHvduj1wvLtMFtBeVV/D6W54ZBNWMQ+4yj0jQEQGutff84Htqvow8Cgwyq0L8KjqSzjDo44KUt5dwJ0i0tEtbyTOpa1/u/PXsT9pnBnwvvY4CQhgcgPxFgHtGou/7ptEpDtQqqpPA3fXE3uTuJfPDupxVlW3AEUicqSICM4IbbNCLPZ8nH6ATAKyy0cmUmrqFMA5Er7YbT2zQUReAL4AVgKfucu0A2aJM7iL4AxtGKpHcC4lLXF3YDtwzjbGAb8WkSqgGGfH1gN4XERqDohuqluYqr7q7oAXiNNaqCswQlV3uIvcAjwqIr8DPgp46104l49+Cfy3gXi/AHwishSYBvyjnvjrOhT4i4j4gSrgqgbWEarAHmf/6E47UVW3u+VPwxl7+HX3gYgcjnNmkQOcIiK3uAP0IE7LpF7Au2GIzcSANUk1pgFuUngc56z6p2o/GNPKWVIwxhhTy+oUjDHG1LKkYIwxppYlBWOMMbUsKRhjjKllScEYY0wtSwrGGGNq/T9NrhmoNytiagAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.violinplot(data = netflix_stocks_quarterly , x = 'Quarter', y = 'Price')\n",
    "ax.set_title(\"Distribution of 2017 Netflix Stock Prices by Quarter\")\n",
    "ax.set_ylabel(\"Closing Stock Price\")\n",
    "ax.set_xlabel(\"Business Quarters in 2017\")\n",
    "plt.savefig('quarterlyDistribution2017.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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kvJdtGjRIs4//3xee+01Xn31VVatWsWoUaMYO3Yst956K5s3bwbgrbfeAmDw4MG8884727fff//9WbZsGVu3bqW+vn57eUtLCwcemHxf+s9//vNdbp+ZWVvyGfRTp8LcuXDQQSAlz3Pndmp+fsGCBZx77rk7lH3uc59j9erVVFVVUVNTw9FHH81dd90FwPTp0xk/fvz2i7GzZ89mwoQJnHbaaRxwwAHb93HVVVfx+c9/nk984hPtzuebme2KsvmGqWXLlvHxj3+8RC0qf37/zPLN3zBlZtaLOejNzHLOQW9mlnMOejOznHPQm5nlnIPezCznHPQd0LdvX8aMGbP9MXv27DbrLl68mOeee2778pVXXsl9993X6TasX7+eW265pdP7MbPeI58fgQA0NkJdXfLxNlVVMHky1NR0bp977rknTz/9dKa6ixcvZsKECYwePRqAH/zgB507eGpb0H/jG9/okv2ZWf7lckTf2Ahz5kBzM1RWJs9z5iTl3eGyyy5j9OjR1NTUMHPmTB555BGWLFnCJZdcwpgxY3jppZeYNm0aixYtAqC6uprLL7+ck046idraWp588knOPPNMDj74YG699VYg+UjkT3/604wdO5ajjjqKX/3qV9uP9dJLLzFmzBguueQSAK6//nqOO+44ampq+P73v989nTSzspXLEX1dHQwdmjzgg+e6us6N6t99913GjBmzfXnWrFmcccYZ1NfXs3z5ciSxfv16hgwZwsSJE5kwYQLnnXde0X2NHDmSP/3pT3znO99h2rRpPPzww2zatIkjjjiCGTNmMHDgQOrr69lnn3148803OfHEE5k4cSKzZ8/mmWee2f6bxb333suLL77I448/TkQwceJEHnroIT75yU/uekfNLFdyGfQrVyYj+UIVFZ3+lOKiUzebN29m4MCBXHjhhZx99tlMmDAh074mTpwIwFFHHcWGDRsYPHgwgwcPZuDAgaxfv5699tqLyy+/nIceeog+ffrw+uuvF/1SknvvvZd7772XY445Bkh+E3jxxRcd9Ga2XaaglzQO+BegL3BbRMxutf5w4N+BscAVETGnYN2rwDvAFmBzW5/F0JWqqpLpmm0jeYCWlk59SnGb+vXrx+OPP84f//hHFi5cyE033cT999/f7nZ77LEHAH369Nn+etvy5s2bmT9/PmvXrmXp0qX079+f6urqHT7e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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "plt.scatter(x_positions, earnings_actual, color = 'red')\n",
    "plt.scatter(x_positions, earnings_estimate, color = 'blue', alpha = .5)\n",
    "plt.legend([\"Actual\", \"Estimate\"])\n",
    "plt.title(\"Earnings Per Share in Cents\")\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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Gkn9ylSjmZmVoOgYuqT+wNaI2CCpF/B54Pt5bfYD3oqIkDSO5INiXYerm9Gnw4vYcXmNRZu0XD63xdSpU4teb6UUS5Ys4Y477mDWrFkdXpaZWWtKOctlAHC7pG4kQX1fRDwk6UKAiJgDfAmYLqkZeBeYGpU6wb2Dci+f217Nzc107976Jq2traW2ttVTR83MyqLokEtEPB8RoyLi8Ig4NCJuSKfPScOciLglIkZExMiIOCoinurswne3G264gbFjx3LooYcybdq07ddgGT9+PNdccw3HHnssP/7xjxk/fjxXXnkl48aN45BDDuHJJ58Edrw87owZMzj//PMZP348Bx100A699u985zt84hOfYMKECZxxxhnMnDkTgFmzZjF8+HAOP/xwpk6duptfvZl1BVX91f9KaLnaYourr76a008/nUsuuYRrr02+L3XWWWfx0EMPccoppwCwYcOGHS6h29zczLPPPsvChQu5/vrr+f3vf7/Tel5++WUef/xxNm3axLBhw5g+fTrLly/n/vvv57nnnqO5uZnRo0czZswYAG688UZee+01evTowYYNGzp3I5hZl+RAz1NoyOXxxx/npptuYvPmzaxfv54RI0ZsD/TTTz99h7Zf/OIXARgzZgyrV69udT0nn3wyPXr0oEePHnzkIx/hrbfeYvHixZx66qn06tULYPvyAQ4//HDOPPNMpkyZwpQpUzr+Qs0sc3y1xRJs2bKFiy66iPnz5/PCCy9wwQUXbL+8LcBee+21Q/uWy+N269aN5ubmVpeZewndlnZtHXZ4+OGHufjii6mrq2PMmDEFl2tmH1wO9BK0hHe/fv1oamra/rNx5XbMMcfw4IMPsmXLFpqamnj44eQCRu+//z5r1qzhuOOO46abbmLDhg00NTUVWZqZfdBU95BLCacZllv+GPrEiRO58cYbueCCCzjssMMYMmQIY8eO7ZR1jx07lsmTJzNy5EgGDx5MbW0tffr0Ydu2bXzlK1+hsbGRiOCKK66gb9++nVKDmXVdvnxulWlqaqJ3795s3ryZz372s8ydO5fRo0eX9FxvP+sqfPncXdfW5XOru4f+ATRt2jReeukltmzZwjnnnFNymNvu5UCyauRArzJ33313pUswsy6q6g6KdtEvmFact5uZVVWg9+zZk3Xr1jmc2ikiWLduHT179qx0KWZWQVU15DJw4EDq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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = .8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "plt.bar(bars1_x, revenue_by_quarter)\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = .8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "plt.bar(bars2_x, earnings_by_quarter)\n",
    "\n",
    "\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.legend(labels)\n",
    "plt.title(\"Netflix Revenue and Earnings in $ Billions\")\n",
    "plt.savefig('revenue&earning.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#revenue has an upward trend as well as earnings\n",
    "#10%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "\n",
    "ax1 = plt.subplot(1,2,1,)\n",
    "ax1.set_xlabel('Date')\n",
    "ax1.set_ylabel('Price')\n",
    "ax1.set_title(\"Netflix\")\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])\n",
    "plt.xticks(rotation='vertical')\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "\n",
    "ax2 = plt.subplot(1,2,2)\n",
    "ax2.set_xlabel('Date')\n",
    "ax2.set_ylabel('Stock Price')\n",
    "ax2.set_title('Dow Jones')\n",
    "plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'], color= 'Red')\n",
    "plt.subplots_adjust(wspace=.5)\n",
    "plt.xticks(rotation='vertical')\n",
    "plt.savefig(\"netflix_chart11.png\",dpi=100, bbox_inches='tight')\n",
    "plt.show()\n",
    "plt.savefig(\"test.png\", dpi=100, bbox_inches='tight')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.savefig(\"netflix10_chart.png\",dpi=300, bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
