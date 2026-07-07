import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="퀵쿼트 | 화장품 ODM 견적 관리 도구",
    page_icon="🧾",
    layout="wide",
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@st.cache_data
def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


@st.cache_data
def _read_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


@st.cache_data
def build_home_html() -> str:
    """퀵쿼트.html 을 iframe 안에서도 동작하도록 가공한다.

    - sample-data.js 외부 스크립트를 인라인으로 삽입
    - sensifilter-hero.webp 를 base64 data URI 로 인라인
    - '새 견적 만들기' 이동 로직을 쿼리 파라미터(?page=quote) 기반으로 변경
    """
    html = _read_text(ASSETS / "home.html")
    js = _read_text(ASSETS / "sample-data.js")
    img_b64 = _read_base64(ASSETS / "sensifilter-hero.webp")

    html = html.replace(
        '<script src="sample-data.js"></script>',
        f"<script>\n{js}\n</script>",
    )
    html = html.replace(
        "url('sensifilter-hero.webp')",
        f"url('data:image/webp;base64,{img_b64}')",
    )
    html = html.replace(
        "window.location.href = 'quote-builder.html';",
        "window.top.location.href = "
        "window.top.location.pathname + '?page=quote';",
    )
    return html


@st.cache_data
def build_quote_builder_html() -> str:
    """quote-builder.html 을 iframe 안에서도 동작하도록 가공한다.

    - '← 홈으로' 링크를 쿼리 파라미터(?page=home) 기반으로 변경
    """
    html = _read_text(ASSETS / "quote_builder.html")
    html = html.replace(
        '<a class="back-link" href="index.html">← 홈으로</a>',
        '<a class="back-link" href="?page=home" target="_top">← 홈으로</a>',
    )
    return html


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

query_page = st.query_params.get("page", "home")
if "page" not in st.session_state:
    st.session_state.page = query_page

# 사이드바의 이동 버튼(iframe 트릭이 막히는 환경을 위한 보조 수단)
with st.sidebar:
    st.markdown("### 🧾 퀵쿼트")
    if st.button("🏠 홈", use_container_width=True):
        st.session_state.page = "home"
        st.query_params["page"] = "home"
        st.rerun()
    if st.button("📝 새 견적 만들기", use_container_width=True):
        st.session_state.page = "quote"
        st.query_params["page"] = "quote"
        st.rerun()

# 페이지 내부 링크 클릭으로 쿼리 파라미터가 바뀐 경우 세션 상태 동기화
if query_page != st.session_state.page:
    st.session_state.page = query_page

# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

if st.session_state.page == "quote":
    components.html(build_quote_builder_html(), height=950, scrolling=True)
else:
    components.html(build_home_html(), height=1700, scrolling=True)
