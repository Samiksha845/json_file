import json
import requests
import time
import os
from bs4 import BeautifulSoup

# file_name = "21_04_2020_17_07_22"+".json"
file_loc="C:\\Users\\SAMIKSHA SENGAR\\PycharmProjects\\samiksha\\data"

def tym(file_loc):
     file_name= time.strftime("%d_%m_%y_%H_%M_%S"+".json")
     file_path = os.path.join(file_loc,file_name)
     return file_path
# print(file_path)

get_url="https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2019"

def op(get_url):
     page = requests.get(get_url)
     soup = BeautifulSoup(page.text,"html.parser")

     table = soup.find_all("table", class_='wikitable')[1]
     rows=table.find_all("tr")
     headings=['title','director','cast','studio']


     row_list=[]
     for tr in rows:
          td=tr.find_all("td")
          row=[i.text for i in td]
          row_list.append(row)
          final_row=row_list[1:]

     final_list=[]
     for i in final_row[1:]:
          fi=dict(zip(headings,i))
          final_list.append(fi)

     final_dic={}
     final_dic['jan-mar']=final_list
     return final_dic

f_dict=op(get_url)
final =tym(file_loc)

def write():
     with open(final,'w') as fp:
        json.dump(f_dict,fp)
                                          # json_string = json.dumps(fi,ensure_ascii=False,indent=4)
write()                                    #print(json_string)


