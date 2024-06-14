import pandas as pd

pt_df = pd.read_csv('data/POC_PT.csv')
# es_df = pd.read_csv('data/POC_ES.csv')

pt_users = [
    "8424040900596005", "8424071001682725",
    "8424061001153447",
    "8424040900895795",
    "8424040903687413",
    "8424010900737420",
    "8424040900798288",
    "8424050900004777"
]
# es_users = [
#     "5267520911676740",
# "4255490496518000",
# "4255492335977000",
# "4940281740138000",
# "4940280499010000"
# ]


df_fitre_by_user = pd.DataFrame()
for user in pt_users:
    df_fitre_by_user = pd.concat(
        [df_fitre_by_user, pt_df.query("id == {}".format(user))])
    print(f"{user}: {df_fitre_by_user.size}")

df_fitre_by_user.to_csv("data/POC_PT_filterByUser.csv")
