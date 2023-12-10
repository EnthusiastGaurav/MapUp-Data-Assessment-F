import pandas as pd
import numpy as np


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    df = pd.read_csv('datasets/dataset-3.csv')
    multi_index_df = df.set_index(['id','id_2'])

    distance_matrix = multi_index_df.pivot_table(values='distance',index='id',columns='id_2',aggfunc=np.sum,fill_value=0)

    distance_matrix = distance_matrix.add(distance_matrix.T, fill_values=0)
    np.fill_diagonal(distance_matrix.values,0)

    return distance_matrix
    result_distance_matrix = calculate_distance_matrix(df)
    print(result_distance_matrix)


def unroll_distance_matrix(df, distance_matrix=int)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    df = pd.read_csv('datasets/dataset-3.csv')
    distance_matrix_reset = distance_matrix.reset_index()
    melted_distance = pd.melt(distance_matrix_reset, id_vars='id',var_name='id_end',value_name='distance')

    melted_distance = melted_distance.rename(columns={'id': 'id_start'})

    unrolled_distance = melted_distance[melted_distance['id_start'] != melted_distance['id_end']]

    unrolled_distance = unrolled_distance.sort_values(by=['id_start','id_end']).reset_index(drop=True)


    return unrolled_distance
    result_unrolled_distance = unroll_distance_matrix(result_distance_matrix)
    print(result_unrolled_distance)


def find_ids_within_ten_percentage_threshold(df, reference_id, distance_df=None, reference_value=input(int))->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    reference_rows = distance_df[distance_df['id_start'] == reference_value]
    reference_average_distance = reference_rows['distance'].mean()

    lower_threshold = reference_average_distance - (0.1 * reference_average_distance)
    upper_threshold = reference_average_distance + (0.1 * reference_average_distance)

    within_threshold_rows = distance_df[(distance_df['distance'] >= lower_threshold) & (distance_df['distance']<= upper_threshold)]

    within_threshold_ids = within_threshold_rows['id_start'].unique()
    within_threshold_ids.sort()

    return within_threshold_ids
    reference_value = input(int)
    result_within_threshold = find_ids_within_ten_percentage_threshold(result_unrolled_distance, reference_value)
    print(result_within_threshold)


def calculate_toll_rate(distance_df, toll_rate_df=int)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    toll_rate_df = distance_df.copy()
    toll_rate_df['moto'] = distance_df['distance'] * 0.8
    toll_rate_df['car'] = distance_df['distance'] * 1.2
    toll_rate_df['rv'] = distance_df['distance'] * 1.5
    toll_rate_df['bus'] = distance_df['distance'] * 2.2
    toll_rate_df['truck'] = distance_df['distance'] * 3.6

    return toll_rate_df
    result_with_toll_rates = calculate_toll_rate(result_unrolled_distance)
    print(result_with_toll_rates)




def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
