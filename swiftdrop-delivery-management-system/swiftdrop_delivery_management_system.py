from abc import ABC, abstractmethod


# ==========================================
# 1. PERSON
# ==========================================

class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone_number}")


# ==========================================
# 2. CUSTOMER
# ==========================================

class Customer(Person):
    def __init__(self, name, phone_number, customer_id):
        super().__init__(name, phone_number)
        self.customer_id = customer_id

    def display_customer_info(self):
        self.display_info()
        print(f"Customer ID: {self.customer_id}")


# ==========================================
# 3. DELIVERY AGENT
# ==========================================

class DeliveryAgent(Person):
    def __init__(self, name, phone_number, agent_id):
        super().__init__(name, phone_number)
        self.agent_id = agent_id
        self.agent_availability = "Available"

    def display_agent_info(self):
        self.display_info()
        print(f"Agent ID: {self.agent_id}")
        print(f"Availability: {self.agent_availability}")


# ==========================================
# 4. TRACKING HISTORY
# ==========================================

class TrackingHistory:
    def __init__(self):
        self.history = ["Pending"]

    def add_entry(self, status):
        self.history.append(status)

    def display_history(self):
        for status in self.history:
            print(status)


# ==========================================
# 5. PARCEL
# ==========================================

class Parcel:
    VALID_TRANSITIONS = {
        "Pending": "Picked Up",
        "Picked Up": "In Transit",
        "In Transit": "Awaiting Confirmation"
    }

    def __init__(
        self,
        tracking_number,
        description,
        weight,
        delivery_distance,
        customer
    ):
        if weight <= 0:
            raise ValueError("Weight must be greater than zero")

        if delivery_distance <= 0:
            raise ValueError("Distance must be greater than zero")

        self.tracking_number = tracking_number
        self.description = description
        self.weight = weight
        self.delivery_distance = delivery_distance

        self.customer = customer
        self.delivery_agent = None

        self.delivery_status = "Pending"
        self.tracking_history = TrackingHistory()

        self.delivery_type = None
        self.delivery_fee = None

    def update_status(self, new_status):
        if self.delivery_status in ("Delivered", "Cancelled"):
            raise ValueError("Parcel cannot be updated")

        expected_status = self.VALID_TRANSITIONS.get(
            self.delivery_status
        )

        if new_status != expected_status:
            raise ValueError("Invalid delivery transition")

        self.delivery_status = new_status
        self.tracking_history.add_entry(new_status)

        return self.delivery_status

    def recipient_confirmation(self, confirmation):
        if self.delivery_status != "Awaiting Confirmation":
            raise ValueError("Parcel is not awaiting confirmation")

        if confirmation.lower() != "yes":
            raise ValueError("Recipient confirmation rejected")

        self.delivery_status = "Delivered"
        self.tracking_history.add_entry("Delivered")

        return self.delivery_status

    def cancel(self):
        if self.delivery_status in ("Delivered", "Cancelled"):
            raise ValueError("Parcel cannot be cancelled")

        self.delivery_status = "Cancelled"
        self.tracking_history.add_entry("Cancelled")


# ==========================================
# 6. DELIVERY SERVICE
# ==========================================

class DeliveryService(ABC):

    @abstractmethod
    def calculate_fee(self, parcel):
        pass


class StandardDelivery(DeliveryService):

    def calculate_fee(self, parcel):
        return (
            parcel.weight * 50
            + parcel.delivery_distance * 20
        )


class ExpressDelivery(DeliveryService):

    def calculate_fee(self, parcel):
        return (
            parcel.weight * 80
            + parcel.delivery_distance * 35
        )


# ==========================================
# 7. SWIFTDROP MANAGEMENT
# ==========================================

