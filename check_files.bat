@echo off
echo ============================================================
echo CHECKING YOUR GOOGLE CLOUD STORAGE
echo ============================================================
echo.

echo Checking if files are uploaded...
echo.

gsutil ls gs://krishna-dotted-music-460617-k2-vertex-pipeline-bucket/datasets/

echo.
echo ============================================================
echo If you see both files above, you're ready!
echo If not, run: upload_files.bat
echo ============================================================
pause
