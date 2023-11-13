# MailboxSendersList
Tool to retrieve and list all email addresses that have ever sent you an email for a specific mailbox.

## Configuration

Open the *config.yaml* file and fill in your IMAP server details and your credentials.

```yaml
host: "yourmailserver@server.com"
port: 993
mailbox: "INBOX"
username: "bob@the_bobs.com"
password: "my_very_secure_password"
outfile: "out.txt"
```

By default all email addresses from the inbox mailbox will be checked. If you want to check a specific mailbox change the `mailbox` property in the configuration.

## Running the script

To run the script Python is required.

### Using a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Using your default python environment

```bash
pip install -r requirements.txt
python3 main.py
```