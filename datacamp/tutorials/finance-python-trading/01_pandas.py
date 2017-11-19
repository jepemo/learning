import quandl 
aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

# Return first rows of `aapl`
aapl.head()

# Return last rows of `aapl`
aapl.tail()

# Describe `aapl`
aapl.describe()

# Inspect the index 
aapl.index

# Inspect the columns
aapl.columns

# Select only the last 10 observations of `Close`
ts = aapl['Close'][-10:]

# Check the type of `ts` 
type(ts)
