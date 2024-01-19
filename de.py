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
        
p1=Phone()
p1.set_color("black")
p1.set_cost(50000)
p1.show_color()
p1.show_cost()
p1.make_phone()
p1.play_games()
