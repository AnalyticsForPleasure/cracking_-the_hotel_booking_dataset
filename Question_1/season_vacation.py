import pandas as pd
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
import seaborn as sns
# import matplotlib.lines as mlines
# #import seaborn as sys
# import seaborn as sns


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/cracking_the_hotel_booking_dataset/Data/hotel_booking_data.csv')
    df = df.replace(np.nan, '', regex=True)

    #Booking Hotel analysis:
    # 1) What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
    # 2) Which time periods see more families with children in the summer – weekdays or weekends?
    #    And during the winter, are families with children more prevalent than those without children?
    # 3) In which month can we see the highest waiting list?
    # 4) Is there any connection between the lead time and the cancel status?
    # 5) How do the dynamics of invitations differ between resort hotels and city hotels?

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)
    number_or_columns =df.shape[1]
    res=df['customer_type'].value_counts()
    res = df['arrival_date_month'].value_counts()
    print('*')

    # 1) What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
    summer_time = ['April','May','June','July','August','September']
    winter_time = ['October','November','December','January','February','March']

    filter_summer_vacation = df[df['arrival_date_month'].isin(summer_time)]
    filter_winter_vacation = df[df['arrival_date_month'].isin(winter_time)]
    #filter_season_vacation = filter_season_vacation.sort_values(by='arrival_date_month', inplace=True, ascending=False)
    print('*')

    avg_lead_time_in_the_summer = filter_summer_vacation.loc[:,'lead_time'].mean()
    avg_lead_time_in_the_winter = filter_winter_vacation.loc[:, 'lead_time'].mean()
    print('*')





