# 모듈 05 — Linux 기초

> **포커스**: 파일시스템·권한·핵심 명령어·파이프/리다이렉션·쉘 스크립트
> **예상 기간**: 1주
> **선행 모듈**: 03 개발 환경 & 터미널

데이터 엔지니어는 거의 매일 Linux 위에서 일합니다. 데이터 서버, 파이프라인 실행 환경,
클라우드 인스턴스, Docker 컨테이너 — 대부분 Linux입니다. 이 모듈에서는 **마우스 없이
터미널만으로** 파일을 다루고, 데이터를 가공하고, 반복 작업을 자동화하는 기본기를 익힙니다.

> 💡 Windows 사용자는 **WSL2 + Ubuntu**, macOS 사용자는 기본 터미널에서 실습하세요.

---

## 🎯 학습 목표
이 모듈을 마치면 다음을 할 수 있습니다.
- 파일시스템 구조를 이해하고 터미널로 자유롭게 이동·탐색한다
- 파일/디렉토리를 생성·복사·이동·삭제하고 내용을 확인한다
- `grep`, `wc`, `sort`, `uniq`, `awk` 등으로 텍스트 데이터를 가공한다
- **파이프(`|`)와 리다이렉션(`>`, `>>`)** 으로 명령어를 조합한다
- 파일 **권한(permission)** 을 읽고 변경한다 (`chmod`)
- 변수·반복문·조건문을 포함한 간단한 **쉘 스크립트**를 작성한다

---

## 📚 핵심 주제

### 1. 파일시스템 구조
Linux는 모든 것이 `/`(루트)에서 시작하는 하나의 트리입니다.

| 경로 | 의미 |
|------|------|
| `/` | 최상위 루트 |
| `/home/사용자` (`~`) | 사용자 홈 디렉토리 |
| `/etc` | 시스템 설정 파일 |
| `/var/log` | 로그 파일 (데이터 엔지니어가 자주 봄) |
| `/tmp` | 임시 파일 |

- **절대경로**: `/home/intern/data.csv` (루트부터 전체 경로)
- **상대경로**: `./data.csv`, `../other/` (현재 위치 기준)
- `.` = 현재 디렉토리, `..` = 상위 디렉토리, `~` = 홈

### 2. 이동 & 탐색
```bash
pwd              # 현재 위치 출력 (print working directory)
ls               # 파일 목록
ls -al           # 숨김파일 포함 + 상세정보 (권한/크기/날짜)
cd /var/log      # 디렉토리 이동
cd ..            # 상위로
cd ~             # 홈으로
```

### 3. 파일 & 디렉토리 조작
```bash
mkdir data            # 디렉토리 생성
mkdir -p a/b/c        # 중간 경로까지 한번에 생성
touch file.txt        # 빈 파일 생성 / 수정시각 갱신
cp src.csv dst.csv    # 복사
cp -r dir1 dir2       # 디렉토리 통째 복사
mv old.txt new.txt    # 이름변경 / 이동
rm file.txt           # 삭제
rm -r dir             # 디렉토리 삭제 (⚠️ 복구 불가, 신중히)
```
> ⚠️ `rm`은 휴지통이 없습니다. `rm -rf /` 같은 명령은 시스템을 파괴하니 절대 실행하지 마세요.

### 4. 파일 내용 보기
```bash
cat file.txt          # 전체 출력
less file.txt         # 페이지 단위로 보기 (q로 종료)
head -n 5 file.txt    # 앞 5줄
tail -n 5 file.txt    # 뒤 5줄
tail -f app.log       # 실시간으로 추가되는 로그 따라가기 (DE 필수)
wc -l file.txt        # 줄 수 세기
```

### 5. 검색: grep & find
```bash
grep "ERROR" app.log          # ERROR 포함 줄 찾기
grep -i "error" app.log       # 대소문자 무시
grep -c "ERROR" app.log       # 매칭된 줄 개수
grep -rn "TODO" .             # 현재 폴더 전체에서 재귀 검색 + 줄번호
find . -name "*.csv"          # 이름으로 파일 찾기
find . -type f -size +1M      # 1MB 초과 파일 찾기
```

### 6. 파이프(`|`)와 리다이렉션 ⭐
데이터 엔지니어링의 핵심 사고방식입니다. **작은 명령어를 조합**해 데이터를 흘려보냅니다.

