from docassemble.base.util import variables_snapshot_connection,get_config, user_info, json
import psycopg2
from num2words import num2words
from cryptography.fernet import Fernet
from docassemble.base.util import log
from docassemble.base.util import *

def branch_addres(branch_place):
  conn = variables_snapshot_connection()
  cur = conn.cursor()
  cur.execute("SELECT branch_address FROM branch_details where branch_place = '" + branch_place + "'")
  results = [record[0] for record in cur.fetchall()]
  conn.close()
  return results



def number_to_indian_words(number):
    return num2words(number, lang='en_IN')



