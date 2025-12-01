# Micro Banking System using FastAPI

A simple but powerful banking system API built with FastAPI. This project demonstrates RESTful API design with Python, including account management, deposits, withdrawals, and money transfers.

## Features

✅ **Account Management**
- Create new bank accounts
- Update account information
- Delete accounts
- List all accounts with real-time balances

✅ **Banking Operations**
- Deposit money into accounts
- Withdraw money (with balance validation)
- Transfer money between accounts
- Comprehensive transaction logging

✅ **Error Handling**
- Input validation
- Insufficient balance checks
- Account existence verification
- User-friendly error messages

✅ **Transaction Tracking**
- All transactions are logged to `data/transactions.txt`
- View complete transaction history

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Install required packages:**
```bash
pip install fastapi uvicorn requests
```

Or install all at once:
```bash
pip install -r requirements.txt
```

2. **Verify installation:**
```bash
python -c "import fastapi; import uvicorn; import requests; print('All packages installed successfully!')"
```

## Running the Application

### Step 1: Start the API Server

```bash
# Using uvicorn directly
uvicorn api_server:app --reload --port 8000

# Or using Python module
python -m uvicorn api_server:app --reload --port 8000
```

The server will start on `http://127.0.0.1:8000`

You can view the interactive API documentation at: `http://127.0.0.1:8000/docs`

### Step 2: Run the Client Application

In a new terminal window:

```bash
python api_client.py
```

The client provides an interactive menu for all banking operations.

## API Endpoints

### Account Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/account/insert` | Create a new account |
| POST | `/account/update` | Update account details |
| GET | `/account/delete/{account_id}` | Delete an account |
| GET | `/account/list` | List all accounts |

### Banking Operations

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/bank/deposit` | Deposit money |
| POST | `/bank/withdraw` | Withdraw money |
| POST | `/bank/transfer` | Transfer between accounts |
| GET | `/transactions` | View transaction logs |

## Testing

Run the comprehensive test suite to verify all functionality:

```bash
python test_banking_system.py
```

This will test all major operations including:
- Account creation and listing
- Deposit and withdrawal operations
- Money transfers
- Error handling scenarios
- Transaction logging

## Example Usage

### Using the Interactive Client

```
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

Enter choice (1-9): 1
Enter Account ID: ACC001
Enter Name: John Doe
Enter Initial Balance: 5000
```

### Using the API Directly with curl

```bash
# Create an account
curl -X POST "http://127.0.0.1:8000/account/insert" \
  -H "Content-Type: application/json" \
  -d '{
    "account_id": "ACC001",
    "name": "John Doe",
    "balance": 5000
  }'

# List all accounts
curl "http://127.0.0.1:8000/account/list"

# Deposit money
curl -X POST "http://127.0.0.1:8000/bank/deposit" \
  -H "Content-Type: application/json" \
  -d '{
    "account_id": "ACC001",
    "amount": 1000
  }'
```

## File Structure

```
mbs_using_FastAPI/
├── api_server.py          # FastAPI application and endpoints
├── api_client.py          # Interactive CLI client
├── test_banking_system.py # Comprehensive test suite
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── data/
    ├── accounts.txt       # Persistent account storage
    └── transactions.txt   # Transaction logs
```

## Data Storage

- **accounts.txt**: Stores account information in pipe-separated format
  ```
  ACC001|John Doe|5000.00
  ACC002|Jane Smith|8500.50
  ```

- **transactions.txt**: Logs all transactions
  ```
  DEPOSIT | ACC001 | +1000.0
  WITHDRAW | ACC002 | -500.0
  TRANSFER | ACC001 -> ACC003 | 750.0
  ```

## Improvements Made

✨ **Code Quality Enhancements:**
- Added comprehensive error handling
- Input validation for all operations
- Better formatted output in the client
- Connection error handling with helpful messages
- Consistent naming conventions

✨ **Testing & Verification:**
- Created comprehensive test suite (`test_banking_system.py`)
- Verified all endpoints work correctly
- Tested error scenarios
- Validated transaction logging

✨ **Documentation:**
- Updated README with complete setup instructions
- Added API endpoint reference table
- Provided example usage scenarios
- Included file structure overview

## Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Uvicorn Documentation**: https://www.uvicorn.org/
- **Requests Module**: https://www.w3schools.com/python/module_requests.asp
- **Pydantic Documentation**: https://docs.pydantic.dev/

## Troubleshooting

### Port 8000 already in use
Change the port number:
```bash
uvicorn api_server:app --reload --port 8001
```
Then update `API_BASE` in `api_client.py` to `http://127.0.0.1:8001`

### Server connection errors
- Ensure the API server is running before starting the client
- Check that you're using the correct port
- Make sure your firewall allows local connections

### Module not found errors
```bash
# Reinstall all dependencies
pip install --upgrade fastapi uvicorn requests
```

## Future Enhancements

Potential improvements for this project:
- Database integration (SQLite, PostgreSQL)
- User authentication and authorization
- Account types (Savings, Checking, etc.)
- Interest calculation
- Account statement generation
- Data encryption for sensitive information
- Unit tests with pytest
- Docker containerization
- REST API pagination

## License

This project is open source and available for educational purposes.