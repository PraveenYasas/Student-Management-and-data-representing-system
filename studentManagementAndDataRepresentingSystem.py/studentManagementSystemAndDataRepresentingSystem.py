print("Are you Student? please enter 's', Are you Staff? please enter 't'.")
version = input("Student version for 's' and Staff version for 't': ")
if version == "t":
    from graphics import *

    count_progress = 0
    count_trailer = 0
    count_exclude = 0
    count_retriver = 0

    progression_data = []

    document = open("coursework scoring.txt","w")
    document.close
    
    score = [0,20,40,60,80,100,120]

    while True:
        try:
            pass_credits = int(input("Enter your total PASS credits: "))
            if pass_credits not in score:
                print("Out of range")
                continue
            defer_credits = int(input("Enter your total DEFER credits: "))
            if defer_credits not in score:
                print("Out of range")
                continue
            fail_credits = int(input("Enter your total FAIL credits: "))
            if fail_credits not in score:
                print("Out of range")
                continue
        except ValueError:
            print("Integer required")
            continue
        except:
            continue
    
        if (pass_credits + defer_credits + fail_credits) == 120:
            if pass_credits == 120:
                print("progress")
                outcome = "progress"
                count_progress += 1
            elif  (pass_credits == 100 and defer_credits == 20) or (pass_credits == 100 and fail_credits == 20):
                print("Progress (module trailer)")
                outcome = "Progress (module trailer)"
                count_trailer += 1        
            elif fail_credits >= 80:
                print("exclude")
                outcome = "exclude"
                count_exclude += 1
            else:
                print("Do not progress - module retriever")
                outcome = "Do not progress - module retriever"
                count_retriver += 1
        else:
            print("Tatal incorrect")
            continue

        progression_data.append([outcome, pass_credits, defer_credits, fail_credits])
          
        print("Would you like to enter another set of data?")
        your_choice = input("Enter 'y' for yes or 'q' to quit and view results ")
        
        if your_choice == "q":
            break
        else:
            your_choice == "y"
            continue
        
    total = count_progress + count_trailer + count_exclude + count_retriver
    size = 25


    win = GraphWin("Histrogram", 650, 575)
    win.setBackground("white")
    
    
    topic = Text(Point(150,30), "Hisrogram Results")
    topic.setTextColor("Gray")
    topic.setSize(18)
    topic.setStyle("bold")
    topic.draw(win)
    
    start_point = Point(50, 450)
    end_point = Point(600, 450)
    horizontal_line = Line(start_point, end_point)
    horizontal_line.setOutline("black")
    horizontal_line.draw(win)
    
    colloum_1 = Rectangle(Point(70, 450),Point(190, (450 - count_progress * size)))
    colloum_1.setFill("palegreen")
    colloum_1.draw(win)
    colloum_1_name = Text(Point(130 , (450 + 25)), "Progress")
    colloum_1_name.setTextColor("Gray")
    colloum_1_name.setStyle("bold")
    colloum_1_name.draw(win)
    colloum_1_score = Text(Point(130, (450 - 25) - count_progress * size), count_progress)
    colloum_1_score.setTextColor("Gray")
    colloum_1_score.setStyle("bold")
    colloum_1_score.draw(win)
       
    colloum_2 = Rectangle(Point(200, 450), Point(320, (450 - count_trailer * size)))
    colloum_2.setFill("darkseagreen")
    colloum_2.draw(win)
    colloum_2_name = Text(Point(260, (450 + 25)), "Trailer")
    colloum_2_name.setTextColor("Gray")
    colloum_2_name.setStyle("bold")
    colloum_2_name.draw(win)
    colloum_2_score = Text(Point(260, (450 - 25) - count_trailer * size), count_trailer)
    colloum_2_score.setTextColor("Gray")
    colloum_2_score.setStyle("bold")
    colloum_2_score.draw(win)

    colloum_3 = Rectangle(Point(330 , 450), Point(450, (450 - count_retriver * size)))
    colloum_3.setFill("yellowgreen")
    colloum_3.draw(win)
    colloum_3_name = Text(Point(390, (450  + 25)), "Retriever")
    colloum_3_name.setTextColor("Gray")
    colloum_3_name.setStyle("bold")
    colloum_3_name.draw(win)
    colloum_3_score = Text(Point(390, (450 - 25) - count_retriver * size), count_retriver)
    colloum_3_score.setTextColor("Gray")
    colloum_3_score.setStyle("bold")
    colloum_3_score.draw(win)

    colloum_4 = Rectangle(Point(460, 450), Point(580, (450 - count_exclude * size)))
    colloum_4.setFill("lightpink")
    colloum_4.draw(win)
    colloum_4_name = Text(Point(520, (450 + 25)), "Exclude")
    colloum_4_name.setTextColor("Gray")
    colloum_4_name.setStyle("bold")
    colloum_4_name.draw(win)
    colloum_4_score = Text(Point(520, (450 - 25) - count_exclude * size), count_exclude)
    colloum_4_score.setTextColor("Gray")
    colloum_4_score.setStyle("bold")
    colloum_4_score.draw(win)

    results = Text(Point(200, 525),f"{total} outcomes in total.")
    results.setSize(18)
    results.setTextColor("Gray")
    results.setStyle("bold")
    results.draw(win)

    win.getMouse() # pause for click in window
    win.close()

    print(" ")
    print("Part 2:")
    for i in progression_data:
        print(f"{i[0]} - {i[1]} , {i[2]} , {i[3]}")

    print(" ")
    print("Part 3:")
    with open ("coursework scoring.txt","a") as document:
        for i in progression_data:
            document.write(f"{i[0]} - {i[1]}, {i[2]}, {i[3]}\n")

    with open ("coursework scoring.txt","r") as document:
        x = document.read()
        print(x)

elif version == "s":
    while True:
        try:
            score = [0,20,40,60,80,100,120]
            
            pass_credits = int(input("Enter your total PASS credits: "))
            if pass_credits not in score:
                print("Out of range")
                continue
            defer_credits = int(input("Enter your total DEFER credits: "))
            if defer_credits not in score:
                print("Out of range")
                continue
            fail_credits = int(input("Enter your total FAIL credits: "))
            if fail_credits not in score:
                print("Out of range")
                continue
        except ValueError:
            print("Integer required")
            continue
        except:
            continue
        
        if (pass_credits + defer_credits + fail_credits) == 120:
            if pass_credits == 120:
                print("progress")
            elif  (pass_credits == 100 and defer_credits == 20) or (pass_credits == 100 and fail_credits == 20):
                print("Progress (module trailer)")        
            elif fail_credits >= 80:
                print("exclude")
            else:
                print("Do not progress - module retriever")
            break

else:
    print("Please enter Staff for letter 't' or Student for letter 's'.")
