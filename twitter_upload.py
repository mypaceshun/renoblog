# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import csv

FILENAME = 'twitter_token.csv'
CK = 'XXXXX'  # Consumer Key
CS = 'XXXXX'  # Consumer Secret
AT = 'XXXXX'  # Access Token
AS = 'XXXXX'  # Access Token Secret

# tweetを投稿する
def tweet(tweet_text):
# ツイート投稿用のURL
  url = 'https://api.twitter.com/1.1/statuses/update.json'
# ツイート本文
  params = {'status': tweet_text}
# OAuth認証でPOST method で投稿
  twitter = OAuth1Session(CK, CS, AT, AS)
  req = twitter.post(url, params = params)
# レスポンスを確認
  if req.status_code == 200:
    print('OK')
  else:
    print('Error: %d' % req.status_code)

import sqlite3

SEARCHWORDS = ['中村麗乃','麗乃','れにょ','生田']
def get_new_entry(db_name):
  conn = sqlite3.connect(db_name)
  c = conn.cursor()

  result = c.execute('''SELECT * FROM entry
               WHERE title NOT IN (
                 SELECT title FROM entry_python)''')

# 最後insertする用命令文
  insert_str = ''

  for row in result:
    insert_str += 'insert into entry_python values('\
                + '"' +str(row[0]) + '",'\
                + '"' +str(row[1]) + '",'\
                + '"' +str(row[2]) + '",'\
                + '"' +str(row[3]) + '");\n'
                
# 単語検索しようか
    hit = False
    for search_word in SEARCHWORDS:
# auth
      if search_word in row[1]:
        hit = True
# title
      if search_word in row[2]:
        hit = True
# entry
      if search_word in row[4]:
        hit = True

      if hit:
# 投稿
        tweet_text = 'さぁ、どうだ！\n'\
                    + row[1] + ':' + row[2] + '\n'\
                    + row[3]
        print(tweet_text)
        tweet(tweet_text)
        break;
# 検索し終わったエントリーは探索済みデータベースに追加
  c.executescript(insert_str)
      
  conn.commit()
  conn.close()

if __name__ == '__main__':
  f = open(FILENAME, 'r')
  reader = csv.reader(f)
  CK = next(reader)[1]
  CS = next(reader)[1]
  AT = next(reader)[1]
  AS = next(reader)[1]

  get_new_entry('entry.db')
