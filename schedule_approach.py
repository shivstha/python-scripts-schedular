import schedule
import time

def job():
    print("I'm working...")

def job_in_second():
    print("I'm now working!!!!")

schedule.every(1).minutes.do(job)
schedule.every(10).seconds.do(job_in_second)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)