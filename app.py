import os
from shutil import copyfile
from tqdm import tqdm


class CopyFile:

    def __init__(self, file_extentions, dest_file_path, current_dir_path="."):
        self.file_extentions = file_extentions
        self.file_path = current_dir_path
        self.dest_file_path = dest_file_path
        self.source_file_path = self.main()

    def main(self):

        try:
            print("Main function clled now...")
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
            print("copyfile function called now...")
            if not os.path.exists(self.dest_file_path):
                os.mkdir(self.dest_file_path)

            for file_path in tqdm(self.source_file_path, desc="File copy", total=len(self.source_file_path)):
                destination_path = os.path.join(
                    self.dest_file_path, file_path.split("\\")[-1])
                copyfile(file_path, destination_path)

            print("All files are copied successfully")

            return

        except Exception as e:
            print(f"[ERROR] {e}")
            return


if __name__ == '__main__':
    # taget file extension
    file_extentions = [".jpeg", ".jpg", ".xbm", ".bmp", ".png", ".JPG"]

    # define file path
    root_path = input("Enter your folder path: \n")  # default root path is "./"
    destination_path = ".\out_put"

    # make object of copyfile class
    cp = CopyFile(file_extentions, destination_path, root_path)

    # copy file from source path to destination path
    cp.copy()  
