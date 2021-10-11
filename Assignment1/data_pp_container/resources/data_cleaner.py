from flask import jsonify


def clean(dataset):
    # only keep dataset priced between 200,000 and 1,000,000
    dataset = dataset[dataset["SoldPrice"] > 200000]
    dataset = dataset[dataset["SoldPrice"] < 1000000]

    # Limit to select columns
    dataset = dataset[
        ['Acres', 'Deck', 'GaragCap', 'Latitude', 'Longitude', 'LstPrice', 'Patio', 'PkgSpacs', 'PropType', 'SoldPrice',
         'Taxes', 'TotBed', 'TotBth', 'TotSqf', 'YearBlt']]

    # convert numbers back to strings

    dataset['TotSqf'] = dataset['TotSqf'].str.replace(',', '')
    dataset['TotSqf'] = dataset['TotSqf'].astype(int)

    dataset['Latitude'] = dataset['Latitude'].str.replace('.', '')
    dataset['Latitude'] = dataset['Latitude'].astype(int)

    dataset['Longitude'] = dataset['Longitude'].str.replace('.', '')
    dataset['Longitude'] = dataset['Longitude'].astype(int)
    dataset.dtypes

    # Add Prop_Type_num column, 0 if listing is condo or townhouse, 1 if single family house

    Prop_Type_num = []
    check = dataset['PropType'].str.contains('Single')
    for item in check:
        if item == True:
            Prop_Type_num.append(1)
        else:
            Prop_Type_num.append(0)

    dataset['Prop_Type_num'] = Prop_Type_num

    dataset = dataset[dataset.Taxes < 50000]
    dataset = dataset[dataset.Longitude != 0]
    dataset = dataset[dataset.Patio < 10]
    return dataset
