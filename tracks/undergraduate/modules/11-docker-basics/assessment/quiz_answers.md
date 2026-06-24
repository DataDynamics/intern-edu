# 모듈 11 — 퀴즈 정답

1. 이미지는 실행에 필요한 것을 담은 **템플릿/패키지**, 컨테이너는 그 이미지를 **실행한 인스턴스**.
2. 컨테이너는 삭제하면 내부 데이터가 사라짐. 볼륨에 데이터를 두면 컨테이너를 지워도 **데이터가 보존**됨.
3. `호스트포트:컨테이너포트`. 호스트의 5432로 들어온 요청을 컨테이너의 5432로 전달.
4. `down`은 컨테이너만 제거(볼륨 유지 → 데이터 보존), `down -v`는 **볼륨까지 삭제**(데이터 소멸).
5. 컨테이너가 **빈 데이터 디렉토리로 처음 기동될 때 한 번** 자동 실행됨.

6.
   ```bash
   docker run -d postgres:16
   docker ps
   ```
7. `docker logs pg`
8. `docker exec -it pg bash`
9. `docker compose exec db psql -U postgres -d shop`
10. `docker compose config`
