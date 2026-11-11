# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

   import pandas as pd

   data = {
       "order_id": [1, 2, 3],
       "region": ["South", "North", "West"],
       "amount": [250, 400, 150],
   }
   df = pd.DataFrame(data)
   print("Total sales:", df["amount"].sum())
   df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

    df["tax"] = df["amount"] * 0.18
    print("Total tax:", df["tax"].sum())
    df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
