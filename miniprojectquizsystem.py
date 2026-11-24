quiz_list=['Python','Java']
#Python questions
question_list=[
            'Who developed Python?',
            'Which function is used to display output in Python?',
            'Which function is used to take input from the user?',
            'What is the output of print(10 // 3)?',
            'What is the output of print(2 + 3 * 4)?',
            'Which keyword is used for conditional statements?',
            'Which loop is best when the number of iterations is known?',
            'Which statement immediately exits a loop?',
            'Which operator is used to find the remainder?',
            'Which of the following is a valid variable name?',
            'What is the output of x = "10"; print(int(x) + 5)?',
            'Which function returns the length of a string?',
            'What is the output of print("Python"[1])?',
            'Which method adds an element to the end of a list?',
            'What is the output of numbers = [5, 10, 15]; print(numbers[-1])?',
            'Which condition correctly checks whether a number is even?',
            'What is the output of for i in range(1, 4): print(i)?',
            'What is the output of total = 0; for i in range(1, 6): total += i; print(total)?',
            'Which keyword is used to define a function?',
            'What is the output of def square(n): return n * n; print(square(4))?'
  ]
optionA = ['James Gosling','display()','read()','3.33','20','when','while','continue','/','2value','105','size()','P','add()','5','n / 2 == 0','0 1 2','10','function','8']
optionB = ['Guido van Rossum','print()','scan()','3','14','if','for','break','//','my-name','15','count()','y','append()','10','n % 2 == 0','1 2 3','15','define','16']
optionC = ['Dennis Ritchie','output()','input()','1','24','switch','do-while','pass','%','my_value','Error','len()','t','insert()','15','n // 2 == 0','1 2 3 4','20','def','4']
optionD = ['Bjarne Stroustrup','show()','get()','4','18','case','repeat','exit','**','class','10','length()','h','push()','Error','n == 2','Error','21','fun','Error']
#java questions
questions1 = [
            'Java is primarily a ______ programming language.',
            'Which command is used to compile a Java program?',
            'Which command is used to execute a Java program?',
            'Which of the following is the correct extension for a Java source file?',
            'Which symbol is used to terminate a statement in Java?',
            'Which keyword is used to declare a constant variable?',
            'Which package contains the Scanner class?',
            'Which method is used to read a String using Scanner?',
            'Which data type stores true or false values?',
            'Which operator is used for logical AND?',
            'What is the output?\nint x = 5;\nSystem.out.println(x++);',
            'What is the output?\nint x = 5;\nSystem.out.println(++x);',
            'What is the output?\nSystem.out.println(10 % 3);',
            'What is the output?\nSystem.out.println(10 / 4);',
            'What is the output?\nSystem.out.println(3 + 4 * 2);',
            'What is the output?\nint a = 8;\nSystem.out.println(a > 5);',
            'What is the output?\nint a = 10;\nif(a > 5)\nSystem.out.println("Yes");',
            'How many times will the loop execute?\nfor(int i=1;i<=5;i++)',
            'What is the output?\nint sum=0;\nfor(int i=1;i<=3;i++) sum+=i;\nSystem.out.println(sum);',
            'What is the output?\nSystem.out.println(15 / 2);'
  ]
optiona = ['Compiled','java','javac','.class','.','const','java.io','nextInt()','int','&','5','5','3','2.5','14','true','Yes','4','3','7.5']
optionb = ['Interpreted','javac','java','.java',':','fixed','java.util','next()','char','&&','6','6','1','2','11','false','No','5','6','7']
optionc = ['Platform Independent','compile','run','.jar',';','final','java.lang','nextDouble()','boolean','||','4','4','0','3','10','8','Error','6','9','8']
optiond = ['Assembly','jdk','execute','.exe',',','static','java.net','read()','String','!','Error','Error','10','2.0','8','Error','Nothing','Infinite','10','15']

