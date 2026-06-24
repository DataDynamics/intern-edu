# 모듈 04 — 퀴즈 정답

1. **절대경로**는 루트(`/`)부터 시작하는 전체 경로(`/home/intern/data.csv`), **상대경로**는 현재 위치 기준 경로(`./data.csv`, `../data/`).
2. `.` 현재 디렉토리, `..` 상위 디렉토리, `~` 사용자 홈 디렉토리.
3. `>` 는 파일을 **새로 덮어쓰기**, `>>` 는 파일 **끝에 이어붙이기**.
4. `uniq`는 **인접한** 중복만 처리하므로, 먼저 `sort`로 같은 값을 모아야 정확히 집계된다.
5. `rwx`(7) `r-x`(5) `r--`(4) → **754**.

6. `grep -c "ERROR" app.log`
7. `find . -name "*.csv"`
8. `awk '{print $9}' access.log | sort | uniq -c | sort -rn`
9.
   ```bash
   chmod +x script.sh
   ./script.sh
   ```
10. `sort names.txt | uniq > unique.txt`

11. **shebang(셔뱅)**. 이 스크립트를 어떤 인터프리터(`/bin/bash`)로 실행할지 OS에 알려준다.
12.
    ```bash
    for f in *.csv; do
      echo "$f: $(wc -l < "$f") 줄"
    done
    ```
