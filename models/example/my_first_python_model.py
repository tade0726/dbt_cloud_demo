def model(dbt, session):

    df = dbt.ref("my_first_dbt_model")

    return df.where("id = 2")
