print(df["Entity"].unique())
print(len(df["Entity"]).unique()))

onehot = pd.get_dummies(df["Entity"])

df = df.join(onehot)

df.head()