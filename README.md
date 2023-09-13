# 2023-translator-back
- Web application that provides translation services from Korean to English   
- Developed with python, FastAPI, MySQL   

## ❣️ Team

Hi, we are **'All for One'** team! 🤗
<br>
<br>
We gave lectures for BUET (Bangladesh University of Engineering and Technology) students 🇧🇩
<br>
<br>
Supported by **NIA (National Information Society Agency, 한국지능정보사회진흥원)**
<br>
![image](https://github.com/KIV-All-For-One/Lecture/assets/53294075/22bf88f4-8b19-4e69-81b6-0812d39d3af4) ![image](https://github.com/KIV-All-For-One/Lecture/assets/53294075/ccd2da49-6353-4eb3-a803-19581c658ee0)


## 📅 Periods
21 Aug - 30 Aug 2023

## 👥 Members
👑 Kangsan Kim (Leader) : Lead our project / Cloud computing   
🤖 [Judy Choi](https://github.com/judy-choi) : AI, Backend   
🥛 [Mihyeon Byeon](https://github.com/cocoball200) : Frontend   
❤️ [Jini Moon](https://github.com/JiniMoon62) : Data Science  

## 🧑🏻‍🏫 Backend Lecture
### Day 5
- Backend API, RDBMS
- Architecture with FastAPI
- Model serving

### Run
#### 1. Set SQLALCHEMY_DATABASE_URL
```
export SQLALCHEMY_DATABASE_URL=mysql+pymysql://root:"[PASSWD]"@[MySQL DB IP]:3306/nmt?charset=utf8
```

#### 2. Run
```
gunicorn -k uvicorn.workers.UvicornWorker main:app
```
or if you want run 4 workers,
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Example
<img src="https://github.com/Judy-Choi/2023-translator-back/assets/53294075/672ffd39-56f2-4ad0-8fa5-7c5badf735d1" width=700>

<img src="https://github.com/Judy-Choi/2023-translator-back/assets/53294075/906a6a4a-fedd-4fd5-be50-ea1e081d38e6" width=700>
