from pathlib import Path
import subprocess
import diff_days
import diff_days_from_white_paper
import email_sender
import json_reader as jr

def write_file(filename, options, data):
    with open(filename, options) as f:
        f.write(data)
        f.close()

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        return lines

####### Main
def main():
    d = jr.get_data()
    path = Path('./sended_emails.txt')
    diff = diff_days.days()
    day_zero = diff_days_from_white_paper.days()
    
    #Check if at least one beat was registered
    if diff == day_zero:
        to_email=str(d["emails"]["your"])
        subject="Missing first beat"
        content=str(d["email_messages"]["missing_first_beat"])
        email_sender.main(to_email, subject, content)          
        if str(d["send_messages_on_nostr"]) == "yes":
            subprocess.run(["./post-to-nostr.sh",str(d["email_messages"]["missing_first_beat"])])
        exit
    
    # Time intervals to send a e-mail
    # Remind you to hit the script
    if diff >= 2 and diff < 30:
        to_email=str(d["emails"]["your"])
        subject=str(d["email_messages"]["ordinary"]["subject"])+str(diff)+" dias"
        content=str(d["email_messages"]["ordinary"]["content"])+str(diff)+str(d["email_messages"]["ordinary"]["content_cmp"])
        email_sender.main(to_email, subject, content)          
        if str(d["send_messages_on_nostr"]) == "yes":
            subprocess.run(["./post-to-nostr.sh",str(d["nostr_notes"]["ordinary"]["content"])+str(diff)+str(d["nostr_notes"]["ordinary"]["content_cmp"])])

    # first e-mail with instructions
    if diff >= 30 and diff < 90:
        to_email=str(d["emails"]["your"])+","+str(d["emails"]["person_will_receive_access"])
        subject=str(d["email_messages"]["first_email"]["subject"])
        content=str(d["email_messages"]["first_email"]["content"])+str(d["email_messages"]["first_email"]["content_cmp"])
        count = '1\n'
        if path.is_file():
            lines = read_file('sended_emails.txt')
            if len(lines) < 1:
                #Send e-mail with message: the password to open testment file is ########
                email_sender.main(to_email, subject, content)
                write_file('sended_emails.txt', 'a+', count)
            else:
                if lines[0] != count:
                    #Send e-mail with message: the password to open testment file is ########
                    email_sender.main(to_email, subject, content)
                    write_file('sended_emails.txt', 'a+', count)
                    if str(d["send_messages_on_nostr"]) == "yes":
                        subprocess.run(["./post-to-nostr.sh",str(d["nostr_notes"]["first_note"]["content"])+str(diff)+str(d["nostr_notes"]["first_note"]["content_cmp"])])
        else:
            email_sender.main(to_email, subject, content)
            write_file('sended_emails.txt', 'a+', count)

    # second e-mail with instructions
    if diff >= 90 and diff < 180:
        to_email=str(d["emails"]["your"])+","+str(d["emails"]["person_will_receive_access"])
        subject=str(d["email_messages"]["second_email"]["subject"])
        content=str(d["email_messages"]["second_email"]["content"])+str(d["email_messages"]["second_email"]["content_cmp"])
        count = '2\n'
        if path.is_file():
            lines = read_file('sended_emails.txt')
            if len(lines) < 2:
                #Send e-mail with message: the password to open seed file is ########
                email_sender.main(to_email, subject, content)
                write_file('sended_emails.txt', 'a+', count)
            else:
                if lines[1] != count:
                    #Send e-mail with message: the password to open seed file is ########
                    email_sender.main(to_email, subject, content)
                    write_file('sended_emails.txt', 'a+', count)
                    if str(d["send_messages_on_nostr"]) == "yes":
                        subprocess.run(["./post-to-nostr.sh",str(d["nostr_notes"]["first_note"]["content"])+str(diff)+str(d["nostr_notes"]["second_note"]["content_cmp"])])
        else:
            email_sender.main(to_email, subject, content)
            write_file('sended_emails.txt', 'a+', count)
    # last e-mail with instructions
    if diff >= 180 and diff < 360:
        to_email=str(d["emails"]["your"])+","+str(d["emails"]["person_will_receive_access"])
        subject=str(d["email_messages"]["final_email"]["subject"])
        content=str(d["email_messages"]["final_email"]["content"])+str(d["email_messages"]["final_email"]["content_cmp"])
        count = '3\n'
        if path.is_file():
            lines = read_file('sended_emails.txt')
            if len(lines) < 3:
                #Send e-mail with message: the password to open passphrase file is ########
                email_sender.main(to_email, subject, content)
                write_file('sended_emails.txt', 'a+', count)
            else:
                if lines[2] != count:
                    #Send e-mail with message: the password to open passphrase file is ########
                    email_sender.main(to_email, subject, content)
                    write_file('sended_emails.txt', 'a+', count)
                    if str(d["send_messages_on_nostr"]) == "yes":
                        subprocess.run(["./post-to-nostr.sh",str(d["nostr_notes"]["final_note"]["content"])+str(diff)+str(d["nostr_notes"]["final_note"]["content_cmp"])])
        else:
            email_sender.main(to_email, subject, content)
            write_file('sended_emails.txt', 'a+', count)
if __name__ == "__main__":
    main()
