import os
import datetime
import re

class DownloadFolderUtility:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def validate_folder(self):
        # 경로 확인(존재 경로, 폴더인지)
        if os.path.isdir(self.folder_path):
            return True
        else:
            return False
        
    def get_files(self):
        # 파일 목록 리턴
        return [os.path.join(curDir, f) for curDir, dirs, files in os.walk(self.folder_path) for f in files]

    def has_date_format(self, file_name):
        # 날짜 형식 써놯는지 확인
        pattern = r'\d{4}-\d{2}-\d{2}'
        return bool(re.search(pattern, file_name))

    def format_timestamp(self, timestamp):
        # 날짜 사람이 알아먹게 하기
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

    def rename_file_with_mtime(self, file_path):
        # 수정일 붙히기
        base_name = os.path.splitext(file_path)[0]
        extension = os.path.splitext(file_path)[1]

        if self.has_date_format(base_name):
            base_name = re.sub(r"_\d{4}-\d{2}-\d{2}", "", base_name)

        new_path = base_name + "_" + self.format_timestamp(os.path.getmtime(file_path)) + extension
        
        try:
            os.rename(file_path, new_path)
        except FileExistsError:
            print(f"A file already exists with the name to be replaced: {new_path}\n"\
                  "(이미 바꿀 이름의 파일이 존재함: {new_path})")
        except Exception as e:
            print(f"Another Error Occurred: {e}\n"\
                  "(또 다른 에러 발생:{e})")

    def process(self):
        # 돌기
        if not self.validate_folder():
            print("Invalid path.\n" \
            "(잘못된 경로입니다.)")
            return
        else:
            for file_path in self.get_files():
                self.rename_file_with_mtime(file_path)

download_folder_utility = DownloadFolderUtility(
    input("Please enter the path of the folder\n" \
    "(폴더의 경로를 입력해주세요)\n" \
    " > ")
)
download_folder_utility.process()