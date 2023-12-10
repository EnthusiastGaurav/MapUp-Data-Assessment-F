import pandas as pd


def generate_car_matrix(datasets):
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    df = pd.read_csv("datasets/dataset-1.csv")
    car_matrix = df.pivot(index='id_1',columns='id_2',values='car').fillna(0)

    for col in car_matrix.columns:
        car_matrix.loc[car_matrix.index == col,col] = 0

    result_matrix = generate_car_matrix(df)
    #return car_matrix
    print(result_matrix)


def get_type_count(datasets):
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df = pd.read_csv("datasets/dataset-1.csv")
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'),15,25,float('inf')],labels=['low','medium','heigh'],right=False)

    type_count = df['car_type'].value_counts().to_dict()
    type_count = dict(sorted(type_count.items()))

    return type_count
    result_count = get_type_count(df)
    print(result_count)

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    bus_mean = df['bus'].mean()

    bus_indexes = df[df['bus']>2 * bus_mean].index.tolist() #identify whaere values double thsn mean

    bus_indexes.sort()




    return bus_indexes
    result_indexes = get_bus_indexes(df)
    print(result_indexes)

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    route_avg_truck = df.groupby('route')['truck'].mean()

    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    selected_routes.sort()

    return selected_routes
    result_routes = filter_routes(df)
    print(result_routes)


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modified_matrix = matrix.copy()

    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    modified_matrix = modified_matrix.round(1)

    return modified_matrix
    result_matrix = generate_car_matrix(df)
    modified_result = multiply_matrix(result_matrix)
    print(modified_result)


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df1 = pd.read_csv("datasets/dataset-2.csv")
    df1['start_timestamp'] = pd.to_datetime(df1['startDay'] + '' + df1['startTime'])

    df1['end_timestamp'] = pd.to_datetime(df1['endDay'] + ' ' + df1['endTime'])

    multi_index_df = df1.set_index(['id','id_2'])

    completeness_check = (
        (multi_index_df['start_timestamp'].dt.time != pd.Timestamp('00:00:00').time()) |
        (multi_index_df['end_timestamp'].dt.time != pd.Timestamp('23:59:59').time()) |
        (multi_index_df['start_timestamp'].dt.dayofweek > 0) |
        (multi_index_df['end_timestamp'].dt.dayofweek < 6)
    )

    return completeness_check

    result_completness = verify_timestamps_completness(df2)
    print(result_completness)
