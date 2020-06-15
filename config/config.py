 #!/usr/bin/env python
import os
import sys 

AIR_BNB_DATA_FILE_PATH = "../data/AB_NYC_2019.csv"

CATEGORICAL_FEATURES = ['neighbourhood_group', 
                        'neighbourhood',
                        'room_type']

NUMERIC_FEATURES = ['minimum_nights',
                    'number_of_reviews', 
                    'reviews_per_month',
                    'calculated_host_listings_count',
                    'availability_365']

GEO_FEATURES = ['latitude',
                'longitude']


TEXT_FEATURES = ['name',
                 'host_name']

LABEL = ['price']

FEATURES = CATEGORICAL_FEATURES + \
           NUMERIC_FEATURES + \
           GEO_FEATURES + \
           TEXT_FEATURES