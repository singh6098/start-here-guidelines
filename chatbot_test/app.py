from tkinter import *
from test_chatbot import load_knowledge_base, find_best_match, get_answer_for_question, save_knowledge_base
#from chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
bot_name = "BOT"
suggestion = ['Bot: I don\'t know the answer please teach me\n\n','You: skip or Type the answer \n\n','skip','Type the answer']
msgTemp :str = ""
msgOldTemp= [None]

oldmsg = "" 
knowledge_base : dict = load_knowledge_base('knowledge_base.json')

class ChatApplication:
    
    def __init__(self):
        self.quit = False
        self.questionprev = ""
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        if self.quit == False:
           self.window.mainloop()
      
        
    def _setup_main_window(self):
        self.window.title("ChatBotApp")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
      # UpTrain button
        UpTrain_button = Button(self.window, text="UpdateBot", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda : self._on_updateBot_pressed(None)) # command=lambda t=text: click_button(t) 
        UpTrain_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22) 


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        oldmsg = msg 
        #self._insert_message(msg, "You")
        #self._noRet_insert_message(msg, "You")
        if(msg != ""):
          self._noRet_testing_chatbot(msg)
        if(oldmsg != msg):
          oldmsg = msg  
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        question:str = ""
         
        if( suggestion[0] != msg) and (suggestion[1] != msg) and (suggestion[2] != msg) and (suggestion[3] != msg):
          question:str = msg
        
        knowledge_base : dict = load_knowledge_base('knowledge_base.json')
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        if(msgOldTemp[-1] == suggestion[1] ):
           #response = msg1
           question = msgTemp.strip("You:")
           response = msg1.strip("You:")

        else:
           response = self._testing_chatbot(question, sender,knowledge_base)
        #msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        
        if (question != "") and (response != None) :
           
           msg2 = f"{bot_name}: {response}\n\n"
           self.text_widget.configure(state=NORMAL)
           self.text_widget.insert(END, msg2)
           self.text_widget.configure(state=DISABLED)
           self.text_widget.see(END)
        
        else :
           print(response)
    

        if response  != "skip" and response !=None:
           knowledge_base["questions"].append({"question":question, "answer": response } )
           save_knowledge_base('knowledge_base.json', knowledge_base)
           #print('Bot: Thank you! I learned  a new response! ')
           #self.text_widget.insert(END, 'Bot: Thank you! I learned  a new response! ')
           #self.text_widget.configure(state=DISABLED)
           #self.text_widget.see(END)
        
        if response == -1:
           self.quit = True 


    def _testing_chatbot(self, user_input, user, knowledge_base):
      

      #while True:
      #user_input : str = input( "You : ")
        
      if user_input.lower() == "quit":
        return -1
        
      for q in knowledge_base["questions"]:
        question_list: list[str]  =  q["question"]

      best_match: str | None = find_best_match(user_input, [question_list] )

      if best_match :
        answer: str = get_answer_for_question(best_match, knowledge_base)
        #print(f'Bot: {answer}')
        return answer
           #self.text_widget.insert(END, f'Bot: {answer}')
           #self.text_widget.configure(state=DISABLED)
           #self.text_widget.see(END)
           #get_answer(answer)
      else:
          #print('Bot: I don\'t know the answer please teach me')
          self.text_widget.configure(state=NORMAL)
          self.text_widget.insert(END, 'Bot: I don\'t know the answer please teach me\n\n') 
          self.text_widget.configure(state=DISABLED)
          self.text_widget.see(END)
         
          #new_answer : str = input("skip or Type the answer ")

          #self.msg_entry.delete(0, END)
          new_msg = f"{user}: skip or Type the answer \n\n"
          self.text_widget.configure(state=NORMAL)
          self.text_widget.insert(END, new_msg)
          self.text_widget.configure(state=DISABLED)
          msgTemp = user_input
          msgOldTemp.append(new_msg)
          #new_msg = self.msg_entry.get()

          #new_answer : str = self._insert_message(new_msg, "You")
          return None
          
          if new_answer  != "skip":
            knowledge_base["questions"].append({"question":user_input, "answer": new_answer } )
            save_knowledge_base('knowledge_base.json', knowledge_base)
            #print('Bot: Thank you! I learned  a new response! ')
            #self.text_widget.insert(END, 'Bot: Thank you! I learned  a new response! ')
            #self.text_widget.configure(state=DISABLED)
            #self.text_widget.see(END)
            return new_answer
            #get_answer(new_answer)
          else:
            return None          
    
    def _on_updateBot_pressed(self, event):
      
      msg = self.msg_entry.get()
      if msg != "skip" and self.questionprev != "":
        knowledge_base["questions"].append({"question":self.questionprev, "answer": msg } )
        save_knowledge_base('knowledge_base.json', knowledge_base)
        print('Bot: Thank you! I learned  a new response! ')
        self._noRet_insert_message('Thank you! I learned  a new response! ',bot_name)
      else :
         self.msg_entry.delete(0, END)


    def _noRet_insert_message(self, msg, sender):
      if not msg:
        return
      self.msg_entry.delete(0, END)
      msg1 = f"{sender}: {msg}\n"
      self.text_widget.configure(state=NORMAL)
      self.text_widget.insert(END, msg1)
      self.text_widget.configure(state=DISABLED)

    def _disableSendButton(self):
      self.send_button.config(state = DISABLED)  
    
    def _enableSendButton(self):
      self.send_button.config(state = NORMAL)  

    def _noRet_testing_chatbot(self ,user_input):
      #user_input : str = input( "You : ")
      #user_input = self.msg_entry.get()
      self._noRet_insert_message(user_input, "You")  
      #if user_input.lower() == "quit":
      #  break
        
      for q in knowledge_base["questions"]:
        question_list: list[str]  =  q["question"]

      best_match: str | None = find_best_match(user_input, [question_list] )
      # best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]] )   

      if best_match :
        answer: str = get_answer_for_question(best_match, knowledge_base)
        print(f'Bot: {answer}')
        msg2 = f"{bot_name}: {answer}\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
        self.questionprev = ""
      else:
        user_input_str = user_input 
        print('Bot: I don\'t know the answer please teach me')
        dummy_suggest = 'I don\'t know the answer please teach me'
        #new_answer : str = input("skip or Type the answer ")
        
        self.questionprev = user_input
        
        self._noRet_insert_message(dummy_suggest,bot_name)
        self._noRet_insert_message("skip or Type the answer and press Update",bot_name)
    
        
        
        #self.msg_entry.delete(0, END) 

        #if new_answer  != "skip" and new_answer != "":
        #if  user_input_str != "skip" and new_answer != "":
        #  knowledge_base["questions"].append({"question":user_input_str, "answer": user_input } )
        #  save_knowledge_base('knowledge_base.json', knowledge_base)
        #  print('Bot: Thank you! I learned  a new response! ')
        #  self._noRet_insert_message('Bot: Thank you! I learned  a new response! ',bot_name)
      
         
if __name__ == "__main__":
    app = ChatApplication()
    app.run()