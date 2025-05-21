def removeVirus(files_string):
    prefix = "PC Files: "

    if not files_string.startswith(prefix):
        print(f'output = "Invalid input format: String must start with \'{prefix}\'"')
        return

    files_list_str = files_string[len(prefix):].strip()

    if not files_list_str:
        print(f'output = "{prefix}Empty"')
        return

    files = [f.strip() for f in files_list_str.split(',')]

    safe_files = []

    for file_name in files:
        is_virus = False

        if "virus" in file_name and "antivirus" not in file_name and "notvirus" not in file_name:
            is_virus = True
        elif "malware" in file_name:
            is_virus = True

        if not is_virus:
            safe_files.append(file_name)

    if not safe_files:
        final_result = f"{prefix}Empty"
    else:
        final_result = prefix + ", ".join(safe_files)

    print(f'output = "{final_result}"')

#Example
#removeVirus("PC Files: spotifysetupvirus.exe, virus.exe, ntvirus.exe, virusitisnotithink.pdf dog.jpg")
