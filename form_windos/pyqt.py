import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, \
    QSpacerItem, QMessageBox, QScrollArea, QTextEdit
from PyQt5.QtCore import Qt, QTimer
# from cracker_wallet.wallet_generator import main_generator_wallet
import string



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-window Application")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        main_layout = QHBoxLayout()

        # Create a widget for the left section (buttons) with a gray background
        left_widget = QWidget()
        left_widget.setStyleSheet("background-color: gray;")
        left_widget.setFixedWidth(128)  # Set the fixed width to 16% of 800px (the total width)
        left_layout = QVBoxLayout()

        # Create a spacer item to push buttons down
        left_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create buttons for navigation
        self.button1 = self.create_button("Hunter")
        self.button2 = self.create_button("Withdraw")
        self.button3 = self.create_button("Contact us")
        self.button4 = self.create_button("Guide")

        # Connect buttons to their respective functions
        self.button1.clicked.connect(lambda: self.switch_page(0))
        self.button2.clicked.connect(self.open_withdraw_window)  # Connect Withdraw button to new function
        self.button3.clicked.connect(self.contact_us_window)
        self.button4.clicked.connect(self.open_guide_window)

        # Add buttons to the left layout with spacing
        left_layout.addWidget(self.button1)
        left_layout.addSpacing(10)  # Add spacing between buttons
        left_layout.addWidget(self.button2)
        left_layout.addSpacing(10)  # Add spacing between buttons
        left_layout.addWidget(self.button3)
        left_layout.addSpacing(10)  # Add spacing between buttons
        left_layout.addWidget(self.button4)

        # Add another spacer to keep the buttons from the bottom
        left_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Set the layout for the left widget
        left_widget.setLayout(left_layout)

        # Create a widget for the right section
        right_widget = QWidget()
        right_layout = QVBoxLayout()

        # Create two sections with different background colors and sizes
        blue_top_section = self.create_colored_section_with_balance("blue", "", 1, "BTC",
                                                                    0)
        self.black_mid_section = self.create_colored_section("black", "This is the green section (text from server)", 7)

        # Add the colored sections to the right layout
        right_layout.addWidget(blue_top_section)
        right_layout.addWidget(self.black_mid_section)

        # Create buttons
        start_button = self.create_button("Start")
        start_button.setStyleSheet("background-color: green; color: white; font-size: 18px; border-radius: 10px;")
        stop_button = self.create_button("Stop")
        stop_button.setStyleSheet("background-color: red; color: white; font-size: 18px; border-radius: 10px;")

        # Set size policy for the buttons
        start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Connect start and stop buttons to their respective functions
        start_button.clicked.connect(self.start_generating_numbers)
        stop_button.clicked.connect(self.stop_generating_numbers)

        # Create a horizontal layout for the buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(start_button)
        buttons_layout.addWidget(stop_button)
        buttons_layout.setAlignment(Qt.AlignCenter)

        # Add buttons layout to the right layout
        right_layout.addLayout(buttons_layout)

        # Set the layout for the right widget
        right_widget.setLayout(right_layout)

        # Add the left and right widgets to the main layout
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)

        # Set the main layout for the window
        self.setLayout(main_layout)

        # Timer for generating random numbers
        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_random_number)

    def create_button(self, text):
        """Create a button with specified text, size, and color."""
        button = QPushButton(text)
        button.setMinimumSize(80, 60)
        return button

    def create_colored_section(self, color, text, proportion):
        """Create a section with a specified background color, proportion, and optional buttons."""
        section = QWidget()
        section.setStyleSheet(f"background-color: {color};")
        layout = QVBoxLayout()

        if color == "green":
            label = QLabel(text)
            label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            label.setStyleSheet("color: white; font-size: 18px; margin: 10px;")
            layout.addWidget(label)
        else:
            # Add a scroll area for the black section to display random numbers
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            self.scroll_content = QWidget()
            self.scroll_layout = QVBoxLayout()
            self.scroll_content.setLayout(self.scroll_layout)
            scroll_area.setWidget(self.scroll_content)

            layout.addWidget(scroll_area)

        section.setLayout(layout)
        section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        section.setFixedHeight(proportion * 60)  # 600px total height divided by 10 parts
        return section

    def create_colored_section_with_balance(self, color, text, proportion, currency, balance):
        """Create a section with a specified background color, proportion, and balance text."""
        section = QWidget()
        section.setStyleSheet(f"background-color: {color};")
        layout = QVBoxLayout()

        # Create a QHBoxLayout to arrange the label and balance text horizontally
        balance_layout = QHBoxLayout()

        # Create label for "Balance:"
        balance_label = QLabel("Balance:")
        balance_label.setStyleSheet("color: white; font-size: 18px;")
        balance_layout.addWidget(balance_label)

        # Create label for balance value
        balance_value_label = QLabel(f"{balance} {currency}")
        balance_value_label.setStyleSheet("color: white; font-size: 18px;")
        balance_layout.addWidget(balance_value_label)

        # Add balance layout to main layout
        layout.addLayout(balance_layout)

        if color == "green":
            label = QLabel(text)
            label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            label.setStyleSheet("color: white; font-size: 18px; margin: 10px;")
            layout.addWidget(label)
        else:
            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("color: white; font-size: 18px;")
            layout.addWidget(label)

        section.setLayout(layout)
        section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        section.setFixedHeight(proportion * 60)  # 600px total height divided by 10 parts
        return section

    def contact_us_window(self):
        contact_us_window = QMessageBox()
        contact_us_window.setWindowTitle("Contact Us ")
        contact_us_window.setText("WalletHunter@gamil.com")
        contact_us_window.exec()

    def open_withdraw_window(self):
        """Open a new window to display withdrawal message."""
        withdraw_window = QMessageBox()
        withdraw_window.setWindowTitle("Withdrawal Message")
        withdraw_window.setText("You have to wait a month to withdraw your money")
        withdraw_window.exec()

    def open_guide_window(self):
        guide_window = QMessageBox()
        guide_window.setWindowTitle("Withdrawal Message")
        guide_window.setText(" تو باید صبر کنی دوست من ")
        guide_window.exec()

    def switch_page(self, index):
        """Switch to the page at the given index."""
        self.stacked_widget.setCurrentIndex(index)

    def start_generating_numbers(self):
        """Start generating random 15-digit numbers."""
        self.scroll_layout.addWidget(QLabel("Starting number generation..."))
        self.timer.start(1000)  # Generate a number every second

    def stop_generating_numbers(self):
        """Stop generating numbers and clear the section."""
        self.timer.stop()
        self.scroll_layout.addWidget(QLabel("Stopping number generation..."))
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def generate_random_number(self):
        """Generate a random 15-digit number and add it to the section."""
        prefix = random.choice(["bc1q", "bc1p", "3"])
        if prefix == "bc1q":
            initial_suffix = "bc1q"
            possible_characters = string.ascii_lowercase.replace('p', '') + '123456789'
        elif prefix == "bc1p":
            initial_suffix = "bc1p"
            possible_characters = string.ascii_lowercase + '123456789'
        elif prefix == "3":
            initial_suffix = "3"
            possible_characters = string.ascii_lowercase + '123456789'
        else:
            return None
        suffix_length = 59
        suffix = ''.join(random.choice(possible_characters) for _ in range(suffix_length))
        address = initial_suffix + suffix
        label = QLabel(address[:45] + ".........")
        label.setStyleSheet("color: white; font-size: 18px;")
        self.scroll_layout.addWidget(label)

def main_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
