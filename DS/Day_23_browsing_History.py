class Browser:
    def __init__(self, size=5):
        # Initialize the browser with a maximum stack size for back and forward navigation
        self.size = size
        self.back_stack = []  # Stack to store the history for the "back" operation
        self.forward_stack = []  # Stack to store the history for the "forward" operation
        self.current_page = None  # To store the current page

    def visit(self, page):
        """Visits a new page."""
        if self.current_page is not None:
            self.back_stack.append(self.current_page)  # Push current page to back history before visiting a new one
            if len(self.back_stack) > self.size:
                self.back_stack.pop(0)  # Remove the oldest entry if the stack exceeds the limit
        self.current_page = page  # Set the new page as the current page
        self.forward_stack.clear()  # Clear the forward stack when a new page is visited
        print(f"Current page: {self.current_page}")

    def back(self):
        """Go back to the previous page."""
        if not self.back_stack:
            print("No more pages to go back to.")
        else:
            # Move the current page to forward_stack before going back
            self.forward_stack.append(self.current_page)
            if len(self.forward_stack) > self.size:
                self.forward_stack.pop(0)  # Maintain the forward stack size limit
            self.current_page = self.back_stack.pop()  # Pop from back stack
            print(f"Current page: {self.current_page}")

    def forward(self):
        """Go forward to the next page."""
        if not self.forward_stack:
            print("No more pages to go forward to.")
        else:
            # Move the current page to back_stack before going forward
            self.back_stack.append(self.current_page)
            if len(self.back_stack) > self.size:
                self.back_stack.pop(0)  # Maintain the back stack size limit
            self.current_page = self.forward_stack.pop()  # Pop from forward stack
            print(f"Current page: {self.current_page}")


# Instantiate the browser object
browser = Browser()

# Main loop for user interaction
while True:
    option = input("Visit a page (visit), go back (back), or forward (forward) or exit: ").strip().lower()

    if option == "visit":
        page = input("Enter page name: ").strip()
        browser.visit(page)
    elif option == "back":
        browser.back()
    elif option == "forward":
        browser.forward()
    elif option == "exit":
        print("Exiting browser navigation.")
        break
    else:
        print("Invalid input! Please try again.")
