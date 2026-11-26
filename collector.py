from playwright.async_api import async_playwright
from pathlib import Path
import datetime
OUTPUT_DIR=Path("screenshots")
OUTPUT_DIR.mkdir(exist_ok=True)
async def capture(name,url):
 filename=OUTPUT_DIR/f"{datetime.date.today()}_{name}.png"
 async with async_playwright() as p:
  browser=await p.chromium.launch()
  page=await browser.new_page(viewport={"width":1600,"height":1200})
  await page.goto(url,wait_until="networkidle",timeout=120000)
  await page.screenshot(path=str(filename),full_page=True)
  await browser.close()
 return str(filename)
