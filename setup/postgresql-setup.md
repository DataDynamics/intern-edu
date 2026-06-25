# PostgreSQL 설치 & 접속 세팅

SQL 모듈(10·11)과 이후 데이터 실습은 **PostgreSQL**을 사용합니다. 운영체제별로 설치 방법이 다르니 자신의 환경에 맞는 절에서 시작하세요.

- **Windows** → [공식 설치 프로그램](#windows--공식-설치-프로그램)
- **macOS** → [Postgres.app](#macos--postgresapp)
- **Linux** → [패키지 매니저](#linux--패키지-매니저)

> 💡 도커에 익숙하다면 모듈 12에서처럼 컨테이너로 띄워도 됩니다. 다만 SQL 모듈을 처음 시작하는 단계에서는 **로컬에 직접 설치**하는 쪽이 접속·관리가 단순합니다. 컨테이너 방식은 모듈 12에서 따로 다룹니다.

---

## Windows — 공식 설치 프로그램

1. EDB가 배포하는 [PostgreSQL 공식 설치 프로그램](https://www.postgresql.org/download/windows/)을 내려받습니다. (버전은 **16** 권장)
2. 설치 마법사를 따라갑니다. 중간에 **슈퍼유저(`postgres`)의 비밀번호**를 정하는 단계가 있으니, 잊지 않도록 적어 두세요.
3. 포트는 기본값 **5432**를 그대로 둡니다.
4. 설치가 끝나면 함께 깔린 **psql** 또는 **SQL Shell (psql)**을 실행해 접속을 확인합니다. (사용자 `postgres`, 비밀번호는 설치 때 정한 값)

> WSL2 + Ubuntu 환경을 쓰고 있다면 Windows용 설치 대신 아래 **Linux** 절을 따르세요. 실습 모듈 대부분이 WSL2를 기준으로 작성되어 있습니다.

---

## macOS — Postgres.app

macOS에서는 설정이 가장 단순한 **[Postgres.app](https://postgresapp.com/)**을 사용합니다.

1. [postgresapp.com](https://postgresapp.com/)에서 앱을 내려받아 `Applications`로 옮깁니다.
2. 앱을 실행하고 **Initialize**(또는 **Start**)를 누르면 PostgreSQL 서버가 곧바로 뜹니다.
3. 코끼리 아이콘이 메뉴 막대에 떠 있으면 서버가 켜진 상태입니다. (앱을 닫아도 서버는 메뉴 막대에서 계속 돌아갑니다.)
4. 터미널에서 `psql`을 바로 쓸 수 있도록 CLI 도구의 경로를 한 번 등록합니다.

```bash
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

터미널을 새로 연 뒤 `psql --version`이 보이면 성공입니다.

> Postgres.app은 **현재 macOS 사용자 이름**으로 슈퍼유저와 같은 이름의 데이터베이스를 자동으로 만들어 줍니다. 그래서 별도 사용자/비밀번호 없이 `psql`만 쳐도 접속됩니다. 실습 코드도 이 기본 접속을 그대로 사용하므로 **추가 설정 없이 바로 동작**합니다.

---

## Linux — 패키지 매니저

Ubuntu/Debian 기준입니다. (다른 배포판은 해당 패키지 매니저로 바꿔 주세요.)

```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo service postgresql start      # 또는: sudo systemctl start postgresql
```

설치 직후에는 OS의 `postgres` 사용자로만 접속할 수 있습니다. 실습용 사용자와 데이터베이스를 만들어 두면 편합니다.

```bash
# postgres 관리자 계정으로 접속
sudo -u postgres psql

-- (psql 안에서) 내 리눅스 계정 이름으로 역할과 DB 생성
CREATE ROLE myname LOGIN PASSWORD 'mypassword';
CREATE DATABASE myname OWNER myname;
\q
```

이제 `psql`로 바로 접속할 수 있습니다.

---

## 접속 확인

설치가 끝나면 터미널에서 `psql`로 접속해 봅니다.

```bash
psql                       # macOS(Postgres.app) / Linux: 기본 접속
psql -U postgres           # Windows / 사용자 지정 시
```

접속되면 아래로 버전과 현재 접속 정보를 확인할 수 있습니다.

```sql
SELECT version();   -- PostgreSQL 16.x ...
\conninfo           -- 현재 사용자/DB/포트
\q                  -- 종료
```

---

## Python에서 접속하기 (psycopg2)

SQL 모듈의 `demo.py`·`check.py`는 Python에서 PostgreSQL에 접속하기 위해 **psycopg2** 드라이버를 사용합니다. 가상환경을 활성화한 상태에서 설치하세요.

```bash
uv pip install psycopg2-binary      # 또는: pip install psycopg2-binary
```

실습 코드는 접속 정보를 **환경변수**에서 읽습니다. 두 가지 방법 중 하나를 쓰면 됩니다.

- **`DATABASE_URL` 하나로 지정** (가장 간단)
  ```bash
  export DATABASE_URL="postgresql://사용자:비밀번호@localhost:5432/DB이름"
  ```
- **개별 `PG*` 변수로 지정** (libpq 표준)
  ```bash
  export PGHOST=localhost PGPORT=5432 PGUSER=postgres PGPASSWORD=비밀번호 PGDATABASE=DB이름
  ```

환경변수를 **아무것도 설정하지 않으면** libpq 기본값(현재 OS 사용자 이름의 사용자·DB, localhost:5432)으로 접속합니다.

### 운영체제별 기본값 요약

| OS | 기본 사용자 | 비밀번호 | 추가 설정 |
|----|-------------|----------|-----------|
| **macOS (Postgres.app)** | 내 macOS 사용자 이름 | 없음 | 없음 — `python demo.py`가 바로 동작 |
| **Linux** | 위에서 만든 역할 | 위에서 정한 값 | 필요 시 `DATABASE_URL` 또는 `PG*` 설정 |
| **Windows** | `postgres` | 설치 때 정한 값 | `DATABASE_URL` 또는 `PG*` 설정 권장 |

예를 들어 Windows에서는 다음처럼 지정합니다(PowerShell).

```powershell
$env:DATABASE_URL = "postgresql://postgres:내비밀번호@localhost:5432/postgres"
```

---

## 자주 묻는 문제

- **`psql: command not found`** — CLI 경로 등록이 안 된 경우입니다. macOS는 위 `paths.d` 등록을, Windows는 설치 폴더의 `bin`을 PATH에 추가하세요.
- **`could not connect to server` / `Connection refused`** — 서버가 꺼져 있습니다. Postgres.app은 **Start**, Linux는 `sudo service postgresql start`로 켜세요.
- **`password authentication failed`** — 사용자/비밀번호가 맞지 않습니다. `DATABASE_URL` 또는 `PG*` 환경변수를 다시 확인하세요.
- **`ModuleNotFoundError: psycopg2`** — 가상환경에서 `psycopg2-binary`를 설치했는지 확인하세요.

> 더 깊은 내용은 [PostgreSQL 공식 문서](https://www.postgresql.org/docs/)를 참고하세요.
