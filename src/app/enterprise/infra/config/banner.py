def show_banner():
    with open('banner.txt', 'r') as file:
        banner = file.read()
        banner = banner.replace("{project_name}", "dev-files-ai")
        banner = banner.replace("{version}", "0.1.0")

    print("\n" + banner + "\n")