score_list=[]
domain=[]
names=[]
print('*'*10,"Vcube Quiz Management System",'*'*10)
print("Welcome,to Vcube Quiz")
print("1.Admin")
print("2.Student")
print("3.Exit")
choice=input("choose the one option(Admin/Student): ")
        
#Admin Section
if choice=='Admin':
       while True:
             username=input("enter username: ")
             password=input("enter password: ")
             if username=='Admin' and password=='admin123':
                    print("Login successfully in Portal")
                    while True:
                        print("1.Add Quiz")
                        print("2.Add Questions")
                        print("3.Modify Questions")
                        print("4.Delete Questions")
                        print("5.Delete Quiz")
                        print("6.View")
                        print("7.Exit")
                        while True:
                            ch=input("choose the one option: ")
                            if ch!= "":
                               break
                            print("please enter a option.")
                        if ch=='Add Quiz':
                            while True:
                                   while True:
                                       quiz_name=input("enter a quiz name: ")
                                       if quiz_name != "":
                                           break
                                       print("Please enter a quiz name.")
                                   if quiz_name in quiz_list:
                                       print("Already Existing quiz.")
                                   else:
                                       quiz_list.append(quiz_name)
                                       print('*'*5,"Quiz Domain",'*'*5)
                                       for i in range(0,len(quiz_list)):
                                           print(i+1,'.',quiz_list[i])
                                       print('-'*20)
                                       print("Successfully added in the Quiz list.")
                                       break
                        elif ch == 'Add Questions':
                                    while True:
                                        domain = input("enter a domain: ")
                                        if domain != "":
                                            break
                                        print("Please enter a domain.")

                                    while True:
                                        if domain == "python" or domain == 'Python':
                                            while True:
                                                q = input("enter a question: ")
                                                if q != "":
                                                    break
                                                print("Question cannot be empty. Please enter a question.")
                                            while True:
                                                a = input("A : ")
                                                if a != "":
                                                    break
                                                print("Option A cannot be empty. Please enter Option A.")
                                            while True:
                                                b = input("B : ")
                                                if b != "":
                                                    break
                                                print("Option B cannot be empty. Please enter Option B.")
                                            while True:
                                                c = input("C : ")
                                                if c != "":
                                                    break
                                                print("Option C cannot be empty. Please enter Option C.")
                                            while True:
                                                d = input("D : ")
                                                if d != "":
                                                    break
                                                print("Option D cannot be empty. Please enter Option D.")

                                            question_list.append(q)
                                            optionA.append(a)
                                            optionB.append(b)
                                            optionC.append(c)
                                            optionD.append(d)

                                        else:
                                            while True:
                                                q = input("enter a question: ")
                                                if q != "":
                                                    break
                                                print("Question cannot be empty. Please enter a question.")
                                            while True:
                                                a = input("A : ")
                                                if a != "":
                                                    break
                                                print("Option A cannot be empty. Please enter Option A.")
                                            while True:
                                                b = input("B : ")
                                                if b != "":
                                                    break
                                                print("Option B cannot be empty. Please enter Option B.")
                                            while True:
                                                c = input("C : ")
                                                if c != "":
                                                    break
                                                print("Option C cannot be empty. Please enter Option C.")
                                            while True:
                                                d = input("D : ")
                                                if d != "":
                                                    break
                                                print("Option D cannot be empty. Please enter Option D.")

                                            questions1.append(q)
                                            optiona.append(a)
                                            optionb.append(b)
                                            optionc.append(c)
                                            optiond.append(d)
                                        while True:
                                               complete = input("Do you want continue (yes/no): ")
                                               if complete == "yes":
                                                      break
                                               elif complete == "no":
                                                      print("Successfully added the questions and options.")
                                                      break
                                               else:
                                                    print("Please enter yes or no.")

                                        if complete == "no":
                                               break               
                        elif ch == 'Modify Questions':
                                    while True:
                                        domain = input("enter a domain: ")
                                        if domain != "":
                                            break
                                        print("Please enter a domain.")

                                    while True:

                                        if domain == 'Python' or domain == 'python':

                                            while True:
                                                i = input("enter question index number: ")
                                                if i != "":
                                                    i = int(i) - 1
                                                    if 0 <= i < len(question_list):
                                                        break
                                                    print("Invalid question index number.")
                                                else:
                                                    print("Question index number cannot be empty. Please enter a question index number.")

                                            while True:
                                                q = input("enter a question: ")
                                                if q != "":
                                                    break
                                                print("Question cannot be empty. Please enter a question.")

                                            while True:
                                                a = input("A : ")
                                                if a != "":
                                                    break
                                                print("Option A cannot be empty. Please enter Option A.")

                                            while True:
                                                b = input("B : ")
                                                if b != "":
                                                    break
                                                print("Option B cannot be empty. Please enter Option B.")

                                            while True:
                                                c = input("C : ")
                                                if c != "":
                                                    break
                                                print("Option C cannot be empty. Please enter Option C.")

                                            while True:
                                                d = input("D : ")
                                                if d != "":
                                                    break
                                                print("Option D cannot be empty. Please enter Option D.")

                                            question_list.pop(i)
                                            question_list.insert(i, q)

                                            optionA.pop(i)
                                            optionA.insert(i, a)

                                            optionB.pop(i)
                                            optionB.insert(i, b)

                                            optionC.pop(i)
                                            optionC.insert(i, c)

                                            optionD.pop(i)
                                            optionD.insert(i, d)

                                            print(question_list)

                                        else:

                                            while True:
                                                i = input("enter question index number: ")
                                                if i != "":
                                                    i = int(i) - 1
                                                    if 0 <= i < len(questions1):
                                                        break
                                                    print("Invalid question index number.")
                                                else:
                                                    print("Question index number cannot be empty. Please enter a question index number.")

                                            while True:
                                                q = input("enter a question: ")
                                                if q != "":
                                                    break
                                                print("Question cannot be empty. Please enter a question.")

                                            while True:
                                                a = input("A : ")
                                                if a != "":
                                                    break
                                                print("Option A cannot be empty. Please enter Option A.")

                                            while True:
                                                b = input("B : ")
                                                if b != "":
                                                    break
                                                print("Option B cannot be empty. Please enter Option B.")

                                            while True:
                                                c = input("C : ")
                                                if c != "":
                                                    break
                                                print("Option C cannot be empty. Please enter Option C.")

                                            while True:
                                                d = input("D : ")
                                                if d != "":
                                                    break
                                                print("Option D cannot be empty. Please enter Option D.")

                                            questions1.pop(i)
                                            questions1.insert(i, q)

                                            optiona.pop(i)
                                            optiona.insert(i, a)

                                            optionb.pop(i)
                                            optionb.insert(i, b)

                                            optionc.pop(i)
                                            optionc.insert(i, c)

                                            optiond.pop(i)
                                            optiond.insert(i, d)

                                            print(questions1)

                                        while True:
                                               complete = input("Do you want continue (yes/no): ")
                                               if complete == "yes":
                                                   break
                                               elif complete == "no":
                                                   print("Successfully Modify the questions and options.")
                                                   break
                                               else:
                                                   print("Please enter yes or no.")
                                        if complete == "no":
                                               break
                                                 
                        elif ch == 'Delete Questions':

                                     while True:
                                               domain = input("enter a domain: ")
                                               if domain != "":
                                                   break
                                               print("Please enter a domain.")
                                     while True:

                                           if domain == "Python" or domain == "python":

                                               while True:
                                                   delete_index = input("enter a question index number: ")

                                                   if delete_index != "":
                                                       delete_index = int(delete_index)

                                                       if 1 <= delete_index <= len(question_list):
                                                           delete_index -= 1
                                                           break
                                                       else:
                                                           print("Invalid question index number.")
                                                   else:
                                                       print("Question index number cannot be empty.")

                                               del question_list[delete_index]
                                               del optionA[delete_index]
                                               del optionB[delete_index]
                                               del optionC[delete_index]
                                               del optionD[delete_index]

                                               print("Question deleted successfully.")

                                           elif domain == "Java" or domain == "java":

                                               while True:
                                                   delete_index = input("enter a question index number: ")

                                                   if delete_index != "":
                                                       delete_index = int(delete_index)

                                                       if 1 <= delete_index <= len(questions1):
                                                           delete_index -= 1
                                                           break
                                                       else:
                                                           print("Invalid question index number.")
                                                   else:
                                                       print("Question index number cannot be empty.")

                                               del questions1[delete_index]
                                               del optiona[delete_index]
                                               del optionb[delete_index]
                                               del optionc[delete_index]
                                               del optiond[delete_index]

                                               print("Question deleted successfully.")

                                           else:
                                               print("Invalid domain.")

                                           while True:
                                               complete = input("Do you want continue (yes/no): ")
                                               if complete == "yes":
                                                   break
                                               elif complete == "no":
                                                   print("Successfully deleted the questions and options.")
                                                   break
                                               else:
                                                   print("Please enter yes or no.")

                                           if complete == "no":
                                               break
                        elif ch == 'Delete Quiz':
                                while True:
                                    domain = input("Enter a domain: ").strip()
                                    if domain != "":
                                        break
                                    print("Please enter a domain.")

                                if domain in quiz_list:
                                    quiz_list.remove(domain)
                                    print("Quiz deleted successfully.")
                                else:
                                    print("Quiz is not found.")

                                print(quiz_list)
                                                           
                        elif ch=='View':
                              while True:
                                  domain=input("enter a domain: ")
                                  if domain!="":
                                        break
                                  print("Please enter a domain")
                              if domain=='Python' or domain=='python':
                                 n=1
                                 print('-'*25,domain,"Quiz",'-'*25)
                                 for q in range(0,len(question_list)):
                                        print("Question",n,'.',question_list[q])
                                        print("A.",optionA[q])
                                        print("B.",optionB[q])
                                        print("C.",optionC[q])
                                        print("D.",optionD[q])
                                        n=n+1
                                 print('-'*50)
                              else:
                                 n=1
                                 print('-'*25,domain,"Quiz",'-'*25)
                                 for q in range(0,len(questions1)):
                                        print("Question",n,'.',questions1[q])
                                        print("A.",optiona[q])
                                        print("B.",optionb[q])
                                        print("C.",optionc[q])
                                        print("D.",optiond[q])
                                        n=n+1
                                 print('-'*50)
                        elif ch=='Exit':
                              print("Thank you")
                              break
                    break
             else:
                   print("Invalid username and password")

