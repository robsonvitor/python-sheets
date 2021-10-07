#!/usr/bin/env python3

import gspread 
import re
from subprocess import call
from oauth2client.service_account import ServiceAccountCredentials
import telegram_send


scope = ["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sh = client.open_by_url("URL DA PLANILHA")

ws = sh.get_worksheet(0)

criteria_re = re.compile(r'(STRING1|STRING2)', re.IGNORECASE)

rs = ws.findall(criteria_re)

if rs:
    telegram_send.send(messages=["Diploma pronto!!!!"])

