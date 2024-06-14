import pandas as pd

f = open("data/keywords.txt", "r", encoding="utf-8")
lines = f.readlines()
keywords = list(map(lambda x: x.lower(), lines))

pt_byUsers_df = pd.read_csv('data/POC_ES_filterByUser.csv')
result = pd.DataFrame(columns=["id", "title", "amount", "target", "suscipt"])

for index, row in pt_byUsers_df.iterrows():
    for key in keywords:
        if key.strip() in row['title'].lower():
            data = {
                "id": str(row["id"]),
                "title": row["title"],
                "amount": row["amount"],
                "target": row["target"],
                "suscipt": key.strip()
            }
            result.loc[len(result)] = data
            break

result.to_csv("data/POC_ES_suscrptByUser.csv")
