import requests
import sys

API_BASE = "http://127.0.0.1:8000"


def insert_account():
    try:
        acc_id = input("Enter Account ID: ").strip()
        if not acc_id:
            print("Error: Account ID cannot be empty!")
            return
        name = input("Enter Name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return
        balance = float(input("Enter Initial Balance: "))
        if balance < 0:
            print("Error: Balance cannot be negative!")
            return

        payload = {
            "account_id": acc_id,
            "name": name,
            "balance": balance
        }

        response = requests.post(f"{API_BASE}/account/insert", json=payload)
        print("\nResponse:", response.json())
    except ValueError:
        print("Error: Please enter a valid number for balance!")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def update_account():
    try:
        acc_id = input("Enter Account ID to update: ").strip()
        if not acc_id:
            print("Error: Account ID cannot be empty!")
            return
        name = input("Enter new name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return

        payload = {
            "account_id": acc_id,
            "name": name,
            "balance": 0  
        }

        response = requests.post(f"{API_BASE}/account/update", json=payload)
        print("\nResponse:", response.json())
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def delete_account():
    try:
        acc_id = input("Enter Account ID to delete: ").strip()
        if not acc_id:
            print("Error: Account ID cannot be empty!")
            return
        response = requests.get(f"{API_BASE}/account/delete/{acc_id}")
        print("\nResponse:", response.json())
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def show_accounts():
    try:
        response = requests.get(f"{API_BASE}/account/list")
        accounts = response.json()["accounts"]
        if not accounts:
            print("\nNo accounts found!")
        else:
            print("\n" + "="*60)
            print(f"{'Account ID':<15} {'Name':<20} {'Balance':<15}")
            print("="*60)
            for acc in accounts:
                print(f"{acc['account_id']:<15} {acc['name']:<20} ${acc['balance']:<14.2f}")
            print("="*60)
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")
def deposit():
    try:
        acc_id = input("Enter Account ID: ").strip()
        if not acc_id:
            print("Error: Account ID cannot be empty!")
            return
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Error: Amount must be positive!")
            return

        payload = {"account_id": acc_id, "amount": amount}
        response = requests.post(f"{API_BASE}/bank/deposit", json=payload)
        print("\nResponse:", response.json())
    except ValueError:
        print("Error: Please enter a valid number for amount!")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")]:<15} {acc['name']:<20} ${acc['balance']:<14.2f}")
            print("="*60)
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def deposit():
    acc_id = input("Enter Account ID: ")
    amount = float(input("Enter deposit amount: "))

    payload = {"account_id": acc_id, "amount": amount}
    response = requests.post(f"{API_BASE}/bank/deposit", json=payload)
    print("\nResponse:", response.json())



def withdraw():
    try:
        acc_id = input("Enter Account ID: ").strip()
        if not acc_id:
            print("Error: Account ID cannot be empty!")
            return
        amount = float(input("Enter withdraw amount: "))
        if amount <= 0:
            print("Error: Amount must be positive!")
            return

        payload = {"account_id": acc_id, "amount": amount}
        response = requests.post(f"{API_BASE}/bank/withdraw", json=payload)
        print("\nResponse:", response.json())
    except ValueError:
        print("Error: Please enter a valid number for amount!")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def transfer():
    try:
        from_acc = input("From Account ID: ").strip()
        if not from_acc:
            print("Error: From Account ID cannot be empty!")
            return
        to_acc = input("To Account ID: ").strip()
        if not to_acc:
            print("Error: To Account ID cannot be empty!")
            return
        if from_acc == to_acc:
            print("Error: Cannot transfer to the same account!")
            return
        amount = float(input("Enter transfer amount: "))
        if amount <= 0:
            print("Error: Amount must be positive!")
            return

        payload = {
            "from_acc": from_acc,
            "to_acc": to_acc,
            "amount": amount
        }

        response = requests.post(f"{API_BASE}/bank/transfer", json=payload)
        print("\nResponse:", response.json())
    except ValueError:
        print("Error: Please enter a valid number for amount!")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def show_transactions():
    try:
        response = requests.get(f"{API_BASE}/transactions")
        logs = response.json()["logs"]
        if not logs:
            print("\nNo transactions yet!")
        else:
            print("\n" + "="*80)
            print("TRANSACTION LOGS")
            print("="*80)
            for log in logs:
                print(log.strip())
            print("="*80)
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure it's running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"Error: {str(e)}")


def menu():
    print("""
=====================================
        MICRO BANKING SYSTEM
=====================================
1. Insert Account
2. Update Account
3. Delete Account
4. Show All Accounts
5. Deposit
6. Withdraw
7. Transfer
8. Show Transactions
9. Exit
=====================================
""")


def main():
    while True:
        menu()
        choice = input("Enter choice (1-9): ").strip()

        if choice == "1":
            insert_account()
        elif choice == "2":
            update_account()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            show_accounts()
        elif choice == "5":
            deposit()
        elif choice == "6":
            withdraw()
        elif choice == "7":
            transfer()
        elif choice == "8":
            show_transactions()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid option! Please choose correctly.")


if __name__ == "__main__":
    main()
