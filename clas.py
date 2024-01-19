class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color 
    def show_cost(self):
        return self.cost      
    def make_phone(self):
        print("let's make a phone call")
    def play_games(self):
        print("playing clash of clans")
        
p2=Phone()

p2.make_phone()
p2.play_games()            
p2.set_color("black")
p2.set_cost(50000)
p2.show_color()
p2.show_cost()