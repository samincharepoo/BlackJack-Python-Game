# FINAL PROJECT-SAMIN CHAREPOO 'A' CODE
import random

# Global constant for the winning number of cards
MAX = 21
#player Class
class Player():
    def __init__(self,n, h=0):
        self.name=n
        self.handVal=h
        self.hand=[]

    def __str__(self):
        return(self.name + " has a hand value of " + str(self.handVal)+ ' -')

    #INPUT: none (self)
    #PROCESS: prints the hand in terms of values and suits
    #OUTPUT: pritns statement ^
    def displayHand(self):
        print(self.name+'s hand includes:')
        for item in self.hand:
            print(item)
        
        
    #INPUT: the card value
    #PROCESS: adds the new value to the handValue
        #unless card is an Ace; then 11 or 1 (if +11 would make > 21)
    #OUTPUT: new handValue
    def update_hand_value(self,card):
        self.hand.append(card)
       
        if card!='A':
            self.handVal+=int(card.value)
       
        elif self.handVal > 10:
            self.handVal +=int(card.value)
        else: 
            self.handVal += 11

#card class
class Card():
    def __init__ (self, suit, rank, value):
        self.rank=rank
        self.suit=suit
        self.value=value
    def __str__(self):
        return('rank:'+(self.rank)+ ' suit: '+(self.suit))
    
    #INPUT:none
    #PROCESS: setting blackjack value with rank
    #OUTPUT: value of blackjack
    def setValue():
        if self.rank=='A':
            self.value=1
            return self.value
        elif self.rank in 'JKQ':
            self.value=10
            return self.value
        else:
            self.value=self.rank
            return self.value
        

    
    
# main function
#INPUT:none
#PROCESS: get players name, call different functions, deal the cards while certain conditions are met,
        #print statements on who won
#OUTPUT:print statements^^
def main():
    instructions()
    # Local variables
    name1 = input("What is your name, player1? ")
    player1= Player(name1)
    print('Player 2 will be refered to as "Dealer"')
    name2 = ('Dealer')
    player2= Player(name2)
    deck = create_deck()
    hitorstay1='y'
    dealerhitorstay='y'

    while player1.handVal <= MAX and player2.handVal <= MAX and hitorstay1=='y' or dealerhitorstay=='y' :

        if hitorstay1=='y':
            value, card = deal(deck)
            player1.update_hand_value(card)
            print(player1, ' was dealt', card)
            player1.displayHand()
            hitorstay1=hit_or_stay(player1,deck)
      
            
        if dealerhitorstay=='y':
            value, card = deal(deck)
            player2.update_hand_value(card)
            print(player2 , ' was dealt', card)
            player2.displayHand()
            print()
            dealerhitorstay=dealerHitOrStay(player2,deck)
     
            
        


    # Determine the winner.
    if player1.handVal > MAX and player2.handVal > MAX:
        print("Both busted! There is no winner.")
        
    elif player1.handVal<MAX and player2.handVal < MAX:
        if player1.handVal>player2.handVal:
            print (player1,player1.name,'won!')
        elif player2.handVal>player1.handVal:
            print(player2, player2.name, 'won!')
        elif player2.handVal==player1.handVal:
            print ("It is a tie!")
            
    elif player1.handVal > 21:
        print(player2, player2.name,'won!')
        
    elif player2.handVal > 21:
        print(player1, player1.name,'won!')

    elif player1.handVal<MAX and player2.handVal==MAX:
        print(player2, player2.name, 'won!')

    elif player2.handVal<MAX and player1.handVal==MAX:
        print(player1, player1.name, 'won!')
        

        
#INPUT:none
#PROCESS:print out the instructions
#OUTPUT: none
def instructions(): 
    print ('Hello! We will be playing BlackJack! \nEach card in the deck has a value from 1-10.\nThe player with the highest value sum of cards in their hand that is still<=21 wins.\nPlayer 1, you will play against player 2, who will act as the dealer.')


#Deck related functions (create and deal random card) 
#INPUT: None
#PROCESS: creates a deck of cards dictionary by cycling through all combinations of suits and ranks
#OUTPUT: returns the 52 entry deck dictionary
def create_deck():
    # Set up local variables
    suits = ['♠','♥','♦','♣']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}

    # Create list of all the card values
    ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for i in range(2,11):
        ranks.append(str(i))

    # Initialize deck
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank in special_values:
                value=special_values[rank]
                deck.append(Card(suit,rank,value))
    return deck

###########################
#INPUT: player, deck
#PROCESS: asks player if they want another card
#OUTPUT: returns the input to the main funciton.

def hit_or_stay(player,deck):
    while player.handVal <= MAX:
        hitorstay = input("Do you want another card? (Y/N)").lower()
        return hitorstay

#INPUT: player, deck
#PROCESS: makes the dealer hit a card as long as their handvalue is less than or equal to 16
#OUTPUT: returns thedealerhitorstay    
def dealerHitOrStay(player,deck):
    while player.handVal <= 16:
        dealerhitorstay = 'y'
        return dealerhitorstay
               
            
    
###########################

#INPUT: deck dictionary
#PROCESS: ,shuffles deck, uses the Card Class with deck as a list of cards
#OUTPUT: returns randomly selected key, value pair. deck is one entry smaller
def deal(deck):
    random.shuffle(deck)
    card = deck.pop()
    return(deck,card)
    

# Call the main function.
main()

