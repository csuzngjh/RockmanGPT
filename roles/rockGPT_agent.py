
import langchain
import soul.chatllm
import soul.chinese_text_splitter


class RockStudent:
    def __init__(self):
        self.ability = {'intelligence': 50, 'perseverance': 70, 'social_skill': 60}   
        self.current_goal = 'pass exam'
        self.soul = 'chatglm'

        self.card = ['white_tiger', 'black_turtle']
        self.tasklist = {'exam_prep': ['review_notes', 'do_practice_problems'],  
                         'side_project': ['code', 'test', 'document']}
        self.short_term_memory = []
        self.long_term_memory = {'knowledge': {'math': 50, 'programming': 70}, 
                                 'experiences': []}     
    
    def set_current_goal(self,
                         goal='pass the test'):
        self.current_goa = 	goal.lower()    #converts goal to lower case
        print('\nI am currently on the%s goal'% self.current_goal)   #displays current goal

        
    def attend_exam(self): 
        print('Attend exam, show the results!')
        
    def ask_tutor_for_help(self):
        print('Ask tutor to explain difficult problems!') 
    
    def search_for_information(self):
        print('Browse information, ask classmates!')
        
    def store_information(self):
        print('Record knowledge points and solutions')
            
    def ask_question(self, question_context):
        question = question_context
        print(f'Ask a question: {question}')
         
    def think(self, thinking_context, dfs or bfs):
        print(f'Adopt {dfs or bfs} search to think about {thinking_context}')
        
    def sleep(self): 
        print('Sleep well, and be energetic the next day!')
        
    def upgrade(self):
        self.ability['intelligence'] += 10
        print('Upgrade! Intelligence increased by 10 points')  
        
    def transform(self):
        if 'white_tiger' in self.card and 'black_turtle' in self.card:
            print('Transform into a master of both land and water!')
        else:
            print('Not enough cards to transform!')
