from seleniumbase import SB
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_real_name():
    first_names = ["James", "Robert", "John", "Michael", "David", "William"]
    last_names  = ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson"]
    return random.choice(first_names), random.choice(last_names)

def human_sleep(base):
    time.sleep(base + random.uniform(-0.3, 0.8))

def create(password, account):
    width = random.randint(1024, 1440)
    height = random.randint(768, 900)
    
    with SB(uc=True, test=True, headless=False, locale_code="zh-TW") as sb:

        sb.set_window_size(width, height)
        sb.open("https://google.com")

        human_sleep(1)
        sb.press_keys("#APjFqb", "who am i ")
        sb.submit("#APjFqb")
        human_sleep(1)

        human_sleep(4)
        sb.press_keys("#APjFqb", "youtube ")
        sb.submit("#APjFqb")
        human_sleep(2)
        sb.clear("#APjFqb")
        sb.open("https://www.youtube.com/")
        human_sleep(10)
        sb.open("https://accounts.google.com/signup")

        human_sleep(3)
        fname, lname = get_real_name()
        print(f"Name: {fname} {lname}")

        day  = random.randint(1, 28)
        year = random.randint(1980, 2000)
        sb.wait_for_element_visible("#firstName", timeout=15)
        sb.wait_for_element_visible("#lastName", timeout=15)

        sb.press_keys("body", "\t")
        human_sleep(1)
        sb.press_keys("#firstName", fname)
        human_sleep(0.8)
        sb.press_keys("#lastName", lname)
        human_sleep(1)

        sb.slow_click('button[jsname="LgbsSe"]')
        human_sleep(0.8)

        sb.press_keys('#day', str(day))
        human_sleep(0.8)

        sb.press_keys('#year', str(year))
        human_sleep(4)

        human_sleep(1)
        sb.uc_click("#gender")
        human_sleep(1.2)
        sb.scroll_to_bottom()
        human_sleep(1)
        sb.scroll_to_top()
        gender_value = random.choice([1, 2, 3])
        sb.execute_script(f"""
            const li = document.querySelector('#gender ul[role="listbox"] li[data-value="{gender_value}"]');
            if (li) {{
                ['mousedown','mouseup','click'].forEach(type => {{
                    li.dispatchEvent(new MouseEvent(type, {{bubbles:true, cancelable:true, view:window}}));
                }});
            }}
        """)
        sb.uc_click('#month')
        sb.scroll_to_bottom()
        human_sleep(1)
        sb.scroll_to_top()
        human_sleep(1)
        r = random.randrange(1, 12)
        print(r)
        sb.uc_click(f'li[data-value="{r}"]')

        human_sleep(1.3)
        sb.uc_click('button[jsname="LgbsSe"]')
        human_sleep(1.6)

        sb.wait_for_element_visible('[name="Username"]', timeout=10)
        sb.press_keys('[name="Username"]', account)
        sb.press_keys('[name="Username"]', "isalegne")
        human_sleep(1)
        sb.uc_click('button[jsname="LgbsSe"]')
        human_sleep(1.6)

        sb.wait_for_element_visible('[name="Passwd"]', timeout=10)
        sb.press_keys('[name="Passwd"]', password)
        sb.press_keys('[name="Passwd"]', "2234")
        human_sleep(2)
        sb.press_keys('[name="PasswdAgain"]', password)
        sb.press_keys('[name="PasswdAgain"]', "2234")
        human_sleep(4)
        sb.uc_click('button[jsname="LgbsSe"]')
        human_sleep(100)


ac   = "kenwwa"
pasw = "F1323"
create(pasw, ac)