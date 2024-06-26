nominee1 = input("Enter the name of the 1st nominee: ")
nominee2 = input("Enter the name of the 2nd nominee: ")

# Initially, vote count for both must be 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_of_voter = len(voter_id)

while True:
    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter.")
        voter_id.remove(voter)
        vote = int(input(f"Enter your vote (1 for {nominee1}, 2 for {nominee2}): "))
        if vote == 1:
            nm1_votes += 1
        elif vote == 2:
            nm2_votes += 1
        else:
            print("Invalid vote! Please enter 1 or 2.")
    else:
        print("You are not a registered voter or you have already voted.")
    
    if len(voter_id) == 0:
        print("Voting session is over!!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes / no_of_voter) * 100
            print(f"{nominee1} has won the election with {percent}% of votes.")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes / no_of_voter) * 100
            print(f"{nominee2} has won the election with {percent}% of votes.")
            break
        else:
            print("Both have an equal number of votes! Government will decide the winner.")
            break