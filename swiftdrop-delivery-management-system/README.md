	xx# SwiftDrop 📦

### Parcel Delivery and Tracking Management System

A Python-based parcel delivery management application built to model the morning core operations of a delivery company through Object-Oriented Programming (OOP).

SwiftDrop demonstrates class design, inheritance, abstraction, polymorphism, composition, object relationships, data validation, and controlled delivery status transitions.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Features](#2-features)
3. [System Architecture](#3-system-architecture)
4. [Object-Oriented Design](#4-object-oriented-design)
5. [Delivery Workflow](#5-delivery-workflow)
6. [Delivery Pricing](#6-delivery-pricing)
7. [Technology Stack](#7-technology-stack)
8. [Project Structure](#8-project-structure)
9. [Getting Started](#9-getting-started)
10. [Engineering Concepts](#10-engineering-concepts)
11. [Future Improvements](#11-future-improvements)
12. [Author](#12-author)

---

## 1. Overview

SwiftDrop is a parcel delivery management application designed around the operational requirements of a delivery company.

The system models how customers register, delivery agents are managed, parcels are created, delivery services calculate fees, and parcels progress through different delivery stages.

The project focuses on translating a real-world business problem into a structured software application using Python's Object-Oriented Programming capabilities.

Rather than organizing the application around unrelated functions, SwiftDrop uses interacting classes with defined responsibilities and relationships.

## 2. Features

| Feature | Description |
| :--- | :--- |
| Customer Management | Register and manage customer information. |
| Delivery Agent Management | Maintain delivery agent records and availability. |
| Parcel Management | Create and manage parcel delivery records. |
| Delivery Pricing | Calculate fees for Standard and Express delivery services. |
| Agent Assignment | Associate delivery agents with parcel deliveries. |
| Status Management | Control parcel progression through defined delivery stages. |
| Tracking History | Maintain a chronological record of parcel status changes. |
| Recipient Confirmation | Require recipient confirmation before completing a delivery. |
| Input Validation | Reject invalid parcel information and unsupported operations. |

## 3. System Architecture

SwiftDrop is organized around the following core classes:

| Class | Responsibility |
| :--- | :--- |
| `Person` | Provides shared attributes and behaviour for people in the system. |
| `Customer` | Represents a customer requesting parcel delivery. |
| `DeliveryAgent` | Represents an agent responsible for delivering parcels. |
| `Parcel` | Stores parcel information and manages its delivery status. |
| `TrackingHistory` | Records the chronological history of parcel status changes. |
| `DeliveryService` | Defines the abstract interface for delivery fee calculation. |
| `StandardDelivery` | Implements standard delivery pricing. |
| `ExpressDelivery` | Implements express delivery pricing. |
| `SwiftDropManagement` | Coordinates customer, agent, and parcel management operations. |

**Class Relationships**

- `Customer` and `DeliveryAgent` inherit from `Person`.
- `StandardDelivery` and `ExpressDelivery` inherit from `DeliveryService`.
- `Parcel` maintains references to its associated customer and delivery agent.
- `Parcel` owns a `TrackingHistory` instance through composition.
- `SwiftDropManagement` coordinates the management of customers, agents, and parcels.

## 4. Object-Oriented Design

The project applies the following OOP principles:

### 4.1 Inheritance

The `Person` class provides shared attributes and methods inherited by:

- `Customer`
- `DeliveryAgent`

The `DeliveryService` abstract base class is inherited by:

- `StandardDelivery`
- `ExpressDelivery`

This reduces unnecessary code duplication and establishes relationships between related classes.

### 4.2 Encapsulation

Classes organize their data and behaviour while applying validation to protect important operations.

For example, the `Parcel` class validates parcel weight and delivery distance and controls permitted delivery status transitions.

### 4.3 Abstraction

The `DeliveryService` abstract base class defines a common `calculate_fee()` method.

Concrete delivery service classes must provide their own implementation of this method.

### 4.4 Polymorphism

Both `StandardDelivery` and `ExpressDelivery` implement the same `calculate_fee()` interface but use different pricing formulas.

This allows different delivery strategies to share a common interface while maintaining their individual implementations.

### 4.5 Composition

Each `Parcel` creates and owns its own `TrackingHistory` instance.

This ensures that every parcel maintains an independent record of its delivery progress.

### 4.6 Object Relationships

A parcel maintains references to its associated customer and delivery agent objects.

The management class coordinates these objects and their relationships within the application.

## 5. Delivery Workflow

SwiftDrop follows a controlled parcel delivery lifecycle:

```text
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
