from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomMessageDialog(QDialog):
    def __init__(self, message, title):
        super().__init__()
        self.message = message
        self.title = title
        self.setWindowTitle(self.title)
        button = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(button)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        content = QLabel(f"{self.message}")
        self.layout.addWidget(content)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)