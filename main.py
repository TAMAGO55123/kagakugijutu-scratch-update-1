# 拡張機能を読み込む
import json
import requests
import os

# データベースの取得URLを指定
webhook_url1 = 'https://script.google.com/macros/s/AKfycbzZ18jdzpAoMQw7q8Ie9z5ren9Y5QUdv9jAq27gvTTijmc8jLBfg0eomYZJF8JwEpof/exec?grade=1'
#webhook_url1=os.getenv('webhook1')
webhook_url2 = 'https://script.google.com/macros/s/AKfycbzZ18jdzpAoMQw7q8Ie9z5ren9Y5QUdv9jAq27gvTTijmc8jLBfg0eomYZJF8JwEpof/exec?grade=2'
#webhook_url2=os.getenv('webhook2')

# データベースからデータを取得
print('r1')
r1 = requests.get(url=webhook_url1)
print('r2')
r2 = requests.get(url=webhook_url2)

# データを変換する
print('1')
data1 = json.dumps(json.loads(r1.text), ensure_ascii=False, indent=4)
print(data1)

print('\n2')
data2 = json.dumps(json.loads(r2.text), ensure_ascii=False, indent=4)
print(data2)

data1s = data1.replace('\n', '')
data1s = data1s.replace(' ', '')
data2s = data2.replace('\n', '')
data2s = data2s.replace(' ', '')
datag = 'var gradedata=[' + data1s + ',' + data2s + '];'
print(datag)

# Webサーバーのデータの最新版をゲットする
print("git pull")
os.system("git pull")
# コマンドの設定
os.system("git config user.name TAMAGO55123")
os.system("git config user.email tamago.55123@gmail.com")

# 書き込み
print("write grade.js")
with open('docs/grade.js', mode='w') as f:
    f.write(datag)

# アップロード
#os.system("cd Kagakugijutu-Scratch")
print("git add .")
os.system("git add .")
print("git commit -m \"update grade files\"")
os.system("git commit -m \"update grade files\"")
print("git push")
os.system("git push")
