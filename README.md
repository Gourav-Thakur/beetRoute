# 🛠 Django REST Complaint Management System

This project is a role-based complaint tracking system with:
- Two roles: **CRO** (complaint submitter) and **ASM** (complaint reviewer)
- CRO can add complaints (retailer name, customer name, pincode)
- ASM can view all complaints and update `feedback_status` (pending/approved/rejected)
- ASM gets alerts every 10 seconds for pending complaints
- Includes a basic HTML interface + Django REST API backend

---

## 📁 Project Setup

### 1. Clone & Set Up Virtual Environment

```bash
git clone <your-repo-url>
cd complaint_project
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
# Follow prompts: username, email, password

python manage.py runserver
```

5. Access Admin Panel
Open:
📍 http://127.0.0.1:8000/admin/

Login using the superuser credentials.

a. Create CRO User:
Go to Users → Add user

Fill in username, password

After saving, edit user and set role = cro

b. Create ASM User:
Same steps

Set role = asm

📝 Complaint Interface:
📍 http://127.0.0.1:8000/complaints/

CRO View:

Can add new complaints using a form

Can view own submitted complaints

feedback_status is read-only

ASM View:

Can view all complaints

Can only edit feedback_status field via dropdown

Alerts every 10 seconds if any complaints are still pending

📡 API Endpoints (Session Auth)
Method	Endpoint	Description
GET	/complaints/api/	List complaints
POST	/complaints/api/	Create complaint (CRO only)
PATCH	/complaints/api/<id>/	Update status (ASM only)
GET	/complaints/api/pending_exists/	Check for pending complaints

✅ Role Summary
Role	Permissions
CRO	Add/view own complaints, cannot edit status
ASM	View all, update feedback_status, gets alert every 10s

✅ Useful URLs
Purpose	URL
Admin Panel	http://127.0.0.1:8000/admin/
Login	http://127.0.0.1:8000/accounts/login/
Complaints Page	http://127.0.0.1:8000/complaints/

