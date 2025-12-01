#!/usr/bin/env python3
"""
Test script for the Micro Banking System API
Demonstrates all major operations without user input
"""

import requests
import json
import time

API_BASE = "http://127.0.0.1:9999"

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_api():
    try:
        # Test 1: List existing accounts
        print_section("1. LISTING EXISTING ACCOUNTS")
        response = requests.get(f"{API_BASE}/account/list")
        accounts = response.json()["accounts"]
        print(f"Found {len(accounts)} existing accounts:")
        for acc in accounts:
            print(f"  - {acc['account_id']}: {acc['name']} (Balance: ${acc['balance']:.2f})")

        # Test 2: Insert a new account
        print_section("2. CREATING NEW ACCOUNT")
        new_account = {
            "account_id": "ACC004",
            "name": "Alice Johnson",
            "balance": 2500.00
        }
        response = requests.post(f"{API_BASE}/account/insert", json=new_account)
        print(f"Response: {response.json()}")

        # Test 3: List accounts again
        print_section("3. LISTING ACCOUNTS AFTER INSERT")
        response = requests.get(f"{API_BASE}/account/list")
        accounts = response.json()["accounts"]
        print(f"Now have {len(accounts)} accounts:")
        for acc in accounts:
            print(f"  - {acc['account_id']}: {acc['name']} (Balance: ${acc['balance']:.2f})")

        # Test 4: Deposit money
        print_section("4. DEPOSIT OPERATION")
        deposit_data = {"account_id": "ACC001", "amount": 1000.00}
        response = requests.post(f"{API_BASE}/bank/deposit", json=deposit_data)
        print(f"Deposit result: {response.json()}")

        # Test 5: Withdraw money
        print_section("5. WITHDRAW OPERATION")
        withdraw_data = {"account_id": "ACC002", "amount": 500.00}
        response = requests.post(f"{API_BASE}/bank/withdraw", json=withdraw_data)
        print(f"Withdraw result: {response.json()}")

        # Test 6: Transfer money
        print_section("6. TRANSFER OPERATION")
        transfer_data = {
            "from_acc": "ACC001",
            "to_acc": "ACC003",
            "amount": 750.00
        }
        response = requests.post(f"{API_BASE}/bank/transfer", json=transfer_data)
        print(f"Transfer result: {response.json()}")

        # Test 7: Show final balances
        print_section("7. FINAL ACCOUNT BALANCES")
        response = requests.get(f"{API_BASE}/account/list")
        accounts = response.json()["accounts"]
        print(f"{'Account ID':<15} {'Name':<20} {'Balance':<15}")
        print("-" * 50)
        for acc in accounts:
            print(f"{acc['account_id']:<15} {acc['name']:<20} ${acc['balance']:<14.2f}")

        # Test 8: Show transaction logs
        print_section("8. TRANSACTION LOGS")
        response = requests.get(f"{API_BASE}/transactions")
        logs = response.json()["logs"]
        if logs:
            for log in logs:
                print(f"  {log.strip()}")
        else:
            print("  No transactions yet")

        # Test 9: Error handling - Insufficient balance
        print_section("9. ERROR HANDLING - INSUFFICIENT BALANCE")
        withdraw_data = {"account_id": "ACC002", "amount": 50000.00}
        response = requests.post(f"{API_BASE}/bank/withdraw", json=withdraw_data)
        print(f"Result: {response.json()}")

        # Test 10: Error handling - Account not found
        print_section("10. ERROR HANDLING - ACCOUNT NOT FOUND")
        deposit_data = {"account_id": "ACC999", "amount": 100.00}
        response = requests.post(f"{API_BASE}/bank/deposit", json=deposit_data)
        print(f"Result: {response.json()}")

        print_section("ALL TESTS COMPLETED SUCCESSFULLY!")

    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to server!")
        print("Make sure the API server is running on http://127.0.0.1:8000")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  MICRO BANKING SYSTEM - API TEST SUITE")
    print("="*60)
    test_api()
