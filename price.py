def price(name):
  import duckdb
  import pandas as pd

  #Connects to database
  conn = duckdb.connect("SampleDB", read_only=False)

  #Table created only if it doesnt exist, data copied from CSV to DB
  conn.execute(
    "CREATE TABLE IF NOT EXISTS price_data AS SELECT * FROM 'Xgrocery_price.csv'"
  )

  conn.execute("""
                CREATE OR REPLACE VIEW latest_records AS
                SELECT price_data.* FROM price_data,
                (SELECT MAX(date) AS date, store_product
                 FROM price_data
                 GROUP BY store_product) max_data
                WHERE price_data.date=max_data.date
                AND price_data.store_product=max_data.store_product
                ORDER BY max_data.date DESC
                """)
  
  #If input(product name) is not NoneType, 1st SQL case insensitive query statement is executed otherwise a simpler SQL statement is executed
  if not name is None:
    name = '%' + name + '%' #adding wildcard char before and after the input
    
    #View records in form of a dataframe
    result = conn.execute("""
                        SELECT 
                        date,
                        ARRAY_EXTRACT(STR_SPLIT(store_product,'_'),1) AS store, 
                        ARRAY_EXTRACT(STR_SPLIT(store_product,'_'),2) AS product,
                        availability,
                        price
                        FROM latest_records
                        WHERE lower(product) LIKE ?
                        """,(name.lower(),)).fetchdf()
    
   
    result['date'] = result['date'].dt.date  #fix for timestamp error
    print(result.dtypes)
    print()
  
  else:
    #View all records in form of a dataframe
    result = conn.execute("""
                        SELECT 
                        date,
                        ARRAY_EXTRACT(STR_SPLIT(store_product,'_'),1) AS store, 
                        ARRAY_EXTRACT(STR_SPLIT(store_product,'_'),2) AS product,
                        availability,
                        price
                        FROM latest_records
                        """).fetchdf()
    result['date'] = result['date'].dt.date  #fix for timestamp error

  return result