class SwiftDropManagement:

    def __init__(self):
        self.customers = []
        self.agents = []
        self.parcels = []

        self.tracking_counter = 1

    # --------------------------------------
    # CUSTOMER REGISTRATION
    # --------------------------------------

    def register_customer(self, customer):

        for existing_customer in self.customers:
            if existing_customer.customer_id == customer.customer_id:
                raise ValueError("Customer ID already exists")

        self.customers.append(customer)

    # --------------------------------------
    # AGENT REGISTRATION
    # --------------------------------------

    def register_agent(self, agent):

        for existing_agent in self.agents:
            if existing_agent.agent_id == agent.agent_id:
                raise ValueError("Agent ID already exists")

        self.agents.append(agent)

    # --------------------------------------
    # PARCEL REGISTRATION
    # --------------------------------------

    def register_parcel(self, parcel):

        for existing_parcel in self.parcels:
            if existing_parcel.tracking_number == parcel.tracking_number:
                raise ValueError("Tracking number already exists")

        self.parcels.append(parcel)

    # --------------------------------------
    # PARCEL CREATION
    # --------------------------------------

    def create_parcel(
        self,
        description,
        weight,
        distance,
        customer,
        delivery_type
    ):

        if customer not in self.customers:
            raise ValueError("Customer is not registered")

        if delivery_type == "Standard":
            service = StandardDelivery()

        elif delivery_type == "Express":
            service = ExpressDelivery()

        else:
            raise ValueError("Invalid delivery type")

        tracking_number = f"SDP{self.tracking_counter:04d}"

        parcel = Parcel(
            tracking_number,
            description,
            weight,
            distance,
            customer
        )

        parcel.delivery_type = delivery_type
        parcel.delivery_fee = service.calculate_fee(parcel)

        self.register_parcel(parcel)

        self.tracking_counter += 1

        return parcel

    # --------------------------------------
    # AGENT ASSIGNMENT
    # --------------------------------------

    def assign_agent(self, parcel, agent):

        if parcel not in self.parcels:
            raise ValueError("Parcel is not registered")

        if agent not in self.agents:
            raise ValueError("Agent is not registered")

        if parcel.delivery_status != "Pending":
            raise ValueError("Parcel is no longer assignable")

        if parcel.delivery_agent is not None:
            raise ValueError("Parcel already has an agent")

        if agent.agent_availability != "Available":
            raise ValueError("Agent is unavailable")

        parcel.delivery_agent = agent
        agent.agent_availability = "Unavailable"

    # --------------------------------------
    # DELIVERY STATUS MANAGEMENT
    # --------------------------------------

    def update_delivery_status(self, parcel, agent, new_status):

        if parcel not in self.parcels:
            raise ValueError("Parcel is not registered")

        if parcel.delivery_agent is not agent:
            raise ValueError("Agent is not assigned to this parcel")

        parcel.update_status(new_status)

        if new_status == "Delivered":
            agent.agent_availability = "Available"

    # --------------------------------------
    # RECIPIENT CONFIRMATION
    # --------------------------------------

    def confirm_delivery(self, parcel, confirmation):

        if parcel not in self.parcels:
            raise ValueError("Parcel is not registered")

        if parcel.delivery_agent is None:
            raise ValueError("Parcel has no assigned agent")

        parcel.recipient_confirmation(confirmation)

        parcel.delivery_agent.agent_availability = "Available"

    # --------------------------------------
    # CANCELLATION
    # --------------------------------------

    def cancel_parcel(self, parcel):

        if parcel not in self.parcels:
            raise ValueError("Parcel is not registered")

        parcel.cancel()

        if parcel.delivery_agent is not None:
            parcel.delivery_agent.agent_availability = "Available"

    # --------------------------------------
    # PARCEL LOOKUP
    # --------------------------------------

    def find_parcel(self, tracking_number):

        for parcel in self.parcels:
            if parcel.tracking_number == tracking_number:
                return parcel

        raise ValueError("Parcel not found")

    # --------------------------------------
    # DISPLAY METHODS
    # --------------------------------------

    def display_customers(self):

        for customer in self.customers:
            customer.display_customer_info()
            print("----------------")

    def display_agents(self):

        for agent in self.agents:
            agent.display_agent_info()
            print("----------------")

    def display_parcels(self):

        for parcel in self.parcels:
            print(f"Tracking Number: {parcel.tracking_number}")
            print(f"Description: {parcel.description}")
            print(f"Customer: {parcel.customer.name}")
            print(f"Agent: {parcel.delivery_agent.name if parcel.delivery_agent else 'Unassigned'}")
            print(f"Status: {parcel.delivery_status}")
            print(f"Delivery Type: {parcel.delivery_type}")
            print(f"Delivery Fee: {parcel.delivery_fee}")
            print("----------------")


