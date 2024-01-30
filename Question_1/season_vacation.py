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
    avg_lead_time_in_the_summer = filter_summer_vacation.loc[:, 'lead_time'].mean()
    avg_lead_time_in_the_winter = filter_winter_vacation.loc[:, 'lead_time'].mean()

    return avg_lead_time_in_the_summer, avg_lead_time_in_the_winter


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/hotel_booking_data.csv')
    df = df.replace(np.nan, '', regex=True)

    # Booking Hotel analysis:
    # 1) What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
    # 2) Which time periods see more families with children in the summer – weekdays or weekends?
    #    And during the winter, are families with children more prevalent than those without children?
    # 3) In which month can we see the highest waiting list?
    # 4) Is there any connection between the lead time and the cancel status?
    # 5) How do the dynamics of invitations differ between resort hotels and city hotels?

    # print(sorted(df.columns))
    for col in ["meal"]:  # df.columns:
        print(f'col: {col} :')
        print(df[col].unique())
        print('#' * 50)

    # print(df.describe())
    # column_headers = list(df.columns.values)
    # print("The Column Header :", column_headers)
    # number_or_columns = df.shape[1]
    # res = df['customer_type'].value_counts()
    # res = df['arrival_date_month'].value_counts()
    # print('*')
    #
    # avg_lead_time_for_each_season(df)
    # print('*')

    # number_of_rows = df.shape[0]
    # res = df['country'].value_counts()
    res_2 = df['country'].value_counts()
    print('*')
