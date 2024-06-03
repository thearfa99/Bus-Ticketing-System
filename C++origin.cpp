#include <iostream>
#include <string>

// Define the Ticket class to represent a bus ticket
class Ticket {
public:
    int seatNumber;
    std::string passengerName;
    std::string entryDestination;
    std::string finalDestination;
    int food;
    Ticket* next;

    Ticket(int seat, const std::string& name, const std::string& entry, const std::string& final)
        : seatNumber(seat), passengerName(name), entryDestination(entry), finalDestination(final), next(nullptr) {}
};

// Define the BusReservationSystem class to manage tickets using a singly linked list
class BusReservationSystem {
private:
    Ticket* head;

public:
    BusReservationSystem() : head(nullptr) {}

    // Function to book a new ticket
    void bookTicket(int seat, const std::string& name, const std::string& entry, const std::string& final) {
        Ticket* newTicket = new Ticket(seat, name, entry, final);
        if (head == nullptr) {
            head = newTicket;
        } else {
            Ticket* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newTicket;
        }
        std::cout << "Ticket booked successfully for seat " << seat << std::endl;
    }

    // Function to cancel a booked ticket
    void cancelTicket(int seat) {
        if (head == nullptr) {
            std::cout << "No tickets booked yet." << std::endl;
            return;
        }
        if (head->seatNumber == seat) {
            Ticket* temp = head;
            head = head->next;
            delete temp;
            std::cout << "Ticket for seat " << seat << " cancelled successfully." << std::endl;
            return;
        }
        Ticket* prev = head;
        Ticket* curr = head->next;
        while (curr != nullptr && curr->seatNumber != seat) {
            prev = curr;
            curr = curr->next;
        }
        if (curr == nullptr) {
            std::cout << "Ticket for seat " << seat << " not found." << std::endl;
        } else {
            prev->next = curr->next;
            delete curr;
            std::cout << "Ticket for seat " << seat << " cancelled successfully." << std::endl;
        }
    }

    // Function to display all booked tickets
    void viewTickets() {
        if (head == nullptr) {
            std::cout << "No tickets booked yet." << std::endl;
            return;
        }
        std::cout << "Booked Tickets:" << std::endl;
        Ticket* temp = head;
        while (temp != nullptr) {
            std::cout << "Seat: " << temp->seatNumber << " | Passenger: " << temp->passengerName << " | Entry: " << temp->entryDestination << " | Final: " << temp->finalDestination << std::endl;
            temp = temp->next;
        }
    }

    // Function to modify details of a booked ticket
    void modifyTicket(int seat, const std::string& newName, const std::string& newEntry, const std::string& newFinal) {
        if (head == nullptr) {
            std::cout << "No tickets booked yet." << std::endl;
            return;
        }

        Ticket* temp = head;
        while (temp != nullptr) {
            if (temp->seatNumber == seat) {
                temp->passengerName = newName;
                temp->entryDestination = newEntry;
                temp->finalDestination = newFinal;
                std::cout << "Ticket details modified for seat " << seat << std::endl;
                return;
            }
            temp = temp->next;
        }

        std::cout << "Ticket for seat " << seat << " not found." << std::endl;
    }
    void addFood(int seat){
        if (head == nullptr) {
            std::cout << "No tickets booked yet." << std::endl;
            return;
        }
        Ticket *temp = head;
        while(temp!=NULL){
            if(temp->seatNumber==seat){
                temp->food = 1;
                std::cout<<"Food has been added."<<std::endl;
                return;
            }
        }
        std::cout<<"Please enter a valid seat number."<<std::endl;
        return;
    }
};

int main() {
    BusReservationSystem busSystem;
    int choice;
    int seat;
    std::string name, entry, final;

    do {
        std::cout << "\nBus Reservation System Menu:" << std::endl;
        std::cout << "1. Book a Ticket\n2. Cancel a Ticket\n3. Modify a Ticket\n4. View Booked Tickets\n5. Add food\n6. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter seat number, passenger name, entry destination, and final destination: ";
                std::cin >> seat >> name >> entry >> final;
                busSystem.bookTicket(seat, name, entry, final);
                break;

            case 2:
                std::cout << "Enter seat number to cancel the ticket: ";
                std::cin >> seat;
                busSystem.cancelTicket(seat);
                break;

            case 3:
                std::cout << "Enter seat number to modify, new passenger name, new entry destination, and new final destination: ";
                std::cin >> seat >> name >> entry >> final;
                busSystem.modifyTicket(seat, name, entry, final);
                break;

            case 4:
                busSystem.viewTickets();
                break;
            case 5:
                std::cout<<"Enter the seat number to add food to:";
                std::cin>>seat;
                busSystem.addFood(seat);
                break;
            case 6:
                std::cout << "Exiting the program.\n";
                break;

            default:
                std::cout << "Invalid choice. Please enter a valid option.\n";
                break;
        }

    } while (choice != 5);

    return 0;
}