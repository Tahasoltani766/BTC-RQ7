import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QSizePolicy, QSpacerItem,
                             QMessageBox, QScrollArea)
from PyQt5.QtCore import Qt, QTimer
import string
import os


# ---------------- Styles ----------------
GLOBAL_STYLE = """
QWidget {
    font-family: 'Segoe UI', 'Tahoma', sans-serif;
}
QScrollArea {
    border: none;
    background: transparent;
}
QScrollBar:vertical {
    background: #1e1e2e;
    width: 10px;
    border-radius: 5px;
}
QScrollBar::handle:vertical {
    background: #4a4a6a;
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background: #6a6a9a;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
"""

SIDEBAR_STYLE = """
QWidget#Sidebar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1a1a2e, stop:1 #16213e);
    border-right: 1px solid #2a2a4a;
}
"""

SIDEBAR_BUTTON_STYLE = """
QPushButton {
    background-color: transparent;
    color: #c8c8e0;
    font-size: 14px;
    font-weight: 500;
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 8px 10px;
    text-align: center;
}
QPushButton:hover {
    background-color: #2a2a4a;
    color: #ffffff;
    border: 1px solid #4a4a8a;
}
QPushButton:pressed {
    background-color: #3a3a6a;
}
"""

BALANCE_CARD_STYLE = """
QWidget#BalanceCard {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #2b5876, stop:1 #4e4376);
    border-radius: 16px;
    border: 1px solid #3a3a6a;
}
"""

OUTPUT_CARD_STYLE = """
QWidget#OutputCard {
    background-color: #12121f;
    border-radius: 16px;
    border: 1px solid #2a2a4a;
}
"""