- **파이프 `|`**: 앞 명령의 출력을 뒤 명령의 입력으로 전달
- **리다이렉션**: `>` 출력을 파일로 덮어쓰기, `>>` 파일에 이어붙이기

```bash
# access.log에서 상태코드별 빈도 Top 5
cat access.log | awk '{print $9}' | sort | uniq -c | sort -rn | head -5

# ERROR 줄 개수를 파일로 저장
grep -c "ERROR" app.log > error_count.txt

# 정렬 후 중복 제거
sort names.txt | uniq > unique_names.txt
```

자주 쓰는 가공 도구:
| 명령 | 역할 |
|------|------|
| `sort` | 정렬 (`-n` 숫자, `-r` 역순) |
| `uniq` | 인접 중복 제거 (`-c` 개수 세기) |
| `cut` | 열 잘라내기 (`-d',' -f1` CSV 1열) |
| `awk` | 열 단위 처리 (`'{print $2}'`) |
| `wc` | 줄/단어/문자 수 |

> 📌 `uniq`는 **정렬된** 입력에서만 제대로 동작합니다. 항상 `sort | uniq` 순서로 씁니다.

### 7. 권한(Permission)
`ls -l` 결과의 `-rwxr-xr--` 가 권한입니다.

```
-  rwx  r-x  r--
타입 소유자 그룹 기타사용자
```
- `r`(읽기)=4, `w`(쓰기)=2, `x`(실행)=1 → 합산해서 숫자로 표현
- `rwx`=7, `rw-`=6, `r-x`=5, `r--`=4

```bash
chmod 644 data.csv     # 소유자 rw, 그룹/기타 r
chmod +x script.sh     # 실행 권한 부여 (스크립트 실행 전 필수)
chmod 755 script.sh    # 소유자 rwx, 나머지 r-x
```

### 8. 쉘 스크립트 기초
반복 작업을 파일로 묶어 자동화합니다.

```bash
#!/bin/bash
# 첫 줄(shebang)은 이 파일을 bash로 실행하라는 의미

NAME="intern"            # 변수 (= 양옆 공백 없음에 주의)
echo "Hello, $NAME"      # 변수 사용은 $

# 조건문
if [ -f "data.csv" ]; then
  echo "파일이 있습니다"
else
  echo "파일이 없습니다"
fi

# 반복문
for f in *.csv; do
  echo "처리 중: $f"
  wc -l "$f"
done
```
실행:
```bash
chmod +x myscript.sh
./myscript.sh
```

---

## 🛠 실습 / 산출물
- `examples/`의 예제 스크립트를 직접 실행하며 명령어를 손에 익힙니다.
- `exercises/`에서 **웹 서버 접속 로그(access.log)를 분석하는 쉘 스크립트**를 완성합니다.
  - 총 요청 수, 상태코드별 통계, 에러(4xx/5xx) 수, 가장 많이 접속한 IP Top 5를 출력
- 산출물: 동작하는 `analyze_log.sh` 스크립트 + 실행 결과

---

## ✅ 완료 기준 (체크리스트)
- [ ] 절대/상대경로를 구분하고 `cd`로 원하는 위치에 이동할 수 있다
- [ ] 파일/디렉토리를 생성·복사·이동·삭제할 수 있다
- [ ] `grep`으로 로그에서 특정 패턴을 찾을 수 있다
- [ ] 파이프와 `sort | uniq -c`로 빈도를 집계할 수 있다
- [ ] `>` 와 `>>` 의 차이를 설명할 수 있다
- [ ] `chmod +x`로 스크립트에 실행 권한을 주고 실행할 수 있다
- [ ] 변수·반복문을 포함한 쉘 스크립트를 작성할 수 있다
- [ ] `exercises/`의 `analyze_log.sh`를 완성해 정상 출력을 얻었다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 강의 예제 스크립트 (직접 실행해보며 학습)
- `exercises/starter/` — 실습 시작 골격 (TODO 포함)
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [The Linux Command Line (무료 책)](https://linuxcommand.org/)
- [explainshell.com](https://explainshell.com/) — 명령어를 입력하면 각 옵션을 설명
- `man <명령어>` — 모든 명령어의 공식 매뉴얼 (예: `man grep`)
- 모듈 03(개발 환경 & 터미널), 모듈 12(Docker 기초)와 이어집니다.
