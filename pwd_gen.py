import string
import random
import webbrowser


def gen_pwd(length=24, use_uppercase=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    pwd = "".join(random.choice(chars) for _ in range(length))
    return pwd


def gen_multiple_pwd(
    num_pwd, length=24, use_uppercase=True, use_digits=True, use_special=True
):
    pwds = []
    for _ in range(num_pwd):
        pwds.append(gen_pwd(length, use_uppercase, use_digits, use_special))
    return pwds


def save_pwds_to_file(pwds, filename):
    with open(filename, "w") as file:
        for pwd in pwds:
            file.write(pwd + "\n")


def main():
    print("Password Generator")
    num_pwd = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_special = input("Include special characters? (y/n): ").lower() == "y"

    pwds = gen_multiple_pwd(num_pwd, length, use_uppercase, use_digits, use_special)

    print("\nGenerated passwords:")
    for i, pwd in enumerate(pwds, start=1):
        print(f"Password {i}: {pwd}")

    save_to_file = (
        input("Do you want to save your passwords to a file? (y/n): ").lower() == "y"
    )
    if save_to_file:
        while True:
            filename = input(
                "Enter the filename to save passwords (e.g., passwords.txt): "
            )
            if filename.endswith(".txt"):
                save_pwds_to_file(pwds, filename)
                print(f"Passwords saved to {filename}")
                webbrowser.open(filename)
                break
            else:
                print("Please enter a valid file name with the '.txt' extension.")


if __name__ == "__main__":
    main()
