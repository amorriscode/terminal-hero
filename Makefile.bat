@echo off

IF "%1%"=="" (
    echo "Run Makefile.bat init"
    exit
) ELSE IF "%1%"=="create-env" (
    python3 -m venv venv
) ELSE IF "%1%"=="install" (
    IF NOT EXIST .\venv (
        python3 -m venv venv
    )
    .\venv\Scripts\activate.bat
    pip install -r requirements.txt
) ELSE IF "%1%"=="init" (
    .\Makefile.bat create-env
    .\Makefile.bat install
) ELSE IF "%1%"=="clean" (
    rmdir /s /q venv
    del /s "*.pyc"
)    
