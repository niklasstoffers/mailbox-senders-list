import yaml
import re
import progressbar
from imaplib import IMAP4_SSL

with open("config.yaml") as f:
    config = yaml.safe_load(f)
    senders = set()

    with IMAP4_SSL(host = config["host"], port = config["port"]) as M:
        print("Logging in...")
        M.login(user = config["username"], password = config["password"])
        print("Selecting mailbox...")
        M.select(mailbox=config["mailbox"])
        
        res, data = M.search(None, "ALL")
        id_list = data[0].split()

        num_ids = len(id_list)
        current_id = 1

        print("Collecting senders from mailbox...")
        with progressbar.ProgressBar(max_value=num_ids) as bar:
            for id in id_list:
                res, maildata = M.fetch(id, "(BODY[HEADER.FIELDS (FROM)])")
            
                sender_header = maildata[0][1].decode("utf-8")
                sender_reg = re.search('([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', sender_header)

                sender_mail = sender_reg.group(1)
                senders.add(sender_mail)

                bar.update(current_id)
                current_id += 1

        print("Logging out...")
        M.logout()

    print("Writing output...")
    sender_list = list(senders)
    with open(config["outfile"], 'w') as outfile:
        outfile.write("\n".join(sender_list))
    print("DONE")