# ==========================================
# 8. TERMINAL APPLICATION
# ==========================================

def main():

    system = SwiftDropManagement()

    while True:

        print("\n========== SWIFTDROP ==========")
        print("1. Register Customer")
        print("2. Register Delivery Agent")
        print("3. Create Parcel")
        print("4. Assign Agent")
        print("5. Update Delivery Status")
        print("6. Confirm Delivery")
        print("7. Cancel Parcel")
        print("8. Track Parcel")
        print("9. Display Customers")
        print("10. Display Agents")
        print("11. Display Parcels")
        print("0. Exit")

        choice = input("Choose an option: ")

        try:

            if choice == "1":

                name = input("Customer name: ")
                phone = input("Phone number: ")
                customer_id = input("Customer ID: ")

                customer = Customer(name, phone, customer_id)

                system.register_customer(customer)

                print("Customer registered successfully")

            elif choice == "2":

                name = input("Agent name: ")
                phone = input("Phone number: ")
                agent_id = input("Agent ID: ")

                agent = DeliveryAgent(name, phone, agent_id)

                system.register_agent(agent)

                print("Agent registered successfully")

            elif choice == "3":

                customer_id = input("Customer ID: ")

                customer = next(
                    (
                        c for c in system.customers
                        if c.customer_id == customer_id
                    ),
                    None
                )

                if customer is None:
                    raise ValueError("Customer not found")

                description = input("Parcel description: ")
                weight = float(input("Weight: "))
                distance = float(input("Distance: "))

                delivery_type = input(
                    "Delivery type (Standard/Express): "
                ).title()

                parcel = system.create_parcel(
                    description,
                    weight,
                    distance,
                    customer,
                    delivery_type
                )

                print("Parcel created successfully")
                print("Tracking Number:", parcel.tracking_number)
                print("Delivery Fee:", parcel.delivery_fee)

            elif choice == "4":

                tracking_number = input("Tracking number: ")
                agent_id = input("Agent ID: ")

                parcel = system.find_parcel(tracking_number)

                agent = next(
                    (
                        a for a in system.agents
                        if a.agent_id == agent_id
                    ),
                    None
                )

                if agent is None:
                    raise ValueError("Agent not found")

                system.assign_agent(parcel, agent)

                print("Agent assigned successfully")

            elif choice == "5":

                tracking_number = input("Tracking number: ")
                agent_id = input("Agent ID: ")
                status = input("New status: ").title()

                parcel = system.find_parcel(tracking_number)

                agent = next(
                    (
                        a for a in system.agents
                        if a.agent_id == agent_id
                    ),
                    None
                )

                if agent is None:
                    raise ValueError("Agent not found")

                system.update_delivery_status(
                    parcel,
                    agent,
                    status
                )

                print("Status updated successfully")

            elif choice == "6":

                tracking_number = input("Tracking number: ")

                parcel = system.find_parcel(tracking_number)

                confirmation = input(
                    "Has the recipient confirmed delivery? (yes/no): "
                )

                system.confirm_delivery(parcel, confirmation)

                print("Delivery confirmed successfully")

            elif choice == "7":

                tracking_number = input("Tracking number: ")

                parcel = system.find_parcel(tracking_number)

                system.cancel_parcel(parcel)

                print("Parcel cancelled successfully")

            elif choice == "8":

                tracking_number = input("Tracking number: ")

                parcel = system.find_parcel(tracking_number)

                print("Current status:", parcel.delivery_status)

                print("Tracking history:")

                parcel.tracking_history.display_history()

            elif choice == "9":
                system.display_customers()

            elif choice == "10":
                system.display_agents()

            elif choice == "11":
                system.display_parcels()

            elif choice == "0":

                print("Thank you for using SwiftDrop")
                break

            else:
                print("Invalid menu option")

        except (ValueError, AttributeError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
