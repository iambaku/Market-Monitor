from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
scheduler=BlockingScheduler(timezone="US/Pacific")
@scheduler.scheduled_job("cron",hour=6,minute=0)
def job():
 subprocess.run(["python","app.py"])
scheduler.start()
