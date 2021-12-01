######################################################
# Project: <Project 3>
# UIN: <679663325>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-3-XiangchengLi#main.py>

# For this project, I received help from the following members of CS111.
# Enkh AmgalanAlt, netID 661490989: help with questions
# Student2name, netID 87654321: help with turtle heading and function parameters
 
######################################################
# imports
import requests
import csv
import json

# function definitions
def get_data_from_file(fn, format=""):
  # get format from fn if not supplied
  if fn[-4 :] == ".csv":
    format = 'csv'

  elif fn[-4 :] == "json":
    format = 'json'
  # if csv, handle csv file
  lst = []
  dic = []
  if format == "csv":

   with open(fn, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        lst.append(row)
   return lst

  # elif json, handle json file
  elif format == "json":
    f = open(fn)
    data = json.loads(f.read())
    for row in data:
      # f_answer.write(row)
      dic.append(row)
    return dic

def get_data_from_internet(url):
  lst_2 = []
  x = requests.get(url)
  data = x.json() 
  for record in data:
    lst_2.append(record)
  return lst_2

def get_index_for_column_label(header_row, column):
  row = 0
  for i in range (len(header_row)):
    if(header_row[i]) == column:
      row = i
  return row

def get_state_name(state_names, state_code):
  for i in state_names:
    if i['abbreviation'] == state_code:
      state_name = i['name']
  return state_name

def get_state_population(state_populations, state_name):
  name = '.' + state_name.upper()
  if type(state_populations) == list:
    for i in state_populations:
      for y in i.keys():
        x = y.upper()
        if x == name:
          population = i[y]
  elif type(state_populations) == dict:
    for i in state_populations.keys():
      if i == name:
        population = state_populations[i]
  return population
def answer_header(question_number, question_titles):
  header = "\n"*2
  header += "="*60 + "\n"
  header += "Question " + str(question_number) + "\n"
  header += question_titles[question_number] + "\n"
  header += "="*60 + "\n"
  return header
def state_answer_header(question_number, question_titles):
  header = "\n"*2
  header += "="*60 + "\n"
  header += question_titles[question_number] +"\n"
  header += "="*60 + "\n"
  return header


def main():
  question_states = [
    "State level information for "
  ]
  question_titles = [
   "",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average taxable income (per resident) per state",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average dependents per return for each agi group",
   "percentage of returns with no taxable income per agi group",
   "average taxable income per resident",
   "percentage of returns for each agi_group",
   "percentage of taxable income for each agi_group"
 ]

  f_answer = open("answersIL.txt", "w") 


  returns_data = get_data_from_file("tax_return_data_2018.csv")

  # f_answer.write (returns_data[1][1])
  # # AL
  
  header_row = returns_data[0]

  # f_answer.write (get_index_for_column_label(header_row, "N1")) 
  # # 4


  populations = get_data_from_internet("https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt")

  # f_answer.write (populations[1][".Alaska"])  
  # # 737438

  states = get_data_from_file("states_titlecase.json")
  

  indxN1 = get_index_for_column_label(header_row, "N1")
  indxA04800 = get_index_for_column_label(header_row, "A04800")
  indxAGI = get_index_for_column_label(header_row, 'agi_stub')
  indxN04800 = get_index_for_column_label(header_row, 'N04800')
  indxNumdep = get_index_for_column_label(header_row, 'NUMDEP')


  # f_answer.write (states[1]["name"])
  # # "Alaska"

  # get_state_name(state_names, "AL")
  #q1
  total1 = 0
  total2 = 0
  for i in returns_data:
    if i[1] != "STATE":
      total1 += int(i[indxN1])
      total2 += int(i[indxA04800])
  q1 = (total2/total1)*1000

  f_answer.write(answer_header(1, question_titles))
  f_answer.write('$ {:.0f}'.format(q1))

  #q2

  g1totalN1 = 0
  g1totalA04800 = 0

  g2totalN1 = 0
  g2totalA04800 = 0
  
  g3totalN1 = 0
  g3totalA04800 = 0
  
  g4totalN1 = 0
  g4totalA04800 = 0
  
  g5totalN1 = 0
  g5totalA04800 = 0
  
  g6totalN1 = 0
  g6totalA04800 = 0
  
  for i in returns_data:
    if i[1] != "STATE":
      if i[indxAGI] == "1":
        g1totalN1 += int(i[indxN1])
        g1totalA04800 += int(i[indxA04800])
        g1 = (g1totalA04800/g1totalN1)*1000
      if i[indxAGI] == "2":
        g2totalN1 += int(i[indxN1])
        g2totalA04800 += int(i[indxA04800])
        g2 = (g2totalA04800/g2totalN1)*1000 
      if i[indxAGI] == "3":
        g3totalN1 += int(i[indxN1])
        g3totalA04800 += int(i[indxA04800])
        g3 = (g3totalA04800/g3totalN1)*1000
      if i[indxAGI] == "4":
        g4totalN1 += int(i[indxN1])
        g4totalA04800 += int(i[indxA04800])
        g4 = (g4totalA04800/g4totalN1)*1000
      if i[indxAGI] == "5":
        g5totalN1 += int(i[indxN1])
        g5totalA04800 += int(i[indxA04800])
        g5 = (g5totalA04800/g5totalN1)*1000
      if i[indxAGI] == "6":
        g6totalN1 += int(i[indxN1])
        g6totalA04800 += int(i[indxA04800])
        g6 = (g6totalA04800/g6totalN1)*1000


  f_answer.write(answer_header(2, question_titles))
  f_answer.write('Group 1: $ {:.0f}\n'.format(g1))
  f_answer.write('Group 2: $ {:.0f}\n'.format(g2))
  f_answer.write('Group 3: $ {:.0f}\n'.format(g3)) 
  f_answer.write('Group 4: $ {:.0f}\n'.format(g4)) 
  f_answer.write('Group 5: $ {:.0f}\n'.format(g5)) 
  f_answer.write('Group 6: $ {:.0f}\n'.format(g6))

  #q3
  # for i in returns_data:
    
  #   if i[1] != "STATE":
  #     # if int(i[0]) - int(i[0]) != 0:
  #     f_answer.write(i[0])
  #     n1 = get_state_name(states, i[1])
  #     pop = get_state_population(populations, n1)
  #     f_answer.write(pop)
  f_answer.write(answer_header(3, question_titles))
  dic_income = {}
  for i in range(1, len(returns_data)):
    if returns_data[i][1] not in  dic_income:
      dic_income[returns_data[i][1]] = 0
    dic_income[returns_data[i][1]] += int(returns_data[i][indxA04800])

  for key in dic_income:
    state = get_state_name(states, key)
    state_pop = get_state_population(populations, state)
    avg = (dic_income[key] / state_pop) *1000

    f_answer.write('{} : $ {:.0f}\n'.format(key,avg))

  user_input = input('Enter State: ')
  # user_state = user_input
  # f_answer.write(state_answer_header(0, question_states) + get_state_name(returns_data, user_state))
    
 #q4
  
  dic_state = {}
  for i in range(1, len(returns_data)):
    if returns_data[i][1] not in dic_state:
      dic_state[returns_data[i][1]] = 0
    dic_state[returns_data[i][1]] += int(returns_data[i][indxN1])
  state_income = (dic_income[user_input] / dic_state[user_input]) * 1000

  f_answer.write(answer_header(4, question_titles))
  f_answer.write('$ {:.0f}'.format(state_income))
 #q5, 6, 7
  
  for i in range(1,len(returns_data)):
    if returns_data[i][1] == user_input:
      if returns_data[i][indxAGI] == '1':
        g1A = (int(returns_data[i][indxA04800])/ int(returns_data[i][indxN1]))*1000

        g1B = (int(returns_data[i][indxNumdep])/ int(returns_data[i][indxN1]))

        g1C = (int(returns_data[i][indxN1]) - int(returns_data[i][indxN04800]))/int(returns_data[i][indxN1])*100
      if returns_data[i][indxAGI] == '2':
        g2A = (int(returns_data[i][indxA04800])/ int(returns_data[i][indxN1]))*1000

        g2B = (int(returns_data[i][indxNumdep])/ int(returns_data[i][indxN1]))

        g2C = (int(returns_data[i][indxN1]) - int(returns_data[i][indxN04800]))/int(returns_data[i][indxN1])*100
      if returns_data[i][indxAGI] == '3':
        g3A = (int(returns_data[i][indxA04800])/ int(returns_data[i][indxN1]))*1000

        g3B = (int(returns_data[i][indxNumdep])/ int(returns_data[i][indxN1]))

        g3C = (int(returns_data[i][indxN1]) - int(returns_data[i][indxN04800]))/int(returns_data[i][indxN1])*100
      if returns_data[i][indxAGI] == '4':
        g4A = (int(returns_data[i][indxA04800])/ int(returns_data[i][indxN1]))*1000

        g4B = (int(returns_data[i][indxNumdep])/ int(returns_data[i][indxN1]))

        g4C = (int(returns_data[i][indxN1]) - int(returns_data[i][indxN04800]))/int(returns_data[i][indxN1])*100
      if returns_data[i][indxAGI] == '5':
        g5A = (int(returns_data[i][indxA04800])/ int(returns_data[i][indxN1]))*1000

        g5B = (int(returns_data[i][indxNumdep])/ int(returns_data[i][indxN1]))

        g5C = (int(returns_data[i][indxN1]) - int(returns_data[i][indxN04800]))/int(returns_data[i][indxN1])*100
      if returns_data[i][indxAGI] == '6':
        g6A = (int(returns_data[i][indxA04800])/ int(returns_data[i][indxN1]))*1000

        g6B = (int(returns_data[i][indxNumdep])/ int(returns_data[i][indxN1]))

        g6C = (int(returns_data[i][indxN1]) - int(returns_data[i][indxN04800]))/int(returns_data[i][indxN1])*100

  f_answer.write(answer_header(5, question_titles))

  f_answer.write('Group 1: $ {:.0f} \n'.format(g1A))
  f_answer.write('Group 2: $ {:.0f} \n'.format(g2A))
  f_answer.write('Group 3: $ {:.0f} \n'.format(g3A))
  f_answer.write('Group 4: $ {:.0f} \n'.format(g4A))
  f_answer.write('Group 5: $ {:.0f} \n'.format(g5A))
  f_answer.write('Group 6: $ {:.0f} \n'.format(g6A))

  f_answer.write(answer_header(6, question_titles))

  f_answer.write('Group 1:  {:.2f} \n'.format(g1B))
  f_answer.write('Group 2:  {:.2f} \n'.format(g2B))
  f_answer.write('Group 3:  {:.2f} \n'.format(g3B))
  f_answer.write('Group 4:  {:.2f} \n'.format(g4B))
  f_answer.write('Group 5:  {:.2f} \n'.format(g5B))
  f_answer.write('Group 6:  {:.2f} \n'.format(g6B))

  f_answer.write(answer_header(7, question_titles))

  f_answer.write('Group 1: {:.2f}% \n'.format(g1C))
  f_answer.write('Group 2: {:.2f}% \n'.format(g2C))
  f_answer.write('Group 3: {:.2f}% \n'.format(g3C))
  f_answer.write('Group 4: {:.2f}% \n'.format(g4C))
  f_answer.write('Group 5: {:.2f}% \n'.format(g5C))
  f_answer.write('Group 6: {:.2f}% \n'.format(g6C))

  #q8
  user_input_pop = get_state_population(populations,get_state_name(states,user_input))
  avg_per_resident = (dic_income[user_input] / user_input_pop) * 1000

  f_answer.write(answer_header(8, question_titles))
  f_answer.write('$ {:.0f}'.format(avg_per_resident))      

  #q9
  N1total = 0
  for i in returns_data[1:]:
    if i[1] == user_input:
      N1total += int(i[indxN1])
  
  for i in range(1,len(returns_data)):
    if returns_data[i][1] == user_input:
      if returns_data[i][indxAGI] == '1':
        q9avg1 = (int(returns_data[i][indxN1]) / N1total)*100
      if returns_data[i][indxAGI] == '2':
        q9avg2 = (int(returns_data[i][indxN1]) / N1total)*100
      if returns_data[i][indxAGI] == '3':
        q9avg3 = (int(returns_data[i][indxN1]) / N1total)*100
      if returns_data[i][indxAGI] == '4':
        q9avg4 = (int(returns_data[i][indxN1]) / N1total)*100
      if returns_data[i][indxAGI] == '5':
        q9avg5 = (int(returns_data[i][indxN1]) / N1total)*100
      if returns_data[i][indxAGI] == '6':
        q9avg6 = (int(returns_data[i][indxN1]) / N1total)*100
  
  f_answer.write(answer_header(9, question_titles))
  f_answer.write('Group 1:  {:.2f}% \n'.format(q9avg1))
  f_answer.write('Group 2:  {:.2f}% \n'.format(q9avg2))
  f_answer.write('Group 3:  {:.2f}% \n'.format(q9avg3))
  f_answer.write('Group 4:  {:.2f}% \n'.format(q9avg4))
  f_answer.write('Group 5:  {:.2f}% \n'.format(q9avg5))
  f_answer.write('Group 6:  {:.2f}% \n'.format(q9avg6)) 


  #q10
  A04800_total = 0
  for i in returns_data:
    if i[1] != 'STATE':
      if i[1] == user_input:
        A04800_total += int(i[indxA04800])
  
  for i in range(1,len(returns_data)):
    if returns_data[i][1] == user_input:
      if returns_data[i][indxAGI] == '1':
        q10avg1 = (int(returns_data[i][indxA04800]) / A04800_total)*100
      if returns_data[i][indxAGI] == '2':
        q10avg2 = (int(returns_data[i][indxA04800]) /A04800_total)*100
      if returns_data[i][indxAGI] == '3':
        q10avg3 = (int(returns_data[i][indxA04800]) / A04800_total)*100
      if returns_data[i][indxAGI] == '4':
        q10avg4 = (int(returns_data[i][indxA04800]) / A04800_total)*100
      if returns_data[i][indxAGI] == '5':
        q10avg5 = (int(returns_data[i][indxA04800]) / A04800_total)*100
      if returns_data[i][indxAGI] == '6':
        q10avg6 = (int(returns_data[i][indxA04800]) /  A04800_total)*100

  f_answer.write(answer_header(10, question_titles))      
  f_answer.write('Group 1: {:.2f}% \n'.format(q10avg1))
  f_answer.write('Group 2: {:.2f}% \n'.format(q10avg2))
  f_answer.write('Group 3: {:.2f}% \n'.format(q10avg3))
  f_answer.write('Group 4: {:.2f}% \n'.format(q10avg4))
  f_answer.write('Group 5: {:.2f}% \n'.format(q10avg5))
  f_answer.write('Group 6: {:.2f}% \n'.format(q10avg6))
  

  
  

main()

