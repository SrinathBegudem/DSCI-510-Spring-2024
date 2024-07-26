# Lab 3
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def count_vowels(sentence: str) -> int:
    count = 0
    vowels = ["A","E","I","O","U"]
    for letter in sentence.upper():
        if letter in vowels:
            count = count + 1
    return count


# invoke the function with relevant args of your choice
print(count_vowels("This is a test sentence."))


# ----------------- Question 2 -----------------
def check_palindrome(word: str) -> bool:
    for i in range(len(word)//2):
        n = len(word)
        if word[i] != word[n-i-1]:
            return False
    return True



# invoke the function with relevant args of your choice
print(check_palindrome("madam"))


# ----------------- Question 3 -----------------
def email_id_filter(inbox_email_ids: list) -> (int, int):
    valid_email_count = 0
    spam_email_count = 0
    for email in inbox_email_ids:
        domain = email.split('@')[-1]
        if domain in ['usc.edu', 'isi.edu']:
            valid_email_count += 1
        else:
            spam_email_count += 1
    return valid_email_count, spam_email_count




# invoke the function with relevant args of your choice

inbox_email_ids = ["user1@usc.edu", "user2@yahoo.com", "user3@isi.edu"]

valid_emails, spam_emails = email_id_filter(inbox_email_ids)
print(f"Valid emails: {valid_emails}, Spam emails: {spam_emails}")

