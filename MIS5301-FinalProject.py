
# Import csv and os
import csv
import os
#from shutil import copyfile
from operator import itemgetter



#Team Data – parallel lists
TEAM_CODES = ['ATF',  'AZC',  'BFB',  'BLR',  'CAP',  'CHB',  'CLB',  'CNB',  'DLC',  'DTL',
              'DVB',  'GBP',  'HST',  'INC',  'JKJ',  'KCC',  'LAC',  'LAR',  'LVR',  'MMD',
              'MNV',  'NEP',  'NOS',  'NYG',  'NYJ',  'PHE',  'PTS',  'SFN',  'STS',  'TBB',  'TNT',  'WSC']
TEAM_NAMES = ['Atlanta Falcons', 'Arizona Cardinals', 'Buffalo Bills', 'Baltimore Ravens', 'Carolina Panthers',
              'Chicago Bears', 'Cleveland Browns', 'Cincinnati Bengals', 'Dallas Cowboys', 'Detroit Lions',
              'Denver Broncos', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars',
              'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Las Vegas Raiders', 'Miami Dolphins',
              'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets',
              'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers',
              'Tennessee Titans', 'Washington Commanders']

#Positions Data – parallel lists
POS_CODES = ['C', 'CB', 'DE', 'DT', 'FB', 'G', 'K', 'LB', 'LS', 'OT', 'P', 'QB', 'RB', 'S', 'TE', 'WR']
POS_NAMES = ['Center', 'Cornerback', 'Defensive end', 'Defensive tackle', 'Fullback', 'Guard', 'Kicker', 'Linebacker',
             'Long snapper', 'Offensive tackle', 'Punter', 'Quarterback', 'Running back', 'Safety', 'Tight end', 'Wide receiver']

# Global constants
INDENT1 = ' '*2
INDENT2 = ' '*4

CSVFILE = 'NFL-players.csv'
#TEMPFILE = 'NFL-temp.csv'


# Main function that validates the selected option

def main():
    #found = False

    #Open file for reading
    infile = open(CSVFILE, 'r', newline='')

    #Create reader
    reader = csv.reader(infile)

    #Read field names
    fields = next(reader)
    

    players  = []

    #Generate a list from reader
    for row in reader:  
        emp_id = int(row[0])
        lst_nm = row[1]
        fst_nm = row[2]
        team_cd = row[3]
        pos_cd = row[4]
        player_num = int(row[5])
        age = int(row[6])
        weight = int(row[7])
        height = int(row[8])
        year_of_exp = int(row[9])
        college = row[10]

        #Append the converted data
        new_row = [emp_id, lst_nm, fst_nm, team_cd, pos_cd, player_num, age, weight, height, year_of_exp, college]
        players.append(new_row)

    # Header
    print('*'*60)
    header = "Victorino Player Reporting Sytem"
    print(f'{header:^60}')
    print('*'*60)
    print()
    print(INDENT1, "1 - Team Roster Report")
    print(INDENT1, "2 - Filtered Players Report")
    print(INDENT1, "X - Exit")
    print()
    print('*'*60)
    
    
    y = False
    # loop that validates input value and calls the respective function
    while y == False:
        menu_option = input('  Enter a selection: ')
        print()
        if menu_option == '1':
            team_rost_rep(players)
           
        elif menu_option == '2':
            filt_play_rep(players)
            
        elif menu_option.upper() == 'X':
            exit()
            y = True
        else:
            print('  invalid option entered, kindly enter a valid input')
        

