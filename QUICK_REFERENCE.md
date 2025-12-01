# Quick Reference Card - Micro Banking System

## 🎯 INSTANT START

### Windows Users - ONE CLICK
```
Double-click: START.bat
↓
System starts automatically
↓
Enter menu choices 1-9
```

### PowerShell Users
```powershell
.\START.ps1
```

### Manual Setup
**Terminal 1:**
```powershell
.\.venv\Scripts\python.exe -m uvicorn api_server:app --reload --port 8000
```

**Terminal 2:**
```powershell
.\.venv\Scripts\python.exe api_client.py
```

---

## 📖 MENU REFERENCE

```
┌─────────────────────────────────────────┐
│    MICRO BANKING SYSTEM - MENU          │
├─────────────────────────────────────────┤
│ 1 → Create New Account                  │
│ 2 → Update Account Name                 │
│ 3 → Delete Account                      │
│ 4 → Show All Accounts & Balances        │
│ 5 → Deposit Money                       │
│ 6 → Withdraw Money                      │
│ 7 → Transfer Between Accounts           │
│ 8 → View Transaction History            │
│ 9 → Exit Application                    │
└─────────────────────────────────────────┘
```

---

## 💰 EXAMPLE TRANSACTION FLOW

### Scenario: Daily Banking Operations

**Step 1: Check Accounts** (Menu: 4)
```
OUTPUT:
Account ID    Name              Balance
ACC001        John Doe          $5000.00
ACC002        Jane Smith        $8500.50
ACC003        Bob Wilson        $3250.75
```

**Step 2: Make a Deposit** (Menu: 5)
```
INPUT:
Account ID: ACC001
Amount: 1500.00

OUTPUT:
Deposit successful
```

**Step 3: Make a Withdrawal** (Menu: 6)
```
INPUT:
Account ID: ACC002
Amount: 1000.00

OUTPUT:
Withdrawal successful
```

**Step 4: Transfer Money** (Menu: 7)
```
INPUT:
From: ACC001
To: ACC003
Amount: 500.00

OUTPUT:
Transfer successful
```

**Step 5: Check Updated Balances** (Menu: 4)
```
OUTPUT:
Account ID    Name              Balance
ACC001        John Doe          $6000.00    ← +1500 deposit, -500 transfer
ACC002        Jane Smith        $7500.50    ← -1000 withdrawal
ACC003        Bob Wilson        $3750.75    ← +500 transfer
```

**Step 6: View Transaction Log** (Menu: 8)
```
OUTPUT:
DEPOSIT | ACC001 | +1500.0
WITHDRAW | ACC002 | -1000.0
TRANSFER | ACC001 -> ACC003 | 500.0
```

---

## 🔢 QUICK TEST DATA

### Default Accounts
```
ACC001 | John Doe   | $5,000.00
ACC002 | Jane Smith | $8,500.50
ACC003 | Bob Wilson | $3,250.75
```

### Test Operations
```
✓ Deposit $1000 to ACC001
✓ Withdraw $500 from ACC002
✓ Transfer $750 from ACC001 to ACC003
✓ Check updated balances
✓ View all transactions
```

---

## ⚠️ COMMON ERRORS & SOLUTIONS

### Error 1: "Cannot connect to server"
```
❌ Client running but server not started
✅ Solution: Start server in Terminal 1 first
```

### Error 2: "Account not found"
```
❌ Entered wrong account ID
✅ Use: ACC001, ACC002, or ACC003
```

### Error 3: "Insufficient balance"
```
❌ Trying to withdraw more than available
✅ Check balance (Menu 4) before withdrawing
```

### Error 4: "Amount must be positive"
```
❌ Entered negative or zero amount
✅ Enter positive numbers only: 100, 500, 1000
```

### Error 5: "Port 8000 already in use"
```
❌ Another app using port 8000
✅ Command: netstat -ano | findstr :8000
   Then: taskkill /PID <PID> /F
```

---

## 📊 SYSTEM STATUS CHECK

### Server Running? ✓
Look for in Terminal 1:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### Client Connected? ✓
Look for in Terminal 2:
```
Enter choice (1-9):
```

