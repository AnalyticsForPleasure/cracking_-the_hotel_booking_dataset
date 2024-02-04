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
# Function  name: creating_the_data
# input:
# return value:
# ***************************************************************************************************************
def  creating_the_data(df_final):
    result = df_final['country'].value_counts()
    result.reset_index()
    print('*')


    return 2



if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/hotel_booking_data.csv')
    #/ home / shay_diy / PycharmProjects / cracking_the_hotel_booking_dataset / Data / hotel_booking_data.csv
    df = df.replace(np.nan, '', regex=True)
    print('*')

    # Filter number 1: Filtering the data by column 'is_canceled'
    df_not_canceled = df.loc[df['is_canceled'] == 0, :]

    # Create a mapping dictionary from country code to full name
    country_mapping = {
        'PRT': 'Portugal',
        'GBR': 'United Kingdom',
        'ESP': 'Spain',
        'IRL': 'Ireland',
        'FRA': 'France',
        'ROU': 'Romania',
        'NOR': 'Norway',
        'DEU': 'Germany',
        'BEL': 'Belgium',
        'CHE': 'Switzerland',
        'GRC': 'Greece',
        'ITA': 'Italy',
        'NLD': 'Netherlands',
        'DNK': 'Denmark',
        'RUS': 'Russia',
        'SWE': 'Sweden',
        'EST': 'Estonia',
        'CZE': 'Czech Republic',
        'LUX': 'Luxembourg',
        'SVN': 'Slovenia',
        'ALB': 'Albania',
        'SMR': 'San Marino',
        'LVA': 'Latvia',
        'SRB': 'Serbia',
        'AUT': 'Austria',
        'BLR': 'Belarus',
        'LTU': 'Lithuania',
        'HUN': 'Hungary',
        'HRV': 'Croatia',
        'BGR': 'Bulgaria'
    }
   # Filter number 3: Filtering by European countries list
    european_countries_list = list(country_mapping.values())
    filtered_df = df_not_canceled[df_not_canceled['country'].isin(european_countries_list)]

    # Filter number 3: Filtering by kind of hotel
    hotels = ['Resort Hotel','City Hotel']
    for specific_hotel in hotels:
        df_final = filtered_df.loc[df_not_canceled['hotel'] == specific_hotel, :]
        creating_the_data(df_final)
        print('*')


