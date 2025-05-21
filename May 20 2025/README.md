# `removeVirus` Function

This `README.md` explains the Python function `removeVirus`, which simulates the process of finding and "removing" specific types of files from a list based on predefined "virus" criteria.

---

## What it Does

The `removeVirus` function takes a single string as input, representing a list of files on a "PC". It then filters this list, identifying and conceptually "removing" files that are considered "viruses" or "malware" according to specific rules. The function then prints the resulting "clean" list of files.

---

## How it Works (Virus Detection Logic)

The function identifies a file as a "virus" if its name contains:

* The substring **"virus"**, **unless** it also contains **"antivirus"** or **"notvirus"**. This means `virus.exe` is a virus, but `antivirus.exe` and `notvirus.exe` are not.
* The substring **"malware"**.

Files that do not meet these criteria are considered "safe" and are kept in the list.

---

## Usage

To use the function, simply call `removeVirus()` with a string formatted as `"PC Files: file1.ext, file2.ext, ..."`.

Output
The function prints its output directly to the console in the format output = "PC Files: ...".

If "safe" files remain, they are listed, separated by commas.

If no "safe" files remain after the removal process (meaning all files were identified as viruses or the initial list was empty), the output will be output = "PC Files: Empty".

Examples
Here are the examples demonstrating the function's behavior:
```
# Example 1: A virus file is removed
removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
# Expected Output: output = "PC Files: spotifysetup.exe, dog.jpg"

# Example 2: Malware and dangerous virus files are removed, antivirus is kept
removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
# Expected Output: output = "PC Files: antivirus.exe, cat.pdf"

# Example 3: No viruses found
removeVirus("PC Files: notvirus.exe, funnycat.gif")
# Expected Output: output = "PC Files: notvirus.exe, funnycat.gif"

# Example 4: All files are viruses
removeVirus("PC Files: myvirus.exe, anothermalware.txt")
# Expected Output: output = "PC Files: Empty"

# Example 5: Empty initial list
removeVirus("PC Files: ")
# Expected Output: output = "PC Files: Empty"
```
