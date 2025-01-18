# plotly gives the best visualization it gives web ui
# before running these function install dependecies 
# pipenv install matplotlib seaborn plotly pandas

####### using matplotlib #######

def use_matplot_lib():
    import matplotlib
    matplotlib.use('Agg')  # Set the backend to Agg for non-interactive plotting
    import matplotlib.pyplot as plt

    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    sales = [300, 700, 2000, 3000, 5000, 8000, 12000]
    countries = ['USA', 'UK', 'France', 'Germany', 'China', 'Brazil', 'India']
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown']

    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.plot(years, sales, marker='o', linestyle='solid', linewidth=2)

    #storing in current folder
    plt.savefig('./data-handling/data-visualization/sales_by_year.jpg')  # Saves the plot as a PNG file


    #advacne graph

    '''
    plt.plot(years, sales, marker='o', linestyle='solid', linewidth=2)
    supported linestyle values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
    '''
    # or 

    # plt.scatter(years, sales, marker='o', color=colors)
    # for i, country in enumerate(countries):
    #     plt.annotate(country, (years[i], sales[i]), textcoords="offset points", xytext=(0,10), ha='center')

    # plt.savefig('./data-handling/sales_by_year.jpg')  # Saves the plot as a PNG file
    # plt.show() # Displays the plot
    
# use_matplot_lib()

#! ------------------------- using seaborn -------------------------

def use_seaborn():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    

    data = { "age": [25, 30, 35, 40, 45, 50, 55, 60], "salary": [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928] }
    df = pd.DataFrame(data)

    # Create a bar plot using Seaborn
    sns.barplot(x='age', y='salary', data=df)
    
    # plt.title('Salary by Age')
    # plt.xlabel('Age')
    # plt.ylabel('Salary')
    # plt.grid(True)

    # plt.show()  # Display the plot #not wokring in terminal use save
    # plt.savefig('./data-handling/data-visualization/person-salary-age.jpg')  # Saves the plot as a PNG file
    
#for sns u need to insta ==> dependecies +> sudo apt-get install libxcb-cursor0
# use_seaborn()


def using_plotly():
    import plotly.express as px
    import pandas as pd

    data = { "age": [25, 30, 35, 40, 45, 50, 55, 60], "salary": [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928] }
    df = pd.DataFrame(data)

    fig = px.bar(df, x='age', y='salary', title='Salary by Age')
    fig.show()
    
    
    # import plotly.express as px
    # import pandas as pd

    # data = { "age": [25, 30, 35, 40, 45, 50, 55, 60], "salary": [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928] }
    # df = pd.DataFrame(data)

    # fig = px.bar(df, x='age', y='salary', title='Salary by Age')
    # fig.show()
    
# using_plotly()