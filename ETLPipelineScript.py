from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("demo").getOrCreate()

df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/learningfiles/veh_data/car_prices.csv')

df1 = df.filter((df.year == 2015) & (df.transmission == 'manual')).orderBy(desc(df.sellingprice))

df2 = df1.withColumn('rank',row_number().over(Window.partitionBy(df.make,df.model).orderBy(desc(df.sellingprice))))

df3 = df2.filter(df2.rank == 1).select('year','make','model','transmission','odometer','sellingprice','seller').orderBy(desc(df2.odometer)).toPandas()

df4 = spark.createDataFrame(df3.dropna())

df4.write.parquet('/Volumes/workspace/learningfiles/veh_data/CarData2015')