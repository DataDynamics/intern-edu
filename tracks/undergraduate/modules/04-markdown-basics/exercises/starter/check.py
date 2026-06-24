"""profile.md가 요구된 Markdown 요소를 모두 포함하는지 검사."""
import re
import sys
import pathlib

PATH = "profile.md"


def main():
    text = pathlib.Path(PATH).read_text(encoding="utf-8")
    lines = text.split("\n")

    checks = {
        "H1 제목(# )": any(re.match(r"# \S", ln) for ln in lines),
        "H2 제목(## ) 2개 이상": sum(bool(re.match(r"## \S", ln)) for ln in lines) >= 2,
        "굵게(**...**)": re.search(r"\*\*[^*\n]+\*\*", text) is not None,
        "순서없는 목록(- )": any(re.match(r"- \S", ln) for ln in lines),
        "순서있는 목록(1. )": any(re.match(r"\d+\. \S", ln) for ln in lines),
        "링크([..](..))": re.search(r"\[[^\]]+\]\([^)]+\)", text) is not None,
        "인라인 코드(`..`)": re.search(r"`[^`\n]+`", text) is not None,
        "코드 블록(```)": text.count("```") >= 2,
        "표(| .. |)": sum(bool(re.match(r"\|.*\|", ln)) for ln in lines) >= 2,
        "체크리스트(- [ ]/[x])": re.search(r"- \[[ xX]\]", text) is not None,
        "인용문(> )": any(re.match(r"> \S", ln) for ln in lines),
    }

    failed = [name for name, ok in checks.items() if not ok]
    for name, ok in checks.items():
        print(f"  {'✅' if ok else '❌'} {name}")
    if failed:
        print(f"\n아직 부족한 요소: {', '.join(failed)}")
        sys.exit(1)
    print("\n✅ 모든 테스트 통과! 훌륭한 Markdown 문서입니다.")


if __name__ == "__main__":
    main()
