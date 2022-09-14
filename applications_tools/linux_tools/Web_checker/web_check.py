import requests


def website_cheker():
    check_response = requests.get(str(input("give me a site to check(with the https://): ")))
    print("Report")
    if check_response.status_code == 200:
        print("    Web site exists")
    else:
        print("    Web site does not exists")
    nothing = input("press enter to exit: ")
    print("\n\n")
