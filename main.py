from helper.quiz import Quiz
from helper.user import login_user, register_user, check_user_exists

dsa_quiz = Quiz("dsa")
dbms_quiz = Quiz("dbms")
os_quiz = Quiz("os")

users = {}

logged: bool = False
logged_user = None

def main():
    global logged, logged_user, users
    
    if not logged:
        
        print("Welcome to the Quiz App!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            res =  login_user(username, password, users)
            
            if res:
                print("Login Successful!")
                logged = True
                logged_user = res
            else:
                print("Invalid Credentials!")
        
        elif choice == "2":
            username = input("Enter your username: ")
            
            if users and check_user_exists(username, users):
                print("=====================================")
                print("Username already exists!")
                print("=====================================")
                return
            
            email = input("Enter your email: ")         
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            
            res =  register_user(username, password, name, email, users)
                
            if res:
                print("Registration Successful!")
                logged = True
                logged_user = res[0]
                users = res[1]
            else:
                print("Registration Failed!")
        
        elif choice == "3":
            exit()
        else:
            print("Invalid Choice!")
            
    else:
        print("=====================================")
        print("Main Menu")
        print(f"Welcome {logged_user.get('name')}!")
        print("1. Start Quiz")
        print("2. Logout")
        print("=====================================")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Choose a quiz to start:")
            print("1. Data Structures and Algorithms")
            print("2. Database Management System")
            print("3. Operating System")
            
            quiz_choice = input("Enter your choice: ")
            
            if quiz_choice == "1":
                print("Starting Data Structures and Algorithms Quiz!")
                
                dsa_quiz.start_quiz()
            elif quiz_choice == "2":
                print("Starting Database Management System Quiz!")
                
                dbms_quiz.start_quiz()
            elif quiz_choice == "3":
                print("Starting Operating System Quiz!")
                
                os_quiz.start_quiz()
            else:
                print("Invalid Choice!")
        elif choice == "2":
            logged = False
            logged_user = None
        elif choice == "3":
            exit()
        else:
            print("Invalid Choice!")
        
            
if __name__ == "__main__":
    
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Choose 3 to exit")