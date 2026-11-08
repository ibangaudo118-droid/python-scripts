SwiftDrop 📦

Parcel Delivery and Tracking Management System

SwiftDrop is a Python-based parcel delivery management system designed to model the core operations of a delivery company. It provides functionality for managing customers, delivery agents, parcel assignments, delivery pricing, and parcel tracking.

The project was developed to apply Object-Oriented Programming (OOP) principles to a practical business use case, with an emphasis on clean class design, object relationships, validation, and controlled state transitions.

---

🎯 Project Objectives

- Manage customer and delivery agent records.
- Create and manage parcel delivery orders.
- Calculate delivery fees based on service type.
- Assign delivery agents to parcels.
- Track parcel delivery progress.
- Maintain a history of parcel status changes.
- Require recipient confirmation before completing a delivery.

⚙️ Core Features

Feature| Description
Customer Management| Register and manage customer information.
Agent Management| Maintain delivery agent records and availability.
Parcel Management| Represent parcels with tracking numbers, descriptions, weight, and delivery distance.
Delivery Pricing| Calculate fees for Standard and Express delivery services.
Agent Assignment| Associate delivery agents with parcel deliveries.
Status Tracking| Track parcel progress through defined delivery stages.
Tracking History| Maintain a chronological record of parcel status changes.
Recipient Confirmation| Require confirmation before marking a parcel as delivered.

🏗️ Object-Oriented Design

SwiftDrop uses several OOP principles to structure its functionality.

1. Inheritance

The "Person" class provides shared attributes and methods inherited by:

- "Customer"
- "DeliveryAgent"

The "DeliveryService" abstract base class is inherited by:

- "StandardDelivery"
- "ExpressDelivery"

2. Encapsulation

Classes manage their own attributes and behaviour, while validation helps prevent invalid parcel information and delivery transitions.

3. Abstraction

The "DeliveryService" abstract class defines a common "calculate_fee()" method that concrete delivery services must implement.

4. Polymorphism

Standard and Express delivery services implement the same "calculate_fee()" interface but use different pricing formulas.

5. Composition

Each "Parcel" creates and owns its own "TrackingHistory" object.

6. Object Relationships

Parcels maintain references to their associated customer and delivery agent objects.

🚚 Delivery Workflow

A parcel follows a controlled delivery lifecycle:

PENDING
   |
   v
PICKED UP
   |
   v
IN TRANSIT
   |
   v
AWAITING CONFIRMATION
   |
   v
DELIVERED

A parcel cannot skip delivery stages or be marked as delivered without recipient confirmation.

💰 Delivery Pricing

SwiftDrop supports two delivery service types.

Standard Delivery

fee = (weight * 50) + (delivery_distance * 20)

Express Delivery

fee = (weight * 80) + (delivery_distance * 35)

The pricing calculation uses the parcel's weight and delivery distance.

🛠️ Technologies Used

- Python 3
- Object-Oriented Programming
- Python ABC Module for abstract base classes

📁 Project Structure

SwiftDrop/
│
├── main.py
└── README.md

The project structure may evolve as additional functionality is implemented.

▶️ Getting Started

Prerequisites

- Python 3.10 or later
- Git

Installation

Clone the repository:

git clone <your-repository-url>

Navigate into the project directory:

cd SwiftDrop

Run the application:

python main.py

🧠 What I Learned

Building SwiftDrop provided practical experience with:

- Designing classes and objects around real-world entities.
- Applying inheritance and method overriding.
- Understanding composition and object references.
- Implementing abstract base classes.
- Using polymorphism to support different delivery services.
- Validating object data with exceptions.
- Managing state transitions and tracking history.
- Structuring a project around business rules.

🚀 Future Improvements

Planned improvements include:

- Persistent storage using PostgreSQL.
- A REST API using FastAPI.
- Customer and delivery agent authentication.
- Automated tests using pytest.
- Improved parcel tracking and management.
- Docker-based application deployment.

👨‍💻 Author

David

Aspiring Backend Engineer | Python Developer

Interested in building reliable backend systems and practical software solutions.

---

SwiftDrop is an educational project developed to strengthen Python programming and software engineering fundamentals.
