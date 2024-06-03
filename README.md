# Bus Reservation System with GUI
During my 3rd semester at university, as part of a minor course on C++, I developed a comprehensive bus reservation system. This project aimed to streamline the process of booking, cancelling, and modifying bus tickets, as well as enhancing the passenger experience by allowing additional services such as adding food preferences. The system was designed to manage reservations efficiently and ensure a seamless user experience through a graphical user interface (GUI) using PyQt5.

## Technical Details

### Language and Tools
  - C++: Core logic and data structures for managing bus reservations.
  - PyQt5: GUI framework for creating an intuitive and user-friendly interface.

### Key Features
  - Ticket Booking: Allows users to book tickets by providing seat number, passenger name, entry, and final destinations. The system checks for seat availability to prevent booking conflicts.
  - Ticket Cancellation: Enables users to cancel previously booked tickets by specifying the seat number.
  - Ticket Modification: Permits users to modify the details of existing bookings, including passenger name, entry, and final destinations.
  - View Booked Tickets: Displays a list of all currently booked tickets with detailed information.
  - Add Food: Offers the option to add food preferences to a specific booking.

### Data Management
Utilized a singly linked list data structure to efficiently manage and traverse the list of booked tickets, ensuring dynamic memory allocation and deallocation as tickets are booked and cancelled.
    
### Error Handling and Validation
Implemented robust error handling to manage scenarios such as booking conflicts, invalid seat numbers, and attempts to cancel or modify non-existent tickets.Provided user feedback through the GUI to inform users of successful operations or errors.


## Challenges and Learning Outcomes

  - Conflict Resolution: Developed a method to check for booking conflicts, ensuring that no two passengers can book the same seat.
  - GUI Development: Gained hands-on experience with PyQt5, enhancing my skills in creating interactive and user-friendly graphical interfaces.
  - Dynamic Data Structures: Strengthened my understanding of linked lists and their application in real-world scenarios.
  - Project Management: Managed the end-to-end development process, from initial design and implementation to testing and deployment.

## Conclusion
This project not only reinforced my programming skills in C++ but also introduced me to the world of GUI development. It provided a practical application of data structures and algorithms in solving real-world problems and highlighted the importance of user-centric design in software development. The successful completion of this project demonstrated my ability to integrate core programming concepts with modern interface design to create a functional and user-friendly application.

