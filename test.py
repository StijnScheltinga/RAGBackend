text = """
# Silverthorne Legal Group – Associate Attorney Onboarding Guide (2025)

This onboarding guide applies to all new associate attorneys at Silverthorne Legal Group (“SLG”).

## 1. First Week – Essentials

During the first week, new associates must:

1. Set up accounts for:
   - SLG Email
   - Document Management System (DMS)
   - Timekeeping and Billing System
   - Legal Research Platform (LexiSearch)
2. Attend mandatory trainings:
   - Ethics and Confidentiality (1 hour)
   - Timekeeping Best Practices (45 minutes)
   - Conflict-Check Training (30 minutes)
3. Shadow a senior attorney in at least one client meeting.

## 2. First Month – Integration

During the first month, associates should:

- Review the **Client Intake Policy (2025)**.
- Observe at least **one deposition or hearing**.
- Draft:
  - One research memo.
  - One client communication under supervision.
- Submit all billable time by **9:00 AM each weekday**.

A check-in with the Practice Group Leader is required at the end of Week 4.

## 3. First 90 Days – Competency Goals

By day 90, associates are expected to:

- Perform conflict checks independently.
- Open a matter in the Practice Management System (with oversight).
- Demonstrate understanding of:
  - Annual leave policy
  - Sick leave policy
  - CLE budget rules
- Assist in at least **two client matters**.

## 4. Evaluation

The probationary review (90 days) assesses:

- Legal analysis
- Writing quality
- Responsiveness to clients
- Use of the DMS
- Adherence to SLG procedures
"""

text = text.casefold()

with open("test.txt", "w") as f:
	f.write(text)