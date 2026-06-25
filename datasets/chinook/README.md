# Chinook — 디지털 음악 스토어

iTunes 풍의 디지털 음악 판매 데이터입니다. 아티스트·앨범·트랙·고객·직원·인보이스로 이어지는 깔끔한 관계형 스키마라 **JOIN과 집계 연습에 가장 무난한 입문용 데이터셋**입니다.

## 출처 / 라이선스
- **출처**: [lerocha/chinook-database](https://github.com/lerocha/chinook-database) (`Chinook_PostgreSql.sql`)
- **라이선스**: MIT (Copyright © Luis Rocha) — 자유 사용
- 원본을 커밋하지 않고 적재 시 내려받습니다(약 0.6MB).

## 규모 / 주요 테이블
- 11개 테이블, 트랙 약 3,500 / 인보이스 약 400
- `artist` → `album` → `track`, `customer` → `invoice` → `invoice_line` ← `track`, `employee`(셀프 조인: 매니저)
- 모든 식별자는 `*_id`, 테이블/컬럼은 소문자 스네이크케이스

## 적재
```bash
./load.sh          # DB 'chinook' 자동 생성/재생성 후 적재
psql -d chinook    # 접속
```
> 이 덤프는 스스로 `DROP/CREATE DATABASE chinook`를 수행하므로 유지보수용 `postgres` DB에 접속해 실행됩니다.

## 연습 아이디어
- 장르별 트랙 수 / 평균 길이 (`track` ⨝ `genre`)
- 고객별 누적 구매액 Top 10 (`customer` ⨝ `invoice`)
- 직원-매니저 셀프 조인 (`employee.reports_to`)
- 국가별 매출, 가장 많이 팔린 트랙(윈도우 함수로 순위)
