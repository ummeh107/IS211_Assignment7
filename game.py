
import random
import argparse


# No of Player build
def buildPlayer(numPlayers):
    player={}
    for i in range(1, int(numPlayers)+1):
        player[i] = 0
    return player        

# decision for roll or hold
def decision(player):
    p=0
    win=0    
    result = 0
    while win < 100:
        print("Are you want to roll or hold --")
        decision = input("Please enter 'r' or 'h' :")
        currentPlayer = (p % len(player)) + 1
        if decision == 'r':
            roll = random.randint(1,6)
            print("Player "+str(currentPlayer)+" has rolled: "+str(roll))
            if roll == 1:
                result = 0
                p += 1
                print("Next Players Turn..")
            else:
                result += roll
        elif decision == 'h':
            player[currentPlayer] += result
            result = 0
            p+=1
            print("Player "+str(currentPlayer)+" Score is :" + str(player[currentPlayer]))
            print("Next Players Turn..")

        win = max(player.values())           
    # print(player)
    # print(max(player.items(), key=lambda x : x[1]))
    return max(player.items(), key=lambda x : x[1])


# main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help='please enter number of players..')
    args = parser.parse_args()

    if args.numPlayers != None:
        player = buildPlayer(args.numPlayers)
        
        againPlay=True
        while againPlay:        
            winner = decision(player)
            print("Winner is Player "+ str(winner[0]))
            print("\nAre you play again!")
            play = input("y/n :")
            player = buildPlayer(args.numPlayers)
            if play == 'n':
                againPlay = False
    else:
        print("Please enter valid argument value! as like..")
        print("python game.py --numPlayers 'number'")
        parser.exit()
     

if __name__ == "__main__":
    main()