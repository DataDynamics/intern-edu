# Northwind — 고전 e-커머스/ERP 샘플

Microsoft가 배포해 온 가장 유명한 교육용 데이터베이스입니다. 식료품 무역회사의 주문·고객·직원·공급사·상품을 담아, **다중 조인과 비즈니스 질의 연습**에 좋습니다. 실무에서 마주치는 전형적인 ERP 스키마라 모듈 10·11 다음 단계로 적합합니다.

## 출처 / 라이선스
- **출처**: [pthom/northwind_psql](https://github.com/pthom/northwind_psql) (`northwind.sql`)
- **라이선스**: Microsoft Public License (Ms-PL) — 자유 사용
- 원본을 커밋하지 않고 적재 시 내려받습니다(약 0.35MB).

## 규모 / 주요 테이블
- 14개 테이블, 주문 약 830 / 주문상세 약 2,150
- 핵심 흐름: `customers` → `orders` → `order_details` ← `products` ← `categories`/`suppliers`
- `employees`(셀프 조인: `reports_to`), `shippers`, `region`/`territories`

## 적재
```bash
./load.sh            # DB 'northwind' 생성 후 적재 (NORTHWIND_DB로 변경 가능)
psql -d northwind
```

## 연습 아이디어
- 카테고리/상품별 매출 (`order_details`의 `unit_price*quantity*(1-discount)`)
- 직원별 매출 실적, 매니저 셀프 조인
- 국가별 고객 수와 주문 수 (`LEFT JOIN`으로 주문 없는 고객까지)
- 월별 매출 추이 (`date_trunc`), 상위 거래처 순위(윈도우 함수)
