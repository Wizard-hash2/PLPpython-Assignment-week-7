import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['Aron', 'Ngenoh', 'Musa', 'Unnonw'], 'Age': [20,21,22,21], 'Place': ['Naks', 'Kericho', ' Kiambu', 'Thika']}

df = pd.DataFrame(data)

#print(df[df['Age'] > 20])

df['Paid'] = ['Yes','Noo','yeah', 'yes']
#print(df)

#df.drop('Paid', axis=1, inplace=True)

#print(df[(df['Age'] > 21 ) & (df['Paid'] == 'yeah')])

#print(df.sort_values(by='Age', ascending= False))

#grop = df.groupby('Place').agg({'Age': 'mean', 'Name': 'count'})
#print(grop)

print(f'The sum of the numbers is {df['Age'].sum()}')

#plt.plot(df['Name'], df ['Age'])
#plt.xlabel('Name')
#plt.ylabel('Age')
#plt.title('Name vs Age')
#plt.grid(True)
#plt.show()

# Bar Chat
 #df['Age'].plot(kind='hist', bins=10 )
#plt.xlabel('AGe')
#plt.title('Age DIstribution')
#plt.show()

#scattetr Plot

#df.plot(kind='scatter', x ='Age', y = 'Name')

#plt.show()

def PlottingData():
    try:
        data = pd.read_csv('Copy of dataset-uci.csv')
        hwData = pd.read_csv('hw_200.csv')
      
        clean_data = data.dropna(axis = 1)
        
     #   plt.plot(data['Age'], data['Height'])   == Line chat
       # data['Age'].plot(kind = 'hist', bins = 10, color = 'red') == Histogram
    #    plt.scatter(data['Age'], data['Height'] )
        plt.bar(data['Age'], data['Height'])
        plt.xlabel('Age')
        plt.ylabel('Height')
        plt.show()

    except Exception as E:
        print(f'The data has error which is{E}')