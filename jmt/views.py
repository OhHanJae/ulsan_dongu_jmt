from django.shortcuts import render
import csv, sqlite3
import pandas as pd
from django.http import JsonResponse

def loadDate(request):
    # CSV 파일을 DataFrame으로 읽어옵니다.
    csv_file_path = 'C:/Users/gram/Desktop/JMT/config/ulsan.csv'  # 여기서 'your_csv_file.csv'에 파일 경로를 입력하세요.
    df = pd.read_csv(csv_file_path, header=None, encoding='CP949')

    # SQLite 데이터베이스에 연결합니다.
    db_file_path = 'C:/Users/gram/Desktop/JMT/config/db.sqlite3'  # 여기서 'your_database_file.sqlite3'에 데이터베이스 파일 경로를 입력하세요.
    con = sqlite3.connect(db_file_path)
    cur = con.cursor()

    # 테이블이 존재하지 않는 경우, 테이블을 생성합니다.
    cur.execute("CREATE TABLE IF NOT EXISTS ulsan_dongu (id INTEGER PRIMARY KEY, name TEXT, adress TEXT);")

    # DataFrame의 데이터를 데이터베이스 테이블에 삽입합니다.
    for index, row in df.iterrows():
        data = (row[0], row[1])
        cur.execute("INSERT INTO unsan_dongu (name, adress) VALUES (?, ?);", data)

    # 변경 사항을 커밋하고 데이터베이스 연결을 닫습니다.
    con.commit()
    con.close()

    print("데이터가 성공적으로 데이터베이스에 저장되었습니다.")

# Create your views here.
def index(request):
    return render(request, "base.html")

def result(request):

    towns = request.GET.getlist("towns", 0)
    num = request.GET.get("num", 0)

    db = "./db.sqlite3"
    conn = sqlite3.connect(db, isolation_level=None)
    read_data = list()

    with conn:
        cursor = conn.cursor()

        if towns[0] == 'all':
                sql = f"SELECT name, adress FROM ulsan_dongu ORDER BY RANDOM() LIMIT {num};"    
        else:
            mapping = {
                '1' : "대송동",
                '2' : "동부동",
                '3' : "방어동",
                '4' : "서부동",
                '5' : "일산동",
                '6' : "전하동",
                '7' : "전하1동",
                '8' : "전하2동",
                '9' : "주전동",
                '10' : "화정동",
            }
            wtf = ', '.join([f'"{mapping[x]}"' for x in towns])
            sql = f"""SELECT name, adress FROM ulsan_dongu 
                    WHERE town IN({wtf}) 
                    ORDER BY RANDOM() LIMIT {num};"""  
            
    cursor.execute(sql)
    result = cursor.fetchall()
                
    for row in result:
        obj = {'name': row[0], 'adress': row[1]}
        read_data.append(obj)

    context = {"read_data" : read_data}

    return JsonResponse(context)