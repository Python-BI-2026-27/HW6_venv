## Исходный код был написан под Python 3.14+, из-за чего возникали ошибки совместимости в более старых окружениях
Для успешного запуска в окружениях с более ранней версией Python в код необходимо внести следующие изменения:
1) Удалить строку импорта annotationlib.
2) Обновить Biopython. В исходном коде указан устаревший модуль Bio.SubsMat, его необходимо заменить на Bio.Align.substitution_matrices, а матрицу BLOSUM62 загрузить через .load("BLOSUM62").
3) Исправить индекс в Pandas с ({1, 2, 3, 4}) на упорядоченный список ([1, 2, 3, 4]), так как Pandas запрещает использовать неперечисляемые множества в качестве индексов.
Исправленный код приведен в файле pain.ipynb

## Отчет об отдыхе на выходных:

Концерт группы Ravanna 

<img width="2388" height="1080" alt="Videoframe_20261104_004219_com huawei himovie overseas" src="https://github.com/user-attachments/assets/d7d85a21-0c89-443b-a77b-38aaab8a63ee" />

Участие в забеге на 10км

<img width="1220" height="2700" alt="Screenshot_20261105_104017_com huami watch hmwatchmanager" src="https://github.com/user-attachments/assets/b0b7b3ca-3098-48a5-b35e-cf08e2b2aa69" />
<img width="2560" height="1707" alt="IMG_20261105_094932" src="https://github.com/user-attachments/assets/f0ab6268-6f9c-4595-bdc5-bda1f991e9fb" />
<img width="960" height="1280" alt="IMG_20261104_165731_785_edit_90483480516106" src="https://github.com/user-attachments/assets/ba71ae69-250e-4390-a7ad-de097f7e6334" />



