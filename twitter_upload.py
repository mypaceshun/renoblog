# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import csv

FILENAME = 'twitter_token.csv'
CK = 'XXXXX'  # Consumer Key
CS = 'XXXXX'  # Consumer Secret
AT = 'XXXXX'  # Access Token
AS = 'XXXXX'  # Access Token Secret
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

if __name__ == '__main__':
  f = open(FILENAME, 'r')
  reader = csv.reader(f)
  CK = next(reader)[1]
  CS = next(reader)[1]
  AT = next(reader)[1]
  AS = next(reader)[1]

  tweet('どうだ！pic.twitter.com/0BYxcQk54h')

  print(CK,CS,AT,AS)
