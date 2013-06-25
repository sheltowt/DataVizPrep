#url, username, socialnetwork
import pandas as pd
import json

filtered_photos = pd.read_csv("updated_big_data.csv")

columns = ['url', 'username', 'socialnetwork']
index = range(0, 150)


can_df = pd.DataFrame(index=index, columns=columns)
logo_df = pd.DataFrame(index=index, columns=columns)
new_df = pd.DataFrame(index=index, columns=columns)

filtered_photo_count = -1
can_df_count = 0
logo_df_count = 0
new_df_count = 0
for row in enumerate(filtered_photos.values):
  print row
  filtered_photo_count +=1
  if filtered_photos["can"][filtered_photo_count] == 1:
    can_df['url'][can_df_count] = filtered_photos["photo_url"][filtered_photo_count]
    can_df['username'][can_df_count] = filtered_photos["photo_submitter"][filtered_photo_count]
    can_df['socialnetwork'][can_df_count] = filtered_photos["photo_source"][filtered_photo_count]
    can_df_count +=1
  if filtered_photos["logo"][filtered_photo_count] == 1:
    logo_df['url'][logo_df_count] = filtered_photos["photo_url"][filtered_photo_count]
    logo_df['username'][logo_df_count] = filtered_photos["photo_submitter"][filtered_photo_count]
    logo_df['socialnetwork'][logo_df_count] = filtered_photos["photo_source"][filtered_photo_count]
    logo_df_count +=1
  if new_df_count < 150:
    new_df['url'][new_df_count] = filtered_photos["photo_url"][filtered_photo_count]
    new_df['username'][new_df_count] = filtered_photos["photo_submitter"][filtered_photo_count]
    new_df['socialnetwork'][new_df_count] = filtered_photos["photo_source"][filtered_photo_count]
    new_df_count +=1

can_df.to_csv("can_photos1.csv")  
logo_df.to_csv("logo_photos1.csv")


f_can = open('can.json', 'w')
f_logo = open('logo.json', 'w')
f_new = open('new.json', 'w')

d = [ 
    dict([
        (colname, row[i]) 
        for i,colname in enumerate(can_df.columns)
    ])
    for row in can_df.values
]

new_can = json.dumps(d)

f_can.write(new_can+'\n')

f = [ 
    dict([
        (colname, row[i]) 
        for i,colname in enumerate(logo_df.columns)
    ])
    for row in logo_df.values
]
new_logo = json.dumps(f)


f_logo.write(new_logo+'\n')

t = [ 
    dict([
        (colname, row[i]) 
        for i,colname in enumerate(new_df.columns)
    ])
    for row in new_df.values
]
new_new = json.dumps(t)


f_new.write(new_new+'\n')
  