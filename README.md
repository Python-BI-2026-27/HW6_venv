< your solution here >
1. Use Windows 11
2. Use Positron Version: 2026.10.2

3. Download the installer for Windows, Miniforge3-Windows-x86_64.exe. (https://conda-forge.org/download/)
   - Check the box "Add Miniforge3 to my PATH environment variable." Don't be alarmed by the red text.

4. Positron restart
5. Rediscover Positron
6. Enter the check command into the terminal: mamba --version
   - a version of the program (something like "2.9.0") should appear

7. install Python 3.14: mamba create -n pain_env python=3.14 -c conda-forge -y
8. install pandas, pyarrow, opencv, google: mamba run -n pain_env pip install pandas pyarrow opencv-python google-auth biopython

9. follow the link: https://github.com/biopython/DIST/blob/670df037ad99a51706fb1cf2da379e25b6080246/biopython-1.81.zip
10. download biopython-1.81.zip
11. Download two (pairwise2 и cpairwise2module.c) files from the 'Bio' folder within this ZIP archive.
12. Place these two files in the folder: ~miniforge3\envs\pain_env\Lib\site-packages\Bio\
    !!!with replacement!!!

13. follow the link: https://github.com/biopython/DIST/blob/670df037ad99a51706fb1cf2da379e25b6080246/biopython-1.79.zip
14. download biopython-1.79.zip
15. download the folder SubsMat
16. add folder to ~miniforge3\envs\pain_env\Lib\site-packages\Bio\

17. Let's comment out the line in the source file (pain.py) #pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})       #F***ing Joe from Texas used a set as an index.
18. we’ll type the magic words into the terminal: mamba run -n pain_env python pain.py
19. we shall see: ✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤



![My Rest](./in_pool.jpg.jpg)
My friends and I rented a swimming pool for the night.