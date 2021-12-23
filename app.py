import os
from shutil import copyfile
from tqdm import tqdm
import time



class CopyFile:

    def __init__(self, file_extentions, dest_file_path, current_dir_path="."):
        self.file_extentions = file_extentions
        self.file_path = current_dir_path
        self.dest_file_path = dest_file_path
        self.source_file_path = self.main()

    def main(self):

        try:
            print("\n>>> Bellow file extension are available: ")
            while True:
                print("\n")
                for i, ext in enumerate(self.file_extentions):
                    print(f"[{i}] {ext}")

                user_response = input(
                    "\n[INFO] press 'a' key to add custom file extensions.\n[INFO] press 'ENTER' key to continue \n\n>>> ")

                if user_response == "":
                    break

                elif user_response == "a":
                    custom_ext = input("\nEnter file extension like '.jpg' :\n\n>>> ")
                    if custom_ext == "":
                        break
                    if custom_ext not in self.file_extentions:
                        self.file_extentions.append(custom_ext)
                    else:
                        print("\n[INFO] extension is already exist")

            file_path_list = []
            for extension in self.file_extentions:
                for dirpath, dirnames, filenames in os.walk(self.file_path):
                    for filename in [f for f in filenames if f.endswith(f"{extension}")]:
                        file_path_list.append(os.path.join(dirpath, filename))
            return file_path_list

        except Exception as e:
            print(f"[ERROR] {e}")

    def copy(self):

        try:
            if not os.path.exists(self.dest_file_path):
                os.mkdir(self.dest_file_path)

            for file_path in tqdm(self.source_file_path, desc="File copy", total=len(self.source_file_path)):

                file_type = file_path.split("\\")[-1].split(".")[-1]
                destination_folder =  os.path.join(self.dest_file_path, file_type)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    destination_path = os.path.join(
                    destination_folder, file_path.split("\\")[-1])
                else:
                    destination_path = os.path.join(
                    destination_folder, file_path.split("\\")[-1])

                copyfile(file_path, destination_path)

            print("\n[SUCCESS] All files are copied successfully")

            return

        except Exception as e:
            print(f"[ERROR] {e}")
            return


if __name__ == '__main__':
    # taget file extension
    file_extentions = [".jpeg", ".jpg", ".xbm", ".bmp", ".png", ".JPG"]

    root_path = input("\n[OPTIONAL] Enter your target folder path: \n\n>>> ")
    destination_path = input("\n[OPTIONAL] Enter your destination folder folder path: \n\n>>> ")

    if root_path == "":
        root_path = "./"
    elif destination_path == "":
        destination_path = ".\out_put"

    # make object of copyfile class
    cp = CopyFile(file_extentions, destination_path, root_path)
    # copy file from source path to destination path
    cp.copy()