#Student section
elif choice=='Student':
       while True:
             username=input("enter username: ")
             password=input("enter password: ")
             if username=='vinay' and password=='std123':
                     print("Login successfully in Portal")
                     while True:
                          print("1.View Available Quizzes")
                          print("2.Start Quiz")
                          print("3.view Score")
                          print("4.Exit")
                          while True:
                              chs=input("enter a option: ")
                              if chs != "":
                                  break
                              print("Please enter a option.")
                          if chs=='View Available Quizzes':
                              print('-'*5,"Quiz Domains",'-'*5)
                              for i in quiz_list:
                                     print("*",i)
                              print()
                          elif chs=='Start Quiz':
                              while True:
                                   name=input("enter your name please: ")
                                   if name != "":
                                       break
                                   print("Please enter your name.")
                              while True:
                                   choose=input("choose the one domain: ")
                                   if choose != "":
                                       break
                                   print("Please enter a domain.")
                              while True:
                                   if choose=='Python' or choose=='python':
                                           while True:
                                                  ch = input("Do you want continue (yes/no): ")
                                                  if ch == "yes":
                                                           break
                                                  elif ch == "no":
                                                           break
                                                  else:
                                                      print("Please enter yes or no.")
                                          
                                           if 'yes'==ch:
                                                score=0
                                                for i in quiz_list:
                                                      if choose==i:
                                                          print()
                                                          print('-'*25,choose,"Quiz",'-'*25)
                                                          print()
                                                answers = ['B','B','C','B','B','B','B','B','C','C','B','C','B','B','C','B','B','B','C','B']
                                                n=1
                                                for q in range(0,len(question_list)):
                                                         print("Question",n,'.',question_list[q])
                                                         print("A.",optionA[q])
                                                         print("B.",optionB[q])
                                                         print("C.",optionC[q])
                                                         print("D.",optionD[q])
                                                         while True:
                                                                ans=input("Answer: ")
                                                                if ans!='':
                                                                       break
                                                                print('Please enter answer')
                                                         for a in range(0,len(answers)):
                                                              if ans==answers[q]:
                                                                   print("correct")
                                                                   score+=1
                                                                   break
                                                              else:
                                                                  print("Wrong Answer")
                                                                  break
                                                         n=n+1
                                                names.append(name)
                                                domain.append(choose)
                                                score_list.append(score)
                                                while True:
                                                        subt = input("Enter submit: ").lower()
                                                        if subt == "":
                                                               print("Please enter submit.")
                                                        elif subt == "submit":
                                                               print("Successfully submitted")
                                                               break
                                                        else:
                                                             print("Please enter only 'submit'.")
                                           else:
                                              print("No worries! Maybe next time.")
                                              break
                                                
                                   elif choose=='Java' or choose=='java':
                                           while True:
                                                  ch = input("Do you want continue (yes/no): ")
                                                  if ch == "yes":
                                                           break
                                                  elif ch == "no":
                                                           break
                                                  else:
                                                      print("Please enter yes or no.")

                                           if 'yes'==ch:
                                                    score=0
                                                    for i in quiz_list:
                                                          if choose==i:
                                                              print()
                                                              print('-'*25,choose,"Quiz",'-'*25)
                                                              print()
                                                    answers = ['C','B','B','B','C','C','B','B','C','B','A','B','B','B','B','A','A','B','B','B']
                                                    n=1
                                                    for q in range(0,len(questions1)):
                                                             print("Question",n,'.',questions1[q])
                                                             print("A.",optiona[q])
                                                             print("B.",optionb[q])
                                                             print("C.",optionc[q])
                                                             print("D.",optiond[q])
                                                             while True:
                                                                ans=input("Answer: ")
                                                                if ans!='':
                                                                       break
                                                                print('Please enter answer')
                                                             for a in range(0,len(answers)):
                                                                  if ans==answers[q]:
                                                                       print("correct")
                                                                       score+=1
                                                                       break
                                                                  else:
                                                                      print("Wrong Answer")
                                                                      break
                                                             n=n+1
                                                    names.append(name)
                                                    domain.append(choose)
                                                    score_list.append(score)
                                                    while True:
                                                           subt = input("Enter submit: ").lower()

                                                           if subt == "":
                                                                  print("Please enter submit.")
                                                           elif subt == "submit":
                                                                  print("Successfully submitted")
                                                                  break
                                                           else:
                                                                print("Please enter only 'submit'.")
                                                                
                                           else:
                                                 print("No worries! Maybe next time.")
                                                 break
                          elif chs=='view Score':
                                     total=20
                                     print('*'*20,"View Score",'*'*20)
                                     print(f'{'Name':<10}{'Domain':<10}{'Score':<10}{'Percentage':<10}')
                                     print('-'*40)
                                     for d in zip(names,domain,score_list):
                                             percentage=(sum(score_list)/total)*100
                                             print(f'{d[0]: <10}{d[1]: <10}{str(d[2])+'/20':<10}{percentage:>5.0f}%')
                                     print('-'*40)   
                          elif chs=='Exit':
                                     print("Thanks for Participating...!")
                                     break
                                   
else:
     print('Exiting...Have a great day')
                     
                            