### Data Files Present? ✓
```
✓ data/accounts.txt      (Account records)
✓ data/transactions.txt  (Transaction logs)
```

---

## 🔧 USEFUL COMMANDS

### Check Python Version
```powershell
python --version
```

### Activate Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies
```powershell
pip install -r requirements.txt
```

### Run Automated Tests
```powershell
.\.venv\Scripts\python.exe test_banking_system.py
```

### Test API with cURL
```powershell
curl -X GET http://127.0.0.1:8000/account/list
```

---

## 📈 OPERATION MATRIX

| Operation | Menu | Input Fields | Errors |
|-----------|------|--------------|--------|
| Create Account | 1 | ID, Name, Balance | ID exists |
| Update Account | 2 | ID, New Name | Account not found |
| Delete Account | 3 | ID | Account not found |
| Show Accounts | 4 | (none) | None |
| Deposit | 5 | Account ID, Amount | Account not found |
| Withdraw | 6 | Account ID, Amount | Insufficient balance |
| Transfer | 7 | From ID, To ID, Amount | Multiple errors |
| Transactions | 8 | (none) | None |
| Exit | 9 | (none) | None |

---

## 🎓 LEARNING PATH

### Beginner
1. Read `README.md`
2. Run `START.bat`
3. Test all 9 menu options
4. Make a deposit and withdrawal

### Intermediate
1. Read `PROFESSIONAL_GUIDE.md`
2. Study `api_server.py` code
3. Study `api_client.py` code
4. Run automated tests

### Advanced
1. Read `DEPLOYMENT_GUIDE.md`
2. Modify port settings
3. Create custom test cases
4. Extend API endpoints

---

## 📁 KEY FILES QUICK ACCESS

| File | Purpose | Open With |
|------|---------|-----------|
| `api_server.py` | Backend code | VS Code |
| `api_client.py` | Frontend code | VS Code |
| `test_banking_system.py` | Test suite | Terminal |
| `PROFESSIONAL_GUIDE.md` | Full guide | Notepad/Markdown |
| `DEPLOYMENT_GUIDE.md` | Deployment info | Notepad/Markdown |
| `PROJECT_SUMMARY.md` | Quick reference | Notepad/Markdown |
| `START.bat` | Quick launcher | Double-click |
| `requirements.txt` | Dependencies | VS Code |

---

## 🚀 PRODUCTION DEPLOYMENT CHECKLIST

- [ ] Read DEPLOYMENT_GUIDE.md
- [ ] Set up database (PostgreSQL)
- [ ] Add user authentication
- [ ] Enable HTTPS/SSL
- [ ] Configure rate limiting
- [ ] Set up logging/monitoring
- [ ] Create backup strategy
- [ ] Add unit tests
- [ ] Performance testing
- [ ] Security audit

---

## 🎯 SUCCESS INDICATORS

### ✅ System Working Correctly If:
- [x] Server starts without errors
- [x] Client menu displays properly
- [x] Can view all accounts
- [x] Deposit increases balance
- [x] Withdrawal decreases balance
- [x] Transfer moves money correctly
- [x] Transactions are logged
- [x] Error messages are clear

### ❌ Issues If:
- [ ] Server won't start
- [ ] Connection refused error
- [ ] Menu doesn't display
- [ ] Operations fail silently
- [ ] Balances incorrect
- [ ] Data not persisting

---

## 💬 SUPPORT RESOURCES

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Python Docs**: https://docs.python.org/
- **HTTP Status**: https://httpwg.org/specs/rfc7231.html
- **REST API**: https://restfulapi.net/

---

## 📝 NOTES

**Current Version**: 1.0.0
**Status**: Production Ready ✅
**Last Updated**: December 2, 2025

**Remember**: Always start server BEFORE client!

---

## 🎉 YOU'RE ALL SET!

```
┌───────────────────────────────┐
│  🚀 System Ready to Launch!   │
│                               │
│  Double-click: START.bat      │
│  Or: .\START.ps1              │
│                               │
│  Then enter choices 1-9       │
└───────────────────────────────┘
```

---

**Questions?** Check the documentation files or re-read this quick reference!
