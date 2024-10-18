import sys
import os

path_to_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_src)

from dao.PolicyServiceImpl import PolicyServiceImpl
from dao.ClientServiceImpl import ClientServiceImpl
from dao.ClaimServiceImpl import ClaimServiceImpl
from dao.UserServiceImpl import UserServiceImpl
from dao.PaymentServiceImpl import PaymentServiceImpl
from entity.Policy import Policy
from entity.Client import Client
from entity.Claim import Claim
from entity.User import User
from entity.Payment import Payment
from exceptions.PolicyNotFoundException import PolicyNotFoundException

if __name__ == "__main__":
    
    # Create instances of service classes
    policy_service = PolicyServiceImpl()
    client_service = ClientServiceImpl()
    claim_service = ClaimServiceImpl()
    user_service = UserServiceImpl()
    payment_service = PaymentServiceImpl()

    while True:
        print("\nInsurance Management System")
        print("1. Create Client")
        print("2. Create Policy")
        print("3. Get Policy")
        print("4. Get All Policies")
        print("5. Update Policy")
        print("6. Delete Policy")
        print("7. Create User")
        print("8. Get User")
        print("9. Get All Users")
        print("10. Update User")
        print("11. Delete User")
        print("12. Create Claim")
        print("13. Get Claim")
        print("14. Get All Claims")
        print("15. Create Payment")
        print("16. Get Payment")
        print("17. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Create Client
           
            clientName = input("Enter client name: ")
            contactInfo = input("Enter contact info: ")
            policy = input("Enter policy: ")
            client = Client(clientName=clientName, contactInfo=contactInfo, policy=policy)
            client_service.createClient(client)
            print("Client created successfully!")

        elif choice == '2':  # Create Policy
            policyName = input("Enter policy name: ")
            policyDescription = input("Enter policy description: ")
            policy = Policy(policyName=policyName, policyDescription=policyDescription)
            policy_service.createPolicy(policy)
            print("Policy created successfully!")

        elif choice == '3':  # Get Policy
            policyId = int(input("Enter policy ID: "))
            try:
                policy = policy_service.getPolicy(policyId)
                print(policy)
            except PolicyNotFoundException as e:
                print(e)

        elif choice == '4':  # Get All Policies
            policies = policy_service.getAllPolicies()
            for policy in policies:
                print(policy)

        elif choice == '5':  # Update Policy
            policyId = int(input("Enter policy ID: "))
            policyName = input("Enter new policy name: ")
            policyDescription = input("Enter new policy description: ")
            policy = Policy(policyId=policyId, policyName=policyName, policyDescription=policyDescription)
            policy_service.updatePolicy(policy)
            print("Policy updated successfully!")

        elif choice == '6':  # Delete Policy
            policyId = int(input("Enter policy ID: "))
            policy_service.deletePolicy(policyId)
            print("Policy deleted successfully!")

        elif choice == '7':  # Create User
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/user): ")
            user = User(username=username, password=password, role=role)
            user_service.createUser(user)
            print("User created successfully!")

        elif choice == '8':  # Get User
            userId = int(input("Enter user ID: "))
            user = user_service.getUser(userId)
            if user:
                print(user)
            else:
                print("User not found.")

        elif choice == '9':  # Get All Users
            users = user_service.getAllUsers()
            for user in users:
                print(user)

        elif choice == '10':  # Update User
            userId = int(input("Enter user ID: "))
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            role = input("Enter new role (admin/user): ")
            user = User(userId=userId, username=username, password=password, role=role)
            user_service.updateUser(user)
            print("User updated successfully!")

        elif choice == '11':  # Delete User
            userId = int(input("Enter user ID: "))
            user_service.deleteUser(userId)
            print("User deleted successfully!")

        elif choice == '12':  # Create Claim
            claimNumber = input("Enter claim number: ")
            dateFiled = input("Enter date filed (YYYY-MM-DD): ")
            claimAmount = float(input("Enter claim amount: "))
            status = input("Enter status: ")
            policy = input("Enter associated policy: ")
            clientId = input("Enter associated client: ")
            claim = Claim(claimNumber=claimNumber, dateFiled=dateFiled, claimAmount=claimAmount, status=status,
                          policy=policy, clientId=clientId)
            claim_service.createClaim(claim)
            print("Claim created successfully!")

        elif choice == '13':  # Get Claim
            claimId = int(input("Enter claim ID: "))
            claim = claim_service.getClaim(claimId)
            if claim:
                print(claim)
            else:
                print("Claim not found.")

        elif choice == '14':  # Get All Claims
            claims = claim_service.getAllClaims()
            for claim in claims:
                print(claim)

        elif choice == '15':  # Create Payment
            paymentDate = input("Enter payment date (YYYY-MM-DD): ")
            paymentAmount = float(input("Enter payment amount: "))
            client = input("Enter associated client: ")
            payment = Payment(paymentDate=paymentDate, paymentAmount=paymentAmount, client=client)
            payment_service.createPayment(payment)
            print("Payment created successfully!")

        elif choice == '16':  # Get Payment
            paymentId = int(input("Enter payment ID: "))
            payment = payment_service.getPayment(paymentId)
            if payment:
                print(payment)
            else:
                print("Payment not found.")

        elif choice == '17':  # Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")