START_BTN_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #11998e, stop:1 #38ef7d);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #0f8578, stop:1 #2fd46e);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #0c6d63, stop:1 #24b85d);
}
"""

STOP_BTN_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #cb2d3e, stop:1 #ef473a);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #b02434, stop:1 #d93d31);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #901d2b, stop:1 #b32e25);
}
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-window Application")
        self.setGeometry(100, 100, 900, 620)
        self.setStyleSheet(GLOBAL_STYLE)
        self.setStyleSheet(self.styleSheet() + "QWidget { background-color: #0e0e1a; }")

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------- Sidebar ----------
        left_widget = QWidget()
        left_widget.setObjectName("Sidebar")
        left_widget.setStyleSheet(SIDEBAR_STYLE)
        left_widget.setFixedWidth(160)
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(12, 20, 12, 20)
        left_layout.setSpacing(0)

        # Logo / Title
        logo = QLabel("₿ Hunter")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("color: #7ee8fa; font-size: 20px; font-weight: bold; padding: 10px;")
        left_layout.addWidget(logo)

        left_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Buttons
        self.button1 = self.create_button("🎯  Hunter")
        self.button2 = self.create_button("💸  Withdraw")
        self.button3 = self.create_button("📧  Contact us")
        self.button4 = self.create_button("📖  Guide")

        self.button1.clicked.connect(lambda: self.switch_page(0))
        self.button2.clicked.connect(self.open_withdraw_window)
        self.button3.clicked.connect(self.contact_us_window)
        self.button4.clicked.connect(self.open_guide_window)

        for btn in (self.button1, self.button2, self.button3, self.button4):
            left_layout.addWidget(btn)
            left_layout.addSpacing(8)

        left_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        left_widget.setLayout(left_layout)

        # ---------- Right content ----------
        right_widget = QWidget()
        right_widget.setStyleSheet("background-color: #0e0e1a;")
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 20, 20, 20)
        right_layout.setSpacing(16)

        # Balance card
        blue_top_section = self.create_colored_section_with_balance(
            "blue", "", 1, "BTC", self.update_balance()
        )

        # Output card
        self.black_mid_section = self.create_colored_section(
            "black", "This is the green section (text from server)", 7
        )

        right_layout.addWidget(blue_top_section)
        right_layout.addWidget(self.black_mid_section, 1)

        # Start / Stop buttons
        start_button = QPushButton("▶  Start")
        start_button.setStyleSheet(START_BTN_STYLE)
        start_button.setCursor(Qt.PointingHandCursor)
        start_button.setMinimumHeight(48)

        stop_button = QPushButton("■  Stop")
        stop_button.setStyleSheet(STOP_BTN_STYLE)
        stop_button.setCursor(Qt.PointingHandCursor)
        stop_button.setMinimumHeight(48)

        start_button.clicked.connect(self.start_generating_numbers)
        stop_button.clicked.connect(self.stop_generating_numbers)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(14)
        buttons_layout.addWidget(start_button)
        buttons_layout.addWidget(stop_button)

        right_layout.addLayout(buttons_layout)
        right_widget.setLayout(right_layout)

        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget, 1)
        self.setLayout(main_layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_random_number)

    # ---------------- Logic (unchanged) ----------------
    def update_balance(self, file_pathh='balance.txt'):
        previous_balance = 0.0
        current_balance = 0.0

        if os.path.exists(file_pathh):
            with open(file_pathh, 'r') as file:
                content = file.read().strip()
                if content:
                    previous_balance = float(content)

        random_number = random.uniform(0.0000000000001, 0.0001)
        current_balance += random_number

        total_balance = previous_balance + current_balance

        with open(file_pathh, 'w') as file:
            file.write(f'{total_balance:.20f}')

        return total_balance

    def create_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet(SIDEBAR_BUTTON_STYLE)
        button.setCursor(Qt.PointingHandCursor)
        button.setMinimumHeight(42)
        return button

    def create_colored_section(self, color, text, proportion):
        section = QWidget()
        section.setObjectName("OutputCard")
        section.setStyleSheet(OUTPUT_CARD_STYLE)
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 14, 16, 14)

        if color == "green":
            label = QLabel(text)
            label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            label.setStyleSheet("color: white; font-size: 16px;")
            layout.addWidget(label)
        else:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setStyleSheet("background: transparent; border: none;")
            self.scroll_content = QWidget()
            self.scroll_content.setStyleSheet("background: transparent;")
            self.scroll_layout = QVBoxLayout()
            self.scroll_layout.setSpacing(6)
            self.scroll_layout.setAlignment(Qt.AlignTop)
            self.scroll_content.setLayout(self.scroll_layout)
            scroll_area.setWidget(self.scroll_content)
            layout.addWidget(scroll_area)

        section.setLayout(layout)
        section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        section.setMinimumHeight(proportion * 40)
        return section

    def create_colored_section_with_balance(self, color, text, proportion, currency, balance):
        section = QWidget()
        section.setObjectName("BalanceCard")
        section.setStyleSheet(BALANCE_CARD_STYLE)
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 20, 24, 20)

        # Top small label
        title = QLabel("TOTAL BALANCE")
        title.setStyleSheet("color: #b8d4ff; font-size: 11px; font-weight: 600; letter-spacing: 2px;")
        layout.addWidget(title)

        # Balance row
        balance_layout = QHBoxLayout()
        balance_value_label = QLabel(f"{balance:.10f}")
        balance_value_label.setStyleSheet(
            "color: white; font-size: 28px; font-weight: bold;"
        )
        balance_layout.addWidget(balance_value_label)

        currency_label = QLabel(currency)
        currency_label.setStyleSheet(
            "color: #7ee8fa; font-size: 16px; font-weight: bold; padding-bottom: 4px;"
        )
        balance_layout.addWidget(currency_label, 0, Qt.AlignBottom)
        balance_layout.addStretch()
        layout.addLayout(balance_layout)

        section.setLayout(layout)
        section.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        section.setMinimumHeight(proportion * 70)
        return section

    def contact_us_window(self):
        msg = QMessageBox()
        msg.setWindowTitle("Contact Us")
        msg.setText("WalletHunter@gmail.com")
        msg.exec()

    def open_withdraw_window(self):
        msg = QMessageBox()
        msg.setWindowTitle("Withdrawal Message")
        msg.setText("You have to wait a month to withdraw your money")
        msg.exec()

    def open_guide_window(self):
        msg = QMessageBox()
        msg.setWindowTitle("Guide")
        msg.setText(" تو باید صبر کنی دوست من ")
        msg.exec()

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

    def start_generating_numbers(self):
        self.scroll_layout.addWidget(self._make_log_label("▶ Starting number generation..."))
        self.timer.start(1000)

    def stop_generating_numbers(self):
        self.timer.stop()
        self.scroll_layout.addWidget(self._make_log_label("■ Stopping number generation..."))
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def _make_log_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("color: #9aa0b5; font-size: 13px; padding: 4px;")
        return label

    def generate_random_number(self):
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

        # Nicer styled row
        row = QWidget()
        row.setStyleSheet("""
            QWidget {
                background-color: #1a1a2e;
                border-radius: 8px;
                border-left: 3px solid #38ef7d;
            }
        """)
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(10, 6, 10, 6)

        dot = QLabel("●")
        dot.setStyleSheet("color: #38ef7d; font-size: 10px;")
        row_layout.addWidget(dot)

        label = QLabel(address[:45] + "…")
        label.setStyleSheet("color: #e0e0f0; font-size: 13px; font-family: 'Consolas', monospace;")
        row_layout.addWidget(label)
        row_layout.addStretch()

        row.setLayout(row_layout)
        self.scroll_layout.addWidget(row)


def main_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main_gui()