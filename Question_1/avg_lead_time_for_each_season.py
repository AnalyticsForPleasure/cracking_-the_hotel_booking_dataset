# Reference: https://www.kaggle.com/datasets/khairullahhamsafar/hotels-booking-data-cleaned-version

# Feature	Description
# hotel	Type of hotel - Resort Hotel or City Hotel.
# is_canceled	Binary indicator of reservation cancellation (1 for canceled, 0 otherwise).
# lead_time	Number of days between booking date and arrival date.
# arrival_date_year	Year of arrival date.
# arrival_date_month	Month of arrival date.
# arrival_date_week_number	Week number of arrival date.
# arrival_date_day_of_month	Day of the month of arrival date.
# stays_in_weekend_nights	Number of weekend nights (Saturday or Sunday) the guest stays.
# stays_in_week_nights	Number of week nights (Monday to Friday) the guest stays.
# adults	Number of adults in the reservation.
# children	Number of children in the reservation.
# babies	Number of babies in the reservation.
# meal	Type of meal booked - e.g., Bed & Breakfast (BB).
#### "BB" bed and breakfast
#### "FB" FB means full board, in which breakfast, lunch and dinner are included
#### "HB" HB means half board, in which breakfast and dinner are included
#### "SC" means self-catering (no meals are included)
# country	Country of origin of the guest.
# market_segment	Market segment designation (e.g., Direct, Corporate).
# distribution_channel	Booking distribution channel (e.g., Direct, Corporate).
# is_repeated_guest	Binary indicator if the guest is a repeated guest (1 for repeated, 0 otherwise).
# previous_cancellations	Number of previous reservation cancellations by the guest.
# previous_bookings_not_canceled	Number of previous bookings not canceled by the guest.
# reserved_room_type	Type of room reserved by the guest.
# assigned_room_type	Type of room assigned to the guest.
# booking_changes	Number of changes made to the reservation.
# deposit_type	Type of deposit made by the guest (e.g., No Deposit).
# agent	ID of the travel agency making the booking.
# company	ID of the company/entity making the booking.
# days_in_waiting_list	Number of days the booking was on the waiting list.
# customer_type	Type of booking, e.g., Transient, Contract.
# adr	Average Daily Rate, i.e., the average rental income per paid occupied room.
# required_car_parking_spaces	Number of parking spaces required by the guest.
# total_of_special_requests	Number of special requests made by the guest.
# reservation_status	Current reservation status (e.g., Check-Out).
# reservation_status_date	Date of the last status update.

import pandas as pd
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
import seaborn as sns



# import matplotlib.lines as mlines
# #import seaborn as sys
# import seaborn as sns

# **************************************************************************************************************
# Question : What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
# Function  name:  avg_lead_time_for_each_season
# input:
# return value:
# ***************************************************************************************************************
def avg_lead_time_for_each_season(df):
    # 1) What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
    summer_time = ['April', 'May', 'June', 'July', 'August', 'September']
    winter_time = ['October', 'November', 'December', 'January', 'February', 'March']
    filter_summer_vacation = df[df['arrival_date_month'].isin(summer_time)]
    filter_winter_vacation = df[df['arrival_date_month'].isin(winter_time)]
    print('*')
    avg_lead_time_in_the_summer = filter_summer_vacation.loc[:, 'lead_time'].mean() # Avg lead time at the summer -> 115.96 ( resort )
    avg_lead_time_in_the_winter = filter_winter_vacation.loc[:, 'lead_time'].mean() # Avg lead time at the winter -> 61.946 ( resort )
    lead_time_list = [avg_lead_time_in_the_summer, avg_lead_time_in_the_winter]
    print('*')
    return lead_time_list

# **************************************************************************************************************
# Question :
# Function  name:  avg_lead_time_for_each_season
# input:
# return value:
# ***************************************************************************************************************

def adding_a_bar_chart(avg_time_seasons):
    fig, ax = plt.subplots(figsize=(21, 7))

    bar_titles = ['Avg lead time in the summer', 'Avg lead time in the winter']  # Categorical data
    avg_time_seasons_values = avg_time_seasons  # Integer value avg_time_seasons_values

    plt.bar(bar_titles, avg_time_seasons_values)
    #ax = sns.barplot(x=bar_titles, y=avg_time_seasons_values, orient='h', joinstyle='bevel')

    #
    # ax = sns.barplot(x=df.Completion, y=avg_time_seasons_values, orient='h', joinstyle='bevel')
    #
    # new_patches = []
    # for patch in reversed(ax.patches):
    #     bb = patch.get_bbox()
    #     color = patch.get_facecolor()
    #     p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),
    #                             abs(bb.width), abs(bb.height),
    #                             boxstyle="round,pad=-0.0040,rounding_size=0.015",
    #                             ec="none", fc=color,
    #                             mutation_aspect=4
    #                             )
    #     patch.remove()
    #     new_patches.append(p_bbox)
    # for patch in new_patches:
    #     ax.add_patch(patch)
    #
    sns.despine(left=True)
    ax.yaxis.set_ticks([])

    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/hotel_booking_data.csv')
    #/ home / shay_diy / PycharmProjects / cracking_the_hotel_booking_dataset / Data / hotel_booking_data.csv
    df = df.replace(np.nan, '', regex=True)

    # Booking Hotel analysis:
    # 1) What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
    # 2) Which time periods see more families with children in the summer – weekdays or weekends?
    #    And during the winter, are families with children more prevalent than those without children?
    # 3) In which month can we see the highest waiting list?
    # 4) Is there any connection between the lead time and the cancel status?
    # 5) How do the dynamics of invitations differ between resort hotels and city hotels?

    # print(sorted(df.columns))
    # for col in ["meal"]:  # df.columns:
    #     print(f'col: {col} :')
    #     print(df[col].unique())
    #     print('#' * 50)
    #
    # print('*')

    hotels = ['Resort Hotel','City Hotel']

    for specific_hotel in hotels:
        df_final = df.loc[df['hotel'] == specific_hotel, :]
        lead_time_list = avg_lead_time_for_each_season(df_final)
        adding_a_bar_chart(lead_time_list )
        print('*')


