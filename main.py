

import datetime
import logging


# -------------------------------
# Logging Configuration
# -------------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------------
# Greeting Class
# -------------------------------
class HelloWorldApp:
    def __init__(self, user_name="Guest"):
        self.user_name = user_name
        logging.info("Application initialized for user: %s", user_name)

    def get_time_based_greeting(self):
        """Return greeting based on current time"""
        current_hour = datetime.datetime.now().hour

        if 0 <= current_hour < 12:
            return "Good Morning"
        elif 12 <= current_hour < 18:
            return "Good Afternoon"
        else:
            return "Good Evening"

    def display_welcome(self):
        """Display welcome message"""
        greeting = self.get_time_based_greeting()
        message = f"{greeting}, {self.user_name}! Welcome to the Hello World App."
        print(message)
        logging.info("Displayed welcome message")

    def display_menu(self):
        """Show menu options"""
        print("\nChoose a greeting style:")
        print("1. Simple Hello")
        print("2. Enthusiastic Hello")
        print("3. Formal Hello")
        print("4. Exit")

    def process_choice(self, choice):
        """Process user choice"""
        if choice == "1":
            print(f"Hello, {self.user_name}!")
        elif choice == "2":
            print(f"HELLOOOO {self.user_name}!!! 🎉🔥")
        elif choice == "3":
            print(f"Greetings, {self.user_name}. It is a pleasure to meet you.")
        elif choice == "4":
            print("Exiting application. Goodbye!")
            logging.info("Application exited by user")
            return False
        else:
            print("Invalid choice. Please try again.")
            logging.warning("Invalid menu choice entered")

        return True


# -------------------------------
# Utility Function
# -------------------------------
def get_user_name():
    """Get user name from input"""
    name = input("Enter your name: ").strip()
    if not name:
        name = "Guest"
    return name


# -------------------------------
# Main Function
# -------------------------------
def main():
    print("===== Hello World Application =====")

    name = get_user_name()
    app = HelloWorldApp(name)

    app.display_welcome()

    running = True
    while running:
        app.display_menu()
        choice = input("Enter your choice: ")
        running = app.process_choice(choice)


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print("Something went wrong. Please check logs.")
