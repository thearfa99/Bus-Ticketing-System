from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox
import sys

class BusReservationSystem:
    def __init__(self):
        self.head = None

    class Ticket:
        def __init__(self, seat, name, entry, final):
            self.seatNumber = seat
            self.passengerName = name
            self.entryDestination = entry
            self.finalDestination = final
            self.food = 0
            self.next = None

    def isSeatBooked(self, seat):
        temp = self.head
        while temp is not None:
            if temp.seatNumber == seat:
                return True
            temp = temp.next
        return False

    def bookTicket(self, seat, name, entry, final):
        if self.isSeatBooked(seat):
            return False
        newTicket = self.Ticket(seat, name, entry, final)
        if self.head is None:
            self.head = newTicket
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newTicket
        return True

    def cancelTicket(self, seat):
        if self.head is None:
            return False
        if self.head.seatNumber == seat:
            self.head = self.head.next
            return True
        prev = self.head
        curr = self.head.next
        while curr is not None and curr.seatNumber != seat:
            prev = curr
            curr = curr.next
        if curr is None:
            return False
        prev.next = curr.next
        return True

    def modifyTicket(self, seat, newName, newEntry, newFinal):
        temp = self.head
        while temp is not None:
            if temp.seatNumber == seat:
                temp.passengerName = newName
                temp.entryDestination = newEntry
                temp.finalDestination = newFinal
                return True
            temp = temp.next
        return False

    def viewTickets(self):
        tickets = []
        temp = self.head
        while temp is not None:
            tickets.append(f"Seat: {temp.seatNumber}, Passenger: {temp.passengerName}, Entry: {temp.entryDestination}, Final: {temp.finalDestination}, Food: {'Yes' if temp.food else 'No'}")
            temp = temp.next
        return tickets

    def addFood(self, seat):
        temp = self.head
        while temp is not None:
            if temp.seatNumber == seat:
                temp.food = 1
                return True
            temp = temp.next
        return False

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.busSystem = BusReservationSystem()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bus Reservation System')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        # Book Ticket
        self.bookLayout = QHBoxLayout()
        self.seatInput = QLineEdit(self)
        self.seatInput.setPlaceholderText('Seat Number')
        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText('Passenger Name')
        self.entryInput = QLineEdit(self)
        self.entryInput.setPlaceholderText('Entry Destination')
        self.finalInput = QLineEdit(self)
        self.finalInput.setPlaceholderText('Final Destination')
        self.bookButton = QPushButton('Book Ticket', self)
        self.bookButton.clicked.connect(self.bookTicket)

        self.bookLayout.addWidget(self.seatInput)
        self.bookLayout.addWidget(self.nameInput)
        self.bookLayout.addWidget(self.entryInput)
        self.bookLayout.addWidget(self.finalInput)
        self.bookLayout.addWidget(self.bookButton)
        layout.addLayout(self.bookLayout)

        # Cancel Ticket
        self.cancelLayout = QHBoxLayout()
        self.cancelSeatInput = QLineEdit(self)
        self.cancelSeatInput.setPlaceholderText('Seat Number to Cancel')
        self.cancelButton = QPushButton('Cancel Ticket', self)
        self.cancelButton.clicked.connect(self.cancelTicket)

        self.cancelLayout.addWidget(self.cancelSeatInput)
        self.cancelLayout.addWidget(self.cancelButton)
        layout.addLayout(self.cancelLayout)

        # Modify Ticket
        self.modifyLayout = QHBoxLayout()
        self.modifySeatInput = QLineEdit(self)
        self.modifySeatInput.setPlaceholderText('Seat Number to Modify')
        self.modifyNameInput = QLineEdit(self)
        self.modifyNameInput.setPlaceholderText('New Passenger Name')
        self.modifyEntryInput = QLineEdit(self)
        self.modifyEntryInput.setPlaceholderText('New Entry Destination')
        self.modifyFinalInput = QLineEdit(self)
        self.modifyFinalInput.setPlaceholderText('New Final Destination')
        self.modifyButton = QPushButton('Modify Ticket', self)
        self.modifyButton.clicked.connect(self.modifyTicket)

        self.modifyLayout.addWidget(self.modifySeatInput)
        self.modifyLayout.addWidget(self.modifyNameInput)
        self.modifyLayout.addWidget(self.modifyEntryInput)
        self.modifyLayout.addWidget(self.modifyFinalInput)
        self.modifyLayout.addWidget(self.modifyButton)
        layout.addLayout(self.modifyLayout)

        # View Tickets
        self.viewButton = QPushButton('View Booked Tickets', self)
        self.viewButton.clicked.connect(self.viewTickets)
        self.ticketsDisplay = QTextEdit(self)
        self.ticketsDisplay.setReadOnly(True)

        layout.addWidget(self.viewButton)
        layout.addWidget(self.ticketsDisplay)

        # Add Food
        self.foodLayout = QHBoxLayout()
        self.foodSeatInput = QLineEdit(self)
        self.foodSeatInput.setPlaceholderText('Seat Number for Food')
        self.foodButton = QPushButton('Add Food', self)
        self.foodButton.clicked.connect(self.addFood)

        self.foodLayout.addWidget(self.foodSeatInput)
        self.foodLayout.addWidget(self.foodButton)
        layout.addLayout(self.foodLayout)

        self.setLayout(layout)

    def bookTicket(self):
        seat = int(self.seatInput.text())
        name = self.nameInput.text()
        entry = self.entryInput.text()
        final = self.finalInput.text()
        if self.busSystem.bookTicket(seat, name, entry, final):
            QMessageBox.information(self, 'Success', 'Ticket booked successfully.')
        else:
            QMessageBox.warning(self, 'Error', 'Seat already booked.')
        self.seatInput.clear()
        self.nameInput.clear()
        self.entryInput.clear()
        self.finalInput.clear()

    def cancelTicket(self):
        seat = int(self.cancelSeatInput.text())
        if self.busSystem.cancelTicket(seat):
            QMessageBox.information(self, 'Success', 'Ticket cancelled successfully.')
        else:
            QMessageBox.warning(self, 'Error', 'Seat not found.')
        self.cancelSeatInput.clear()

    def modifyTicket(self):
        seat = int(self.modifySeatInput.text())
        newName = self.modifyNameInput.text()
        newEntry = self.modifyEntryInput.text()
        newFinal = self.modifyFinalInput.text()
        if self.busSystem.modifyTicket(seat, newName, newEntry, newFinal):
            QMessageBox.information(self, 'Success', 'Ticket modified successfully.')
        else:
            QMessageBox.warning(self, 'Error', 'Seat not found.')
        self.modifySeatInput.clear()
        self.modifyNameInput.clear()
        self.modifyEntryInput.clear()
        self.modifyFinalInput.clear()

    def viewTickets(self):
        tickets = self.busSystem.viewTickets()
        self.ticketsDisplay.clear()
        if tickets:
            self.ticketsDisplay.setPlainText('\n'.join(tickets))
        else:
            self.ticketsDisplay.setPlainText('No tickets booked yet.')

    def addFood(self):
        seat = int(self.foodSeatInput.text())
        if self.busSystem.addFood(seat):
            QMessageBox.information(self, 'Success', 'Food added to ticket.')
        else:
            QMessageBox.warning(self, 'Error', 'Seat not found.')
        self.foodSeatInput.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())