#!/usr/bin/python3
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
PATH = "/home/kodeine/Workspace/InstaSpam/chromedriver"

browser = webdriver.Chrome(PATH)

print("""
  __________                    .__  .__          __
 /  _____/  | ____  _  _______  |  | |  |   _____/  |_
/   __  \|  |/ /\ \/ \/ /\__  \ |  | |  | _/ __ \   __\\
\  |__\  \    <  \     /  / __ \|  |_|  |_\  ___/|  |
 \_____  /__|_ \  \/\_/  (____  /____/____/\___  >__|
       \/     \/              \/               \/
                                                              """)

data = csv.reader(open('users.csv'))
users_mails = []
users_usernames = []

for row in data:
  users_mails.append(row[0])
  users_usernames.append(row[1])


def main():
  n = input('Spam Instagram - insta\nSpam Mail - mail\n\n- Yo mon reuf c\'est pour quoi? ')
  print('-------------------------------------------------------------------------------')

  if n == "insta":
    instaspam('zmtpbnrlc3q@gmail.com', 'Wm10cGJuUmxjM1E')

  if n == "mail":
    mailspam()

  else :
    print("\n- dsl mon reuf jai pas capté, réessaie stp \n ")
    main()


def instaspam(username, password):

  try:
    browser.get('https://instagram.com')
    time.sleep(random.randrange(2,4))

    browser.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
    time.sleep(random.randrange(2,4))

    input_username = browser.find_element_by_name('username')
    input_password = browser.find_element_by_name('password')

    input_username.send_keys(username)
    time.sleep(random.randrange(1,2))
    input_password.send_keys(password)
    time.sleep(random.randrange(1,2))
    input_password.send_keys(Keys.ENTER)

  except Exception as err:
    print(err)
    browser.quit()

  message = input('Quel message tu veux envoyer ? => ')
  print("""/!\ Vérifie ton message => """ + message)
  n = input('Tu veux envoyer les messages? y/n ')

  if n == "y":
    send_insta_message(message)

  else:
    browser.quit()
    return

def send_insta_message(message):
    try:
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(random.randrange(3,5))
        browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
        time.sleep(random.randrange(1,2))
        for user in users_usernames:
          time.sleep(random.randrange(1,2))
          browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
          time.sleep(random.randrange(2,3))
          browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div').find_element_by_tag_name('button').click()
          time.sleep(random.randrange(3,4))
          browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
          time.sleep(random.randrange(3,4))
          text_area = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
          text_area.send_keys(message)
          time.sleep(random.randrange(2,4))
          text_area.send_keys(Keys.ENTER)
          print(f' c\'est bien envoyé a {user}')
          time.sleep(random.randrange(2,3))
          browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
          time.sleep(random.randrange(2,3))

    except Exception as err:
      print(err)
      browser.quit()

def mailspam():
  print('----------')
  print('MAILSPAM')
  print('----------')


if __name__ == "__main__":
  main()
