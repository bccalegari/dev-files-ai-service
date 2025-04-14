def show_banner():
    try :
        with open('version.txt', 'r') as file:
            version = file.read().strip()
    except Exception as e :
        version = "Error reading version file"

    with open('banner.txt', 'r') as file:
        banner = file.read()
        banner = banner.replace("{project_name}", "dev-files-ai")
        banner = banner.replace("{version}", version)

    print("\n" + banner + "\n")