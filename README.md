# File Date Renamer

This is a Python script that automatically places the file modification date after the file name.  
> (파일 수정 날짜를 파일명 뒤에 자동으로 붙여주는 파이썬 스크립트입니다.)

## Prerequisites (사전 준비물)
- Python 3.x or higher
- No external libraries required (Standard library only!)
> (외부 라이브러리 불필요! 표준 라이브러리만 사용함)

## Features (기능)
- File Revision Date (YYYY-MM-DD) Automatic tagging
> (파일 수정 날짜(YYYY-MM-DD) 자동 태깅)
- Update date for already tagged file names  
> (이미 태깅된 파일명은 날짜 갱신)
- Recursively processing subfolders  
> (하위 폴더까지 재귀적으로 처리)
- Includes duplicate file processing (exception processing)  
> (중복 파일 처리(예외 처리) 포함)

## How it works (작동 원리)
- It scans the target folder and its subfolders.
- It identifies the last modified date of each file.
- It renames the file to `original_name_YYYY-MM-DD.ext`.
- If the file is already tagged, it updates the date instead of creating duplicates.  
> (작동 원리: 폴더 내 파일을 스캔하여 수정일을 추출하고, 날짜를 파일명 뒤에 붙여 이름 변경. 기존 태그가 있으면 업데이트함.)
## How to use (사용법)
1. Run 'rename_tool.py' in an environment where Python is installed.  
> (파이썬이 설치된 환경에서 `rename_tool.py`를 실행합니다.)
2. Enter the path to the folder you want to organize and clean up all the files in that folder.  
> (정리할 폴더의 경로를 입력하면 해당 폴더 내 모든 파일을 정리합니다.)

## License (라이선스)
This project is subject to the MIT license.  
> (이 프로젝트는 MIT 라이선스를 따릅니다.)

## Issues (이슈 제보)
Please let me know via the [Issues](https://github.com/dohyeon42/file-date-renamer/issues) tab for bugs or improvements!  
> (버그나 개선 사항은 [이슈](https://github.com/dohyeon42/file-date-renamer/issues) 탭을 통해 알려주세요!)

Note: This documentation contains machine-translated text.  
> (참고: 이 문서는 기계 번역된 내용을 포함하고 있습니다.)
