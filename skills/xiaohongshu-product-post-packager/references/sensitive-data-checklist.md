# Sensitive Data Checklist

Review screenshots before design work. Exclude or redact anything that could grant access, identify a private person, or expose a non-public account state.

## Always treat as sensitive

- Passwords, passcodes, API keys, tokens, private keys
- MFA / OTP codes
- Backup or recovery codes
- Login QR codes or device-link QR codes
- Email addresses, phone numbers, account handles, customer IDs
- Secret URLs, magic links, invitation links
- Billing details, invoices, usage balances, order IDs
- Browser tabs, notifications, chat previews, internal project names

## High-risk setup-flow screens

- Authenticator apps
- Password reset or identity verification pages
- Device pairing screens
- Admin consoles
- Account settings
- Mobile notification banners

## Decision rule

1. If the screenshot teaches nothing unique, drop it.
2. If the risky area is central to the screenshot, use a safer neighboring screenshot instead of editing.
3. If editing is necessary, remove enough context that the secret cannot be reconstructed.
4. Re-open final exports, not only source files, before handoff.
