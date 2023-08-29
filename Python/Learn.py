import pandas as pd

#Dataframes (basically a table)



#so the structure of creating a frame goes column name then corresponding row values

new_frame = pd.DataFrame({'Historical Fiction': ['The Book Theif',"All the Light We Cannot See",'The Nightingale'],
                           'Science Fiction & Fantasy': ['Dune', 'Neuromancer','The Name of the Wind'], 
                           'Self-help & Personal Development': ['The Power of Habit', 'Atomic Habits', 'The Subtle Art of Not Giving a F*ck']})

#print(new_frame)

#Series is a single column of a dataframe, Note that a series does not have a column name

new_Series = pd.Series(['RocketLeague', '2K', 'Cyberpunk'], 
                       index=['Most Hours Played', 'Love but hate', 'Great but needs QOL'])
#print(new_Series)

#the encoding helps to deal with errors
#if your data set has an index col like a db table the you can essentially omit it
youtube_Stats = pd.read_csv("Python/Global YouTube Statistics.csv", encoding='ISO-8859-1', index_col=0)
# pd.set_option('display.max_rows', 5)

#shape is to tell you how large the dataset is
#print(youtube_Stats.shape)

#head gives you the column names and the first 5 rows of each column shown
#print(youtube_Stats.head())

#here we can access any column of data from the frame(essentially creating series from it)
#print(youtube_Stats['Youtuber']) 

#this basically gives you the entire row of data including column headers
#print(youtube_Stats.iloc[0])

#this basically gives you the first 3 rows of data from the set
#print(youtube_Stats.iloc[:3,0])

#rows of your specified columns
#print(youtube_Stats.loc[:, ['Youtuber', 'created_date', 'uploads', 'subscribers']])

#iloc includes the first element in range and excludes the last one
#loc includes everything

#use set index if you can find a better column to use for indexing
#youtube_Stats.set_index("Youtuber")

#show if the the v alues inx column meet some condition
#print(youtube_Stats.subscribers > 100000000)

#show if the rows that satisfy your conditions
#print(youtube_Stats.loc[(youtube_Stats.subscribers >= 30000000) & (youtube_Stats.Country == 'United States')])

#print(youtube_Stats.loc[youtube_Stats.Youtuber == 'KSI'])


type_channel = youtube_Stats.channel_type #this is classed as a series

#f_row = youtube_Stats.iloc[1]

#create a series from the specified rows
sample_types = type_channel.loc[[1,2,3,5,8]]


#print(type_channel.loc[:10])
#print(f_row)

#select specific rows and columns to display
df = youtube_Stats.loc[[1, 10, 100, 120], ['Country', 'Latitude', 'Longitude']]

print(df)


