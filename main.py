# Word Of The Day SMS Bot
# By A.R.T. Corp
# Made for my mom! 

from random_word import RandomWords
from twilio.rest import Client
from datetime import datetime
from colorama import Fore
from time import sleep
import random
import subprocess
import time
import json
import sys

def clearpage(): # Clear page function
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')

def clearall(): # Clears 15 lines
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()


while True:
  random_month = "0" + str(random.randint(1, 9))   # TEST
  random_day = str(random.randint(10, 27))         # TEST
  date = "2022-" + random_month + "-" + random_day # TEST
  # date = "2022-" + random_month + "-" + random_day
  
  # Date / datetime module 
  day = datetime.now()
  current_day = datetime.strftime(datetime.now(), '%b %d')

  # Twilio auth / acc tokens
  account_sid = "ACe524163d700bd0b4849b0c50569a093c" 
  auth_token  = "ed3a2c2beb63206282fb6c8c3612a167"
  client = Client(account_sid, auth_token)
  
  clear = "cls" if sys.platform == "win32" else "clear"

  # Generates word of the day
  r = RandomWords()
  wotd = r.word_of_the_day() 
  
  result = json.loads(wotd) # translates wotd into JSON dictionary
  
  all_pairs = list(result.items()) # Makes a list with each dictionary item
  
  first_pair = all_pairs[0] # Gets the first pair in the dictioary (word: ____)
  first_word_type_str = str(first_pair[1]) # Separates the word 
  
  second_pair = all_pairs[1] # Gets the type, definition, source, etc
  second_word_type_str = str(second_pair[1]) # Turns this into string
  
  # Formats string for UI readability
  format = second_word_type_str.replace("'", "").replace("[", "").replace("]", "").replace(",", "\n")
  
  formatted = format[1:]         # Removes starting bracket
  stopper = formatted.find("{")  # Finds start of second paragraph
  txt_remove = formatted.find("text") # Finds start of definition
  
  # Indents the text to fit with note and partOfSpeech
  formatted = formatted[0:txt_remove] + "" + formatted[txt_remove:] 
  
  # First paragraph 
  first_body = (formatted[txt_remove -1 :stopper])
  
  # Second paragraph 
  second_body = (formatted[stopper + 1:])
  
  # Removes ending bracket
  first_body_text = first_body.replace("}", "")
  second_body_text = second_body.replace("}", "")
  
  # Dictionary url for word
  dict_url = "https://www.merriam-webster.com/dictionary/" + first_word_type_str
  
  # Prints data in terminal 
  word_terminal = Fore.LIGHTYELLOW_EX +  "\n " + str(current_day) + Fore.WHITE + " | '" + Fore.LIGHTGREEN_EX + first_word_type_str + Fore.WHITE +  "' \n\n" + first_body_text + "\n " + Fore.LIGHTCYAN_EX + dict_url + Fore.WHITE + "\n\n Created by " + Fore.RED + "A.R.T." + Fore.WHITE + ""
  
  current_second = day.strftime("%S")
  current_minute = day.strftime("%M")
  current_hour = day.strftime("%H")
  
  print(word_terminal + "\n\n SMS count (H/M/S):") 
  print({current_hour}, {current_minute}, {current_second}, flush=True, end="")

  clearall()
  clearall()
  # subprocess.run(clear, shell=True)

  text = " " + str(current_day) + " | '" + first_word_type_str + "' \n\n" + first_body_text + "\n" + dict_url + "\n\nCreated by A.R.T."

  sorry = "Technical difficulties today. Expect a word momentarily."

  if str(current_hour) == "14":
    if str(current_minute) == "00":
      if str(current_second) == "00":

        numbers_to_message = ['+16692199886', '+15106725996', '+15107542586', '+15105137806', '+15103585844', '+15107387116', '+14087171705', '+15103422639', '+15108270299', '+15103648839', '+15106790082', '+15108611970']
        
        for number in numbers_to_message:
          client.messages.create(
          body = text,
          from_="+19853153395",
          to=number)

                
        # wotd_sms = client.messages.create( 
        # to = "+15106790082", # Dhruv's iPhone
        # from_ = "+19853153395",
        # body = text)

        