# Function for Team Roaster Report
def team_rost_rep(players):
    valid = False
    filt_players = []
    
    search_team_code = input("  Enter Team Code: ").upper()
    while not search_team_code.isalpha() or len(search_team_code) != 3:
        search_team_code = input("\n  Wrong Team Code entered.\n  Please enter a valid Team Code or R to go back to main menu: ")
        print()
        if search_team_code.upper() == 'R':
            return    
    for row in players:
        emp_id = row[0]
        lst_nm = row[1]
        fst_nm = row[2]
        team_cd = row[3]
        pos_cd = row[4]
        player_num = row[5]
        age = row[6]
        weight = row[7]
        height = row[8]
        year_of_exp = row[9]
        college = row[10]
        
        #Apply filter criteria
        if search_team_code == team_cd:
            valid = True
            new_row = [player_num, lst_nm, fst_nm, pos_cd, height, weight, college]
            filt_players.append(new_row) #Append the row that meets he condition to the filt_players list
        
    #print(filt_players)        
    if valid == False:
        print("  The Team Code entered could not be located. \n   You will be redirected to the Main Menu!!! \n")
        return
    else:    
        # Output header
        print(' ', '-'*47)
        print(' '*2, '*** Team Roaster Report (by Player Number) ***')
        print(' ', '-'*47, '\n')
        
        # Sort list
        sorted_filt_players = sorted(filt_players, key=itemgetter(0, 1))

        print(f' {"Player No"} {"LastName":^17} {"FirstName":^14}{"PosCode"}   {"Height"} {"Weight"} {"College"}')
        print(f' {"-"*9} {"-"*30}  {"-"*7}   {"-"*6} {"-"*6} {"-"*24}')
        # Display sorted list
        for row in sorted_filt_players:
            # player_num = row[0]
            # lst_nm = row[1]
            # fst_nm = row[2]
            # pos_cd = row[3]
            # height = row[4]
            # weight = row[5]
            # college = row[6]
            feet = (row[4]//12)
            inches = (round(row[4]%12))
            
            print(f' {row[0]:>9} {row[1]:>17}, {row[2]:<14} {"("+row[3]:>4})     {feet:}\'{inches:}\"  {row[5]:6}   {row[6]:24} \n')
        print(' ', '-'*84, '\n')
    
    input("  Enter to go back to the Main Menu...")

    
def filt_play_rep(players):
    
    filtered_players = []
    filtered_players1 = []
    filtered_players2 = []
    filtered_players3 = []
    filtered_players4 = []
    filtered_players5 = []
    filtered_players6 = []
    an_inp_ent = False
    
    
    print("  Enter any Filter Criteria... ")
    
    while an_inp_ent == False:
        
        valid1 = False
        entered_values1 = False
        while valid1 == False:
            team_cd = input("     Team Code:     ").upper()
            if team_cd.isalpha() and len(team_cd) == 3: 
                valid1 = True
                entered_values1 = True
                for row in players:
                    team_cd_in_players = row[3]
                    entered_values1 = True
                    if team_cd == team_cd_in_players:
                        an_inp_ent = True
                        entered_values1 = True
            elif team_cd == '':
                valid1 = True
            else:
                print('\n  Invalid input. Kindly enter an alphabet')

        valid2 = False
        entered_values2 = False
        while valid2 == False:
            pos_cd = input("     Position Code: ").upper()
            if pos_cd.isalpha() and (0<len(pos_cd) < 3): 
                valid2 = True
                entered_values2 = True
                for row in players:
                    pos_cd_in_players = row[4]
                    if pos_cd == pos_cd_in_players:
                        an_inp_ent = True
                        entered_values2 = True
            elif pos_cd == '':
                valid2 = True
            else:
                print('\n  Invalid input. Kindly enter an alphabet or the length of the Position code not right enough')
    
    
        valid3 = False
        entered_values3 = False
        while valid3 == False:
            lst_nm = input("     Last name:     ").upper()
            if lst_nm.isalpha(): 
                valid3 = True
                for row in players:
                    lst_nm_in_players = row[1].upper()
                    if lst_nm == lst_nm_in_players or lst_nm_in_players.startswith(lst_nm):
                        an_inp_ent = True
                        entered_values3 = True
                        #print('correct lst')
            elif lst_nm == '':
                valid3 = True
            else:
                print('\n  Invalid input. Kindly enter an alphabet')

        valid4 = False
        entered_values4 = False
        while valid4 == False:
            fst_nm = input("     First name:    ").upper()
            if fst_nm.isalpha(): 
                valid4 = True
                for row in players:
                    fst_nm_in_players = row[2].upper()
                    if fst_nm == fst_nm_in_players or fst_nm_in_players.startswith(fst_nm):
                        an_inp_ent = True
                        entered_values4 = True
                        #print('correct fst')
            elif fst_nm == '':
                valid4 = True
            else:
                print('\n  Invalid input. Kindly enter an alphabet')

        valid5 = False
        entered_values5 = False
        while valid5 == False:
            min_weight = input("     Weight (min):  ")
            if min_weight.isdigit():
                valid5 = True
                an_inp_ent = True
                entered_values5 = True
                min_weight = int(min_weight)
            elif min_weight == '':
                valid5 = True
            else:
                print('   invalid Max weight, Kindly enter an interger for the weight.')
            
            
        valid6 = False
        entered_values6 = False
        while valid6 == False:
            max_weight = input("     Weight (max):  ")
            if max_weight.isdigit():
                valid6 = True
                an_inp_ent = True
                entered_values6 = True
                max_weight = int(max_weight)
            elif max_weight == '':
                valid6 = True
            else:
                print('   invalid Min weight, Kindly enter an interger for the weight.')
                
            
        # condition1 = True
        # condition2 = True
        # condition3 = True
        # condition4 = True
        # condition5 = True
        # condition6 = True
        
        if  an_inp_ent == True:
            for row in players:
                emp_id_play = row[0]
                lst_nm_play = row[1].upper()
                lst_nm_play1 = row[1]
                fst_nm_play = row[2].upper()
                fst_nm_play1 = row[2]
                team_cd_play = row[3]
                pos_cd_play = row[4]
                player_num_play = row[5]
                age_play = row[6]
                weight_play = row[7]
                height_play = row[8]
                year_of_exp_play = row[9]
                college_play = row[10]
                
                
                if entered_values1 == True and team_cd == team_cd_play:
                    new_row1 = [emp_id_play, lst_nm_play, fst_nm_play, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]    
                    filtered_players1.append(new_row1)
                    #print("team_cd ", "\n", filtered_players1) 
                else:
                    pass
                
                
                if entered_values2 == True and pos_cd == pos_cd_play:
                    new_row2 = [emp_id_play, lst_nm_play, fst_nm_play, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]
                    filtered_players2.append(new_row2) 
                    #print("poc: ", "\n", filtered_players2) 
                else:
                    pass
                
                                
                if entered_values3 == True and (lst_nm == lst_nm_play or lst_nm_play.startswith(lst_nm)):
                    new_row3 = [emp_id_play, lst_nm_play1, fst_nm_play, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]
                    filtered_players3.append(new_row3)
                    #print("lst_name: ", "\n", filtered_players3) 
                else:
                    pass
                
                
                if entered_values4 == True and (fst_nm == fst_nm_play or fst_nm_play.startswith(fst_nm)):
                    new_row4 = [emp_id_play, lst_nm_play1, fst_nm_play1, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]
                    filtered_players4.append(new_row4)
                    #print("fst_nm: ", "\n", filtered_players4) 
                else:
                    pass
                
                    
                if entered_values5 == True and weight_play >= min_weight:
                    new_row5 = [emp_id_play, lst_nm_play1, fst_nm_play1, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]
                    filtered_players5.append(new_row5)
                    #print("min_weight: ", "\n", filtered_players5) 
                else:
                    pass
                
                    
                if entered_values6 == True and weight_play <= max_weight:
                    new_row6 = [emp_id_play, lst_nm_play1, fst_nm_play1, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]
                    filtered_players6.append(new_row6)
                    #print("max_weight: ", "\n", filtered_players6) 
                else:
                    pass
            
        else:        
            print("  nvalid input or the input is not located. Returning to the Main Menu.....")
            return
        
        
        
    # print("team_cd ", "\n", filtered_players1)
    # print
    # print("pos_cd ", "\n", filtered_players2)    
    # print("lst_nm: ", "\n", filtered_players3)
    # print("fst_nm: ", "\n", filtered_players4)
    # print("min_weight: ", "\n", filtered_players5)        
    # print("max_weight: ", "\n", filtered_players6)
    
    
    bool1 = False
    bool2 = False
    bool3 = False
    bool4 = False
    bool5 = False
    bool6 = False
    
    for i in range(0,len(players)):
        emp_id_play = players[i][0]
        lst_nm_play = players[i][1]
        fst_nm_play = players[i][2]
        team_cd_play = players[i][3]
        pos_cd_play = players[i][4]
        player_num_play = players[i][5]
        age_play = players[i][6]
        weight_play = players[i][7]
        height_play = players[i][8]
        year_of_exp_play = players[i][9]
        college_play = players[i][10]
        
        if filtered_players1 != []:
            for j in range(0, len(filtered_players1)):
                if players[i][3] == filtered_players1[j][3]:
                    #print("team_cd: yes")
                    bool1 = True                   
                    break
        else:
            bool1 = True
            
        if filtered_players2 != []:
            for j in range(0, len(filtered_players2)):
                if players[i][4] == filtered_players2[j][4]:
                    #print("pos_cd: yes")
                    bool2 = True
                    break
        else:
            bool2 = True
                    
        if filtered_players3 != []:
            for j in range(0, len(filtered_players3)):
                if players[i][1] == filtered_players3[j][1]:
                    #print("lst: yes")
                    bool3 = True
                    break
        else:
            bool3 = True
                    
        if filtered_players4 != []:
            for j in range(0, len(filtered_players4)):
                #print("fst: yes")
                if players[i][2] == filtered_players4[j][2]:
                    bool4 = True
                    break
        else:
            bool4 = True
                    
        if filtered_players5 != []:
            for j in range(0, len(filtered_players5)):
                if players[i][7] == filtered_players5[j][7]:
                    #print("weight_min: yes")
                    bool5 = True
                    break
        else:
            bool5 = True
                    
        if filtered_players6 != []:
            for j in range(0, len(filtered_players6)):
                if players[i][7] == filtered_players6[j][7]:
                    #print("weight_max: yes")
                    bool6 = True
                    break
        else:
            bool6 = True
                
        if bool1 == True and bool2 == True and bool3 == True and bool4 == True and bool5 == True and bool6 == True:
            new_row = [emp_id_play, lst_nm_play, fst_nm_play, team_cd_play, pos_cd_play, player_num_play, age_play, weight_play, height_play, year_of_exp_play, college_play]
            filtered_players.append(new_row)
            #print(new_row)   
            
            #print("***********************************************************************")
            #print(filtered_players)
            
        
        bool1 = False
        bool2 = False
        bool3 = False
        bool4 = False
        bool5 = False
        bool6 = False
        
        
    print()
    print("  Sort Options: ")
    print(INDENT1, "1) Name")
    print(INDENT1, "2) Team & Position")
    print(INDENT1, "3) Weight (ASC)")
    print(INDENT1, "3) Weight (DESC)")
    print()
   
    z = False
    # loop that validates input value and calls the respective function
    while z == False:
        menu_option = input('  Enter a sort option (or Press enter for none): ')
        print()
        
                
        if menu_option == '1':
            sorted_filt_players = sorted(filtered_players, key=itemgetter(1, 2))
            opt = "last name, first name"
            z = True
        elif menu_option == '2':
            sorted_filt_players = sorted(filtered_players, key=itemgetter(3, 4, 1, 2))
            opt = "team code, position code, last name, first name"
            z = True
        elif menu_option == '3':
           sorted_filt_players = sorted(filtered_players, key=itemgetter(7, 1, 2))
           opt = "weight ascending, and last name & first name"
           z = True 
        elif menu_option == '4':
            sorted_filt_players = sorted(filtered_players, key=itemgetter(7), reverse=True)
            sorted_filt_players = sorted(sorted_filt_players, key=itemgetter(1, 2))
            opt = "weight descending, and last name & first name"
            Z =  True
        elif menu_option == "":
            sorted_filt_players = filtered_players
            opt = ""
            z = True
        else:
            print(" Invalid option!!! \n  kindly select a sort option or press enter for none") 
    
    print()   
    print('>'*40, "FILTER & SORT OPTIONS", '>'*40)
    # a = '> Team', team_cd
    # b = '> Position', pos_cd
    # c = '> Last Name', lst_nm
    # d = '> First Name', fst_nm
    # e = '> Weight (min)', min_weight
    # f = '> Weight (max)', max_weight
        
    if team_cd == '':
        a = ''
    else:
        a = '> Team: ' + str(team_cd)
        
    if pos_cd == '':
        b = ''
    else:
        b = '> Position: ' + str(pos_cd)
        
    if lst_nm == '':
        c = ''
    else:
        c = '> Last Name: ' + str(lst_nm)
        
    if fst_nm == '':
        d = ''
    else:
        d = '> First Name: ' + str(fst_nm)
         
    if str(min_weight) == '':
        e = ''
    else:
        e = '> Weight (min): ' + str(min_weight)
        
    if str(max_weight) == '':
        f = ''
    else:
        f = '> Weight (max): ' + str(max_weight)
        
        
    print(' '*10,">> Filters: \t\t", a, b, c, d, e, f)
    print(' '*10,">> Sort fields: \t", opt)
    print()
    print("Met Criteria: ", len(sorted_filt_players), "players")
    print('>'*40, "FILTER & SORT OPTIONS", '>'*40)
    
    print()
    
    print(f'{"Emp ID":6} {"Last Name":17} {"First Name":14} {"Team Code":9} {"Pos Code":8} {"Player No":9} {"Age":3} {"Weight":6} {"Height":6} {"Years":5} {"College":24} ')
    print(f'{"-"*6} {"-"*17} {"-"*14} {"-"*9} {"-"*8} {"-"*9} {"-"*3} {"-"*6} {"-"*6} {"-"*5} {"-"*24} ')
    for row in sorted_filt_players:
        print(f'{row[0]:6} {row[1]:17} {row[2]:14} {row[3]:9} {row[4]:8} {row[5]:9} {row[6]:3} {row[7]:6} {row[8]:6} {row[9]:5} {row[10]:24} ')
    print()
    
    input("  ...press enter to return to the Menu")
#isfloat function -------------------------------------------------------------

# def isfloat(value):
#     try: 
#         float(value) 
#         return True
#     except: 
#         return False
main()

