# MVTeaches Owner Demo

Static customer-facing simulator for the MVTeaches MVP.

- Open `index.html` for the role picker and guided tour.
- Direct portal files open their matching simulated student page.
- No backend, database, network calls, CDN, secrets, or real integrations.
- All data is fictional and stored locally in the browser via localStorage.

Regenerate the portal page files after editing `index.html`:

```powershell
python build_pages.py
```
