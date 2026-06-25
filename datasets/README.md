# 실습용 공유 데이터셋

두 트랙이 공유하는 샘플 데이터를 모아둡니다.
- 대학생 트랙: **분석** 대상으로 사용 (SQL 모듈 10·11, pandas/EDA 모듈 13·14)
- 졸업생 트랙: **파이프라인** 입력으로 사용

> 모든 데이터셋은 모듈 10·11과 같은 **PostgreSQL**에 적재합니다. PostgreSQL이 아직 없다면 [../setup/postgresql-setup.md](../setup/postgresql-setup.md)를 먼저 보세요.

## 규칙
- 각 데이터셋은 하위 폴더 + README로 **출처/라이선스/스키마**를 명시
- 대용량 원본은 커밋하지 말고 다운로드/적재 스크립트(`load.sh`)로 제공
- 작은 합성 샘플은 CSV를 그대로 커밋해 **오프라인에서도** 바로 쓰게 함

## 지금 들어 있는 데이터셋

| 폴더 | 주제 | 규모 | 방식 | 난이도 |
|------|------|------|------|--------|
| [`shop/`](shop/) | 합성 e-커머스 (customers/products/orders/order_items) | 작음 (커밋됨) | `./load.sh` 또는 `psql -f load.sql` | ★ 입문 |
| [`chinook/`](chinook/) | 디지털 음악 스토어 | 0.6MB | `./load.sh` (다운로드) | ★ 입문 |
| [`northwind/`](northwind/) | 고전 e-커머스/ERP | 0.35MB | `./load.sh` (다운로드) | ★★ 중급 |
| [`pagila/`](pagila/) | DVD 대여점 (Sakila의 PostgreSQL 포트) | ~3.3MB | `./load.sh` (다운로드) | ★★ 중급 |

- **모듈 10·11을 갓 마쳤다면** → `shop` 또는 `chinook`부터.
- **다중 조인·비즈니스 질의 연습** → `northwind`.
- **PostgreSQL로 Sakila를 쓰고 싶다면** → `pagila`(= postgres 네이티브 Sakila).

## 더 써 볼 만한 PostgreSQL 실습 데이터셋

> 질문하신 **Sakila(=Pagila)·MovieLens 이외**에, PostgreSQL 실습에 좋은 데이터셋 모음입니다.
> 필요하면 위 표처럼 `load.sh`를 갖춘 폴더로 추가해 드릴 수 있습니다.

| 데이터셋 | 무엇을 연습하나 | 규모 | 출처 / 라이선스 |
|----------|-----------------|------|------------------|
| **Northwind** *(추가됨)* | 다중 조인, 매출/실적 분석 | 작음 | [pthom/northwind_psql](https://github.com/pthom/northwind_psql) · Ms-PL |
| **Chinook** *(추가됨)* | 깔끔한 JOIN·집계 입문 | 작음 | [lerocha/chinook-database](https://github.com/lerocha/chinook-database) · MIT |
| **World DB** | 서브쿼리·상관 서브쿼리 입문 | 매우 작음 | 고전 MySQL world DB의 PostgreSQL 포트 |
| **Lahman Baseball** | 풍부한 다중 테이블, 시즌별 집계 | 중간 | [SeanLahman](https://sabr.org/lahman-database/) · CC BY-SA |
| **OpenFlights** | 그래프형 조인(공항·노선·항공사) | 작음 | [openflights.org](https://openflights.org/data.html) · ODbL |
| **Olist Brazilian E-Commerce** | 현실적인 멀티테이블·지저분한 데이터(파이프라인 연습) | 중간 | [Kaggle Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) · CC BY-NC (Kaggle 계정 필요) |
| **NYC Taxi (TLC)** | 대용량·시계열·인덱싱/파티셔닝/성능 | 대용량 | [NYC TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) · 공공 |
| **TPC-H** | 쿼리 최적화·실행계획(원하는 스케일로 생성) | 가변 | [TPC](https://www.tpc.org/tpch/) 벤치마크 |
| **Employees (test_db)** | 큰 테이블에서 인덱스/조인 성능 | 중간(~160MB) | [datacharmer/test_db](https://github.com/datacharmer/test_db) (PG 포트 다수) |
| **Stack Exchange dump** | 윈도우 함수·랭킹·텍스트 | 대용량 | [archive.org SE dump](https://archive.org/details/stackexchange) · CC BY-SA |

**난이도별 추천 동선**
- 입문(모듈 10·11 직후): `shop` → `chinook` → `world`
- 중급(분석 쿼리): `northwind` → `pagila` → `lahman`
- 고급(성능·최적화, 주로 졸업생 트랙): `employees` → `tpc-h` → `nyc-taxi`
- 파이프라인/지저분한 실데이터: `olist`

## 공통 적재 방법
대부분의 폴더에는 `load.sh`가 있습니다. PostgreSQL이 실행 중이면:
```bash
cd <데이터셋폴더>
./load.sh          # 전용 DB를 만들고 적재
```
접속 정보는 `PG*` 환경변수(`PGHOST`/`PGPORT`/`PGUSER`/`PGPASSWORD`)로 바꿀 수 있습니다.
