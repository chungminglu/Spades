
# coding: utf-8

# In[8]:

import time
import threading
import json
import re,requests
from bs4 import BeautifulSoup
from random import randint
from datetime import datetime


class myThread1 (threading.Thread):
    def __init__(self, threadID, name,initurl,delay,proxy):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.initurl=initurl
        self.delay=delay
        self.proxy=proxy
#         self.dest=dest


    def run (self):
        Mt_Kurama(self.initurl,self.delay,self.proxy)

class myThread2 (threading.Thread):
    def __init__(self, threadID, name,initurl,delay,proxy):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.initurl=initurl
        self.delay=delay
        self.proxy=proxy
#         self.dest=dest


    def run (self):
        Kennin_ji_Temple(self.initurl,self.delay,self.proxy)
        
        
        

def Mt_Kurama(initurl,delay,proxy):
    url1 = "https://www.tripadvisor.com.tw/Attraction_Review-g298564-d1424607-Reviews-Mt_Kurama-Kyoto_Kyoto_Prefecture_Kinki.html"
    res = requests.get(url1)
    soup = BeautifulSoup(res.text,'lxml')

    total_topic = soup.select('.pagination-details > b')[2].text
    total_page = soup.select('.pageNum')[6].text

    title = "鞍馬山"
    topic_info = {"景點" : title}


    topic_infos =[]
    page = 1
    for i in range(0,int(total_page)*10,10):
        url = "https://www.tripadvisor.com.tw/Attraction_Review-g298564-d1424607-Reviews-or{}-Mt_Kurama-Kyoto_Kyoto_Prefecture_Kinki.html".format(i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'lxml')
        try:
            for j in range(2,12):
                rating = soup.select('.review')[j].select('.ui_bubble_rating')[0].get('class')[1].split('_')[1]
                topic_titles = soup.select('.review')[j].select('.noQuotes')[0].text
                author = soup.select('.review')[j].select('.expand_inline')[0].text
                ratingDate = datetime.strptime(soup.select('.review')[j].select('.ratingDate')[0].get('title').replace('年','-').replace('月','-').replace('日',''),'%Y-%m-%d').strftime("%Y-%m-%d")
                command = soup.select('.review')[j].select('.partial_entry')[0].text
                commands = {"回覆日期" : ratingDate, "評分" : rating , "id" : author,"回覆標題" : topic_titles , "回覆內文" :command}

                topic_infos.append(commands)
        except:
            pass
        time.sleep(2)

        print("{}page{}完成!".format(title,page))
        page+=1

    topics ={"景點" : title, "評論" : topic_infos }
    print(topics)

    dest_path = "C:\\Users\\Java\\Desktop\\TripAdvastor\\{}\\{}.text".format(title,title)
    with open(dest_path,'a',encoding="utf-8") as f:
    #         f.write(str(test))
        f.write(json.dumps(topics,sort_keys=True,ensure_ascii=False))
        f.close()

def Kennin_ji_Temple(initurl,delay,proxy):
    url2 = "https://www.tripadvisor.com.tw/Attraction_Review-g298564-d1386175-Reviews-Kennin_ji_Temple-Kyoto_Kyoto_Prefecture_Kinki.html"
    res = requests.get(url2)
    soup = BeautifulSoup(res.text,'lxml')

    total_topic = soup.select('.pagination-details > b')[2].text
    total_page = soup.select('.pageNum')[6].text

    title = "建仁寺"
    topic_info = {"景點" : title}


    topic_infos =[]
    page = 1
    for i in range(0,int(total_page)*10,10):
        url2 = "https://www.tripadvisor.com.tw/Attraction_Review-g298564-d1386175-Reviews-or{}-Kennin_ji_Temple-Kyoto_Kyoto_Prefecture_Kinki.html".format(i)
        res = requests.get(url2)
        soup = BeautifulSoup(res.text,'lxml')
        try:
            for j in range(2,12):
                rating = soup.select('.review')[j].select('.ui_bubble_rating')[0].get('class')[1].split('_')[1]
                topic_titles = soup.select('.review')[j].select('.noQuotes')[0].text
                author = soup.select('.review')[j].select('.expand_inline')[0].text
                ratingDate = datetime.strptime(soup.select('.review')[j].select('.ratingDate')[0].get('title').replace('年','-').replace('月','-').replace('日',''),'%Y-%m-%d').strftime("%Y-%m-%d")
                command = soup.select('.review')[j].select('.partial_entry')[0].text
                commands = {"回覆日期" : ratingDate, "評分" : rating , "id" : author,"回覆標題" : topic_titles , "回覆內文" :command}

                topic_infos.append(commands)
        except:
            pass
        time.sleep(randint(1,3))

        print("{}page{}完成!".format(title,page))
        page+=1

    topics ={"景點" : title, "評論" : topic_infos }
    

    dest_path = "C:\\Users\\Java\\Desktop\\TripAdvastor\\{}\\{}.text".format(title,title)
    with open(dest_path,'a',encoding="utf-8") as f:
    #         f.write(str(test))
        f.write(json.dumps(topics,sort_keys=True,ensure_ascii=False))
        f.close()
        
  
        
        
        
        
        
        
        
if __name__ == '__main__':
# #     gg = 1
    
    url1 = "https://www.tripadvisor.com.tw/Attraction_Review-g298564-d1424607-Reviews-Mt_Kurama-Kyoto_Kyoto_Prefecture_Kinki.html"
    url2 = "https://www.tripadvisor.com.tw/Attraction_Review-g298564-d1386175-Reviews-Kennin_ji_Temple-Kyoto_Kyoto_Prefecture_Kinki.html"
    
#     dest="C:\\Users\\Java\\Desktop\\TripAdvastor\\銀閣寺\\command{}.txt".format(gg)
#     dest1="C:\\Users\\Java\\Desktop\\TripAdvastor\\清水寺\\command{}.txt".format(gg)
    threads1=myThread1(1,"Mt_Kurama",url1,2,"https:121.41.55.187:9999")
    threads2=myThread2(2,"Kennin_ji_Temple",url2,2,"https:221.206.5.183:53281")
        
    
    threads1.start()
    threads2.start()
    
    # with open(dest,'a',encoding="utf-8") as f :
    #     f.write(thread1.name+"\n")
    #     f.close()
    # with open(dest1,'a',encoding="utf-8") as f :
    #     f.write(thread2.name+"\n")
    #     f.close()
#     t1=[]
#     t1.append(threads1)
#     t1.append(threads2)
# #     t1.append(threads3)
# #     t1.append(threads4)
# #     t1.append(threads5)
# #     t1.append(threads6)
# #     t1.append(threads7)
# #     t1.append(threads8)
#     for t in t1:
#         t.join()
#     print(" {} Exiting Main Thread".format(t))
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



