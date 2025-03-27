import os

def main():
    path = input("Enter the directory path like 'E:/images': ").strip()
    base_name = input("Enter the base name like 'images': ").strip()

    if not os.path.isdir(path):
        print(f"Error: The directory '{path}' does not exist.")
        return

    if not path.endswith(os.sep):
        path += os.sep

    for i, filename in enumerate(os.listdir(path)):
        if os.path.isfile(os.path.join(path, filename)):
            new_name = f"{base_name}{i}{os.path.splitext(filename)[1]}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
            print(f"Renamed: {filename} -> {new_name}")

    print("All files have been renamed.")

if __name__ == "__main__":
    main()
