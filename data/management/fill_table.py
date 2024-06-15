import pandas as pd
from index import RetailPriceProcessed, RetailPrices, Session

# Populate retail_prices table
with Session.begin() as db:
    data = pd.read_csv("data/retail_price.csv")
    for index, row in data.iterrows():
        retail_prices = RetailPrices(
            product_id=row['product_id'],
            product_category_name=row['product_category_name'],
            month_year=row['month_year'],
            qty=row['qty'],
            total_price=row['total_price'],
            freight_price=row['freight_price'],
            unit_price=row['unit_price'],
            product_name_length=row['product_name_length'],
            product_description_length=row['product_description_length'],
            product_photos_qty=row['product_photos_qty'],
            product_weight_g=row['product_weight_g'],
            product_score=row['product_score'],
            customers=row['customers'],
            weekday=row['weekday'],
            weekend=row['weekend'],
            holiday=row['holiday'],
            month=row['month'],
            year=row['year'],
            s=row['s'],
            volume=row['volume'],
            comp_1=row['comp_1'],
            ps1=row['ps1'],
            fp1=row['fp1'],
            comp_2=row['comp_2'],
            ps2=row['ps2'],
            fp2=row['fp2'],
            comp_3=row['comp_3'],
            ps3=row['ps3'],
            fp3=row['fp3'],
            lag_price=row['lag_price'],
        )
        db.add(retail_prices)

# Populate retail_prices_processed table
with Session.begin() as db:
    data = pd.read_csv("data/df_with_significant_vars.csv")
    for index, row in data.iterrows():
        retail_prices_with_sig_vars = RetailPriceProcessed(
            total_price=row['total_price'],
            unit_price=row['unit_price'],
            customers=row['customers'],
            s=row['s'],
            comp_2=row['comp_2'],
            qty=row['qty'],
        )
        db.add(retail_prices_with_sig_vars)

