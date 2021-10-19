ik = ""
pronounce = ""
gender = ""
year = 0
month = 0
day = 0


def check_input():

    ik = input("Enter isikukood: ")
    if len(ik) == 11 and ik.isdigit() == True: 
        print("Format OK")
        ik_list = list(ik)
        return ik_list
    else:
        print("Wrong data format")
        return False

def check_gender(ik_list):
    
    print("First symbol: ")        
    print("Gender: ",end="")
    gender = int(ik_list[0])
    if gender not in range(1,7):
        print(ik_list[0], "- Wrong gender type!")
        return False
        
    else:
        print(ik_list[0], "- OK")
        if gender // 2 == 0:
            return "women"
        else:
            return "men"
def birth_day(ik_list):
    print("Date of birth: ",end="")
    if int(ik_list[0]) in [3,4]:
        y_pref = 1900
    elif int(ik_list[0]) in [5,6]:
        y_pref = 2000
    year = y_pref + int(ik_list[1] + ik_list[2])
    month = int(ik_list[3] + ik_list[4])
    day = int(ik_list[5] + ik_list[6])

    if month in range(1,13) and day in range(1,32):
        print(f"{day}.{month}.{year} - OK")
        b_list = [day,month,year]
        return b_list
    else:
        print(f"{day}.{month}.{year} - Wrong data detected")
        return False

def clinic(id):

    c_id = int(id[7] + id[8] + id[9])
    if c_id >= 1 and c_id <=10: return  "Kuressaare Haigla"
    elif c_id >= 11 and c_id <=19: return  "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif c_id >= 21 and c_id <=220: return "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif c_id >= 221 and c_id <=270: return "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif c_id >= 271 and c_id <=370: return "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif c_id >= 371 and c_id <=420: return "Narva Haigla"
    elif c_id >= 421 and c_id <=470: return "Pärnu Haigla"
    elif c_id >= 471 and c_id <=490: return "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif c_id >= 491 and c_id <=520: return "Järvamaa Haigla (Paide)"
    elif c_id >= 521 and c_id <=570: return "Rakvere, Tapa haigla"
    elif c_id >= 571 and c_id <=600: return "Valga Haigla"
    elif c_id >= 601 and c_id <=650: return "Viljandi Haigla"
    elif c_id >= 651 and c_id <=700: return "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else: return "None"

def controll_num_check(id):
    print(id)
    first_level_list = [1,2,3,4,5,6,7,8,9,1]
    second_level_list = [3,4,5,6,7,8,9,1,2,3]
    check_sum = 0
    c_num = 0

    for i in range(10):
        check_sum += first_level_list[i] * int(id[i])
    
    jaak = check_sum // 11

    if jaak == 10:
        check_sum = 0
        for i in range(10):
            check_sum += second_level_list[i] * int(id[i])
            jaak = check_sum // 11 
         
        if jaak == 10:
            c_num = 0
            
        else:
            c_num = check_sum - jaak * 11        
    else:
        c_num = check_sum - jaak * 11
        

    print("Control number is ", c_num)
    if c_num == int(id[10]):
        print("Control number matched")
        return True
    else:
        print("Control number does NOT matched")
        return False



def main():
    while True:
        while True:
            ik_list = check_input()
            if ik_list == False: break

            print("Isikukood analys:".center(50,'-'))

            gender = check_gender(ik_list)
            if gender == False: break
            elif gender == "men":
                pronounce = "his"
            else:
                pronounce = "her"

            birth_day_list = birth_day(ik_list)
            if birth_day_list == False: break

            if controll_num_check(ik_list) == False: break
            
            print()
            print(f"It is a {gender}. {pronounce.title()} date of birth is {birth_day_list[0]}.{birth_day_list[1]}.{birth_day_list[2]} and if this code was given before 2013, {pronounce} place of birth is: {clinic(ik_list)}")
    

if __name__ == "__main__":
    main()