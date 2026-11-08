SwiftDrop 📦

Parcel Delivery and Tracking Management System

A Python-based parcel delivery management application built to model the morning core operations of a delivery company through Object-Oriented Programming (OOP).

SwiftDrop demonstrates class design, inheritance, abstraction, polymorphism, composition, object relationships, data validation, and controlled delivery status transitions.

---

Table of Contents

1. "Overview" (#overview)
2. "Features" (#features)
3. "System Architecture" (#system-architecture)
4. "Object-Oriented Design" (#object-oriented-design)
5. "Delivery Workflow" (#delivery-workflow)
6. "Delivery Pricing" (#delivery-pricing)
7. "Technology Stack" (#technology-stack)
8. "Project Structure" (#project-structure)
9. "Getting Started" (#getting-started)
10. "Engineering Concepts" (#engineering-concepts)
11. "Future Improvements" (#future-improvements)
12. "Author" (#author)

---

1. Overview

SwiftDrop is a parcel delivery management application designed around the operational requirements of a delivery company.

The system models how customers register, delivery agents are managed, parcels are created, delivery services calculate fees, and parcels progress through different delivery stages.

The project focuses on translating a real-world business problem into a structured software application using Python's Object-Oriented Programming capabilities.

Rather than organizing the application around unrelated functions, SwiftDrop uses interacting classes with defined responsibilities and relationships.

2. Features

Feature| Description
Customer Management| Register and manage customer information.
Delivery Agent Management| Maintain delivery agent records and availability.
Parcel Management| Create and manage parcel delivery records.
Delivery Pricing| Calculate fees for Standard and Express delivery services.
Agent Assignment| Associate delivery agents with parcel deliveries.
Status Management| Control parcel progression through defined delivery stages.
Tracking History| Maintain a chronological record of parcel status changes.
Recipient Confirmation| Require recipient confirmation before completing a delivery.
Input Validation| Reject invalid parcel information and unsupported operations.

3. System Architecture

SwiftDrop is organized around the following core classes:

Class| Responsibility
"Person"| Provides shared attributes and behaviour for people in the system.
"Customer"| Represents a customer requesting parcel delivery.
"DeliveryAgent"| Represents an agent responsible for delivering parcels.
"Parcel"| Stores parcel information and manages its delivery status.
"TrackingHistory"| Records the chronological history of parcel status changes.
"DeliveryService"| Defines the abstract interface for delivery fee calculation.
"StandardDelivery"| Implements standard delivery pricing.
"ExpressDelivery"| Implements express delivery pricing.
"SwiftDropManagement"| Coordinates customer, agent, and parcel management operations.

Class Relationships

- "Customer" and "DeliveryAgent" inherit from "Person".
- "StandardDelivery" and "ExpressDelivery" inherit from "DeliveryService".
- "Parcel" maintains references to its associated customer and delivery agent.
- "Parcel" owns a "TrackingHistory" instance through composition.
- "SwiftDropManagement" coordinates the management of customers, agents, and parcels.

4. Object-Oriented Design

The project applies the following OOP principles:

4.1 Inheritance

The "Person" class provides shared attributes and methods inherited by:

- "Customer"
- "DeliveryAgent"

The "DeliveryService" abstract base class is inherited by:

- "StandardDelivery"
- "ExpressDelivery"

This reduces unnecessary code duplication and establishes relationships between related classes.

4.2 Encapsulation

Classes organize their data and behaviour while applying validation to protect important operations.

For example, the "Parcel" class validates parcel weight and delivery distance and controls permitted delivery status transitions.

4.3 Abstraction

The "DeliveryService" abstract base class defines a common "calculate_fee()" method.

Concrete delivery service classes must provide their own implementation of this method.

4.4 Polymorphism

Both "StandardDelivery" and "ExpressDelivery" implement the same "calculate_fee()" interface but use different pricing formulas.

This allows different delivery strategies to share a common interface while maintaining their individual implementations.

4.5 Composition

Each "Parcel" creates and owns its own "TrackingHistory" instance.

This ensures that every parcel maintains an independent record of its delivery progress.

4.6 Object Relationships

A parcel maintains references to its associated customer and delivery agent objects.

The management class coordinates these objects and their relationships within the application.

5. Delivery Workflow

SwiftDrop follows a controlled parcel delivery lifecycle:

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

Delivery Rules

- A parcel must begin in the "Pending" state.
- Delivery stages must follow the defined sequence.
- A parcel cannot skip required stages.
- Recipient confirmation is required before the parcel can be marked as "Delivered".
- Successful status changes are recorded in the parcel's tracking history.

These rules help maintain consistency throughout the delivery process.

6. Delivery Pricing

SwiftDrop supports two delivery service types.

Standard Delivery

The standard delivery fee is calculated using:

fee = (weight * 50) + (delivery_distance * 20)

Express Delivery

The express delivery fee is calculated using:

fee = (weight * 80) + (delivery_distance * 35)

Both services calculate delivery fees using parcel weight and delivery distance but apply different pricing rates.

7. Technology Stack

Technology| Purpose
Python 3| Primary programming language
"abc" module| Abstract base classes and abstraction
Object-Oriented Programming| Application architecture and class relationships
Git| Version control
GitHub| Source code hosting

8. Project Structure

swiftdrop-delivery-management-system/
│
├── swiftdrop_delivery_management_systems.py
│
└── README.md

9. Getting Started

Follow these instructions to run SwiftDrop locally.

Prerequisites

- Python 3.10 or later
- Git

Step 1: Clone the Repository

git clone https://github.com/ibangaudo118-droid/python-scripts.git

Step 2: Navigate to the Project Directory

cd python-scripts/swiftdrop-delivery-management-system

Step 3: Run the Application

python swiftdrop_delivery_management_systems.py

10. Engineering Concepts

Building SwiftDrop provided practical experience with:

- Translating business requirements into software components.
- Designing classes around real-world entities.
- Applying inheritance and method overriding.
- Understanding object references and object relationships.
- Implementing composition and aggregation.
- Using abstract base classes.
- Applying polymorphism to support different delivery services.
- Validating data using exceptions.
- Managing state transitions and tracking history.
- Coordinating multiple objects through a management class.

11. Future Improvements

Potential extensions to the project include:

- PostgreSQL integration for persistent data storage.
- REST API development using FastAPI.
- Automated testing with pytest.
- Customer and delivery agent authentication.
- Docker containerisation.
- Application deployment.

These represent possible future development directions rather than currently implemented features.

12. Author

David

Aspiring Backend Engineer | Python Developer

Focused on building reliable software systems, strengthening engineering fundamentals, and solving practical business problems through technology.

---

Project: SwiftDrop
Language: Python
Category: Object-Oriented Programming / Software Engineering

SwiftDrop is a personal software engineering project developed as part of my journey in Python and backend engineering.x