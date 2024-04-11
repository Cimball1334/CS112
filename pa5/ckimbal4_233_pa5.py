#-------------------------------------------------------------------------------
# Author: Craig Kimball 
# Assignment 5
# Date: 10/17/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------

#function group_together takes parameters players, a list of names, and team, the number of people to be in each team
#the function rewrites the passed in list as a 2d list dividing the names up into their teams, or the remainder of players less than team
def group_together(players, team):
    teams = []
    #segmenting the teams up by the number defined
    for i in range(int(len(players)/team)):
        if len(players) - i*team >= team:
            teams.append(players[i*team:i*team+team])
        else:
            teams.append(players[i*team:])    
   
    #checks if their is remainder of players and adds them to the end
    if(len(players)%team > 0):
        teams.append(players[len(players) - len(players)%team:])    
    players.clear()
    
    #sets the initial list for output
    for i in range(len(teams)):
        players.append(teams[i])

#the function monitor_bets takes parameters playerInfo, a 2d array containing a list of player names and their associated number, and bets, a 2d list that contains associated player numbers and the ammount bet on them
#the function rewrites the passed in player info list to add the value bet on each player
def monitor_bets(playerInfo, bets):
    newList = []
    # creating a new list with a 3rd element of the internal arrays
    for i in range(len(playerInfo)):
        newList.append([playerInfo[i][0],playerInfo[i][1],0])
    
    #since not every player has a bet on them or a player may have multiple, we have to search through the bets first
    for bet in bets:
        for i in range(len(playerInfo)):
            if bet[0] == playerInfo[i][1]:
                #if this player has a bet on them
                #then it adds it to the new list
                newList[i][2]+=bet[1]
                
    #removing all 0's in list for people who have no bets on them
    for i in range(len(newList)):
        if(newList[i][2] == 0):
            newList[i] = newList[i][:2]
    
    #rewriting the old list to contain the new bet information
    playerInfo.clear()
    for i in range(len(newList)):
        playerInfo.append(newList[i])
        
#function compress_info takes in parameter playerTrack that is a 2d list containing the amount bet on each player for each game
#the functionm modifies the originial list to consolidate the list to be every bet placed on each player through all games
def compress_info(playerTrack):
    newList = []
    
    for i in range(len(playerTrack)):     
        isIn = False
        
        #this determines whether the player has already been added to the new list 
        for j in range(len(newList)):
            if playerTrack[i][0] == newList[j][0]:
                isIn= True
        
        #if the player is in the list, we have to sum the amount bet
        if(isIn):
            #i is player location in playerTrack
            for j in range(len(newList)):
                #must find where to add it in
                if(playerTrack[i][0] == newList[j][0]):
                    newList[j][1] += playerTrack[i][1]
                    newList[j][1] = round(newList[j][1], 2)
        
        #if the player is not in the list we add them
        else:
            newList.append(playerTrack[i])
        
    #this modifies the original list for output  
    playerTrack.clear()
    for i in range(len(newList)):
        playerTrack.append(newList[i])
        
#this function set_of_games takes parameters games, a dictionary of games, the name of the game, and the number of people who won, and an int search number
#it returns a set of games where the winners are greater than the search number
def set_of_games(games, searchNum):
    #used set(()) insead of {} to force it to be an empty set and not a blank object
    newSet = set(())
    for key in games:
        if(games[key][1] >= searchNum):
            newSet.add(games[key][0])
    
    return newSet
# players = [456, 218, 67, 1, 101, 199]
# group_together(players, 3) #nothing is returned!
# print(players)
#
# players = [456, 218, 67, 1, 101, 199]
# group_together(players, 2) #nothing is returned!
# print(players)
#
# players = [456, 218, 67, 1, 101, 199]
# group_together(players, 5) #nothing is returned!
# print(players)
#
# playerInfo = [["Seong Gi-hun", 456], ["Cho Sang-woo", 218], ["Kang Sae-byeok", 67]]
# bets = [[67, 1000000.00], [67, 2000000.00], [218, 3000000.00]]
# monitor_bets(playerInfo, bets) #nothing is returned!
# print(playerInfo)
#
#
# playerInfo = [["Seong Gi-hun", 456], ["Cho Sang-woo", 218],
#  ["Kang Sae-byeok", 67], ["Abdul Ali", 199], ["Byeong-gi", 111]]
# bets = [[199, 100000], [111, 10000], [218, 10000], [111, 50], [67, 100000.00],
#  [199, 50000.00]]
# monitor_bets(playerInfo, bets) #nothing is returned!
# print(playerInfo) 
#
#
# playerTrack = [[456, 3000000], [10, 10], [67, 10000], [199, 400000], [10, 20]]
# compress_info(playerTrack) #nothing is returned!
# print(playerTrack)
#
#
# playerTrack = [[456, 100000], [456, 200000.00], [67, 300000],
#  [67, 200000.00], [199, 234569.00], [456, 3000000.00]]
# compress_info(playerTrack) #nothing is returned!
# print(playerTrack) 
#
#
#
# games = {
#  'game 1' : ["RLGL", 201],
#  'game 2' : ["PPOPGI", 80],
#  'game 3' : ["Tug of War", 44],
#  'game 4' : ["Marbles", 16],
#  'game 5' : ["Bridge", 3],
#  'game 6' : ["Squid", 1]
#  }
#
# print(set_of_games(games, 10))
# print(set_of_games(games, 70))

