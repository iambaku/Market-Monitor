import asyncio
from config import SITES
from collector import capture
from notifier import send_report
async def run():
 files=[]
 for name,url in SITES.items():
  files.append(await capture(name,url))
 await send_report("Market snapshot generated",files)
if __name__=="__main__":
 asyncio.run(run())
