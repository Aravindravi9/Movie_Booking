#python program to autamate ticket booking system

'''
check_seat_availability(movie_index,number_of_tickets): Checks seat availability for the given movie

calculate_ticket_price(movie_index,number_of_tickets): Calculates total ticket price for the given movie

generate_seat_number(movie_index,number_of_tickets): Allocates required number of seats for the given movie.

Seat numbers are generated starting from 1, prefixed by "M1-" for movie-1 and "M2-" for movie 2


Updates total number of tickets available for the given movie in list_total_tickets

Updates last seat number allocated for the given movie in list_last_seat_number

Returns the list of generated seat numbers

book_ticket(movie_name,number_of_tickets): Book tickets for the given movie.

Return 0, if movie name is invalid

Return -1, if enough tickets are not available for the given movie

Else,

Generates seat numbers

Calculates total ticket price'''

#Created on Fri Feb 14 11:54:57 2020

#@author: Aravind

class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[1,1]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        index=0
        if movie_name in Multiplex.__list_movie_name:
            if (movie_name =='movie1'):
                index =0 
            else:
                index=1
            
            if(self.check_seat_availability(index,number_of_tickets)):
               
                self.generate_seat_number(index,number_of_tickets)
                self.calculate_ticket_price(index,number_of_tickets)
                
            else:
                return -1
        
        
        else:
            return 0
        
    def  generate_seat_number(self,movie_index, number_of_tickets):
        
        if (movie_index == 0):
                movie_name ='M1-'
        else:
            movie_name ='M2-'
        lis=[]
        
        
        for i in range (1, number_of_tickets+1):
            lis.append(movie_name + str(Multiplex.__list_last_seat_number[movie_index]))
            Multiplex.__list_last_seat_number[movie_index] += 1
            
        Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
            
        
            
        self.__seat_numbers=lis    
        
        
        
        
        
        
booking1=Multiplex()
status=booking1.book_ticket("movie2",61)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())