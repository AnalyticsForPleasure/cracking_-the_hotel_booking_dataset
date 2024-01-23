import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.lines as mlines
# #import seaborn as sys
# import seaborn as sns





if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/data/hotel_booking_data.csv')
    df = df.replace(np.nan, '', regex=True)

    #Booking Hotel analysis:
    #1) What is the avg lead time for the winter season? And what is the avg lead time for the summer time?
    # 2) Who states and weekend nights more families with children during the summer? Families without children during the summer? Families with children over the winter?
    # 3) In which month can we see the highest waiting list?
    # 4) Is there any connection between the lead time and the cancel status?
    # 5) How do the dynamics of invitations differ between resort hotels and city hotels?

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)
    number_or_columns =df.shape[1]
    res=df['customer_type'].value_counts()
    print('*')
