#Adding dimensions with textblob
tb_polarity = []
tb_subject = []


for tweet in df["Tweet_Content"]:
    tb_polarity.append(TextBlob(tweet).sentiment[0])
    tb_subject.append(TextBlob(tweet).sentiment[1])
    
    
df["Polarity"] = tb_polarity
df["Subjectivity"] = tb_subject