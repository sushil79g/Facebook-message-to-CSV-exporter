from bs4 import BeautifulSoup
import re
import csv

with open('your_messages.html',encoding="utf8") as fb: #as facebook saves message homepage in your_messages.html
    soup = BeautifulSoup(fb, 'lxml')

soup = soup.find("div", {'class':'_4t5n'})
name = [] #All the chat head names
link = [] #link for the chat head head messagges
c = 0

for div in soup.findAll('div'):
    
    a = div.a
    try:
        name.append(a.string)
        try:
            link.append('.' + a['href'][8:])
            # print()
        except:
            pass
    except:
        pass


total_chat = len(name) #Total  number of chat head
all_name = name #copying names to another variable


for index in range(0,len(name)):
    name = all_name
    print(index,'of',total_chat)
    
    try: #Try helps in throwing error for group chat 
        
        with open(link[index],encoding="utf8") as inside:
            soup = BeautifulSoup(inside, 'lxml')
        soup = soup('div',{'class':"_4t5n"})
        
        for res in soup:
            text = res.text #text consist chat text only
        
        name = name[index]
        rep = " "+name+" "
        rep2 = " "+'Sushil Ghimire'+ " "
        text = text.replace(name,rep)
        text = text.replace("Sushil Ghimire",rep2)
        month = ['Jan','Feb','Mar','Apr','Aug','May','Jun','Jul','Sep','Oct','Nov','Dec']
        
        if 'PM' in ''.join(text):
            tail = 'abc'
            text_ex = text
            new_text = []
            
            while len(tail)!=0:
                head,sep,tail = text_ex.partition('PM')
                new_text.append(head[:-19])
                text_ex = tail
            
            text = new_text

        if 'AM' in ''.join(text):
            text = ''.join(text)
            tail = 'abc'
            text_ex = text
            new_text = []
            
            while len(tail)!=0:
                head,sep,tail = text_ex.partition('AM')
                new_text.append(head[:-19])
                text_ex = tail
        
        final_text = ''.join(new_text)

        
        def find_middle(text, start_text, end_text):
            
            _,_,rest = text.partition(start_text)
            result,_,_ = rest.partition(end_text)
            result = result.replace(start_text,' ')
            result = result.replace(end_text,' ')
            
            return result

        end_text = name
        start_text = 'Sushil Ghimire'
        
        
        try: #try to remove error when you have no chat
            if final_text.index(start_text) > final_text.index(end_text):
                start_text,end_text = end_text, start_text 
        except:
            pass
        
        
        start_name = start_text
        end_name = end_text
        tail = 'abc'
        test = []
        final_text_copy = final_text
        
        
        while len(tail) != 0:
            head,sep,tail = final_text_copy.partition(end_text)
            test.append(find_middle(head,start_text,end_text))
            start_text , end_text= end_text, start_text
            final_text_copy = sep + tail
            
        if len(test) % 2==0:
            chat_starter = end_name
            reply_starter = start_name
        else:
            chat_starter = start_name
            reply_starter = end_name

        print('chat of sushil with ',name,' chat number:',index,'of',total_chat)
        chat_in_order = list(reversed(test))
        
        for ind in range(0, len(chat_in_order), 2):
            if chat_starter == name:
                lis = [name,chat_in_order[ind], chat_in_order[ind+1]]
            else:
                if ind == 0:
                    continue
                else:
                    lis =[name,chat_in_order[ind-1],chat_in_order[ind]]
            
            
            with open(r'name.csv', 'a+', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(lis)
    
    
    except:
        print('error')
        pass


