import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="퀵쿼트 | 화장품 ODM 견적 관리 도구",
    page_icon="🧾",
    layout="wide",
)


# ---------------------------------------------------------------------------
# 견적 이력 샘플 데이터 (원래 sample-data.js)
# ---------------------------------------------------------------------------

SAMPLE_DATA_JS = """
// 퀵쿼트 샘플 견적 데이터 (완성된 견적서 100건)
// 필드: client(고객사명) / category(제품카테고리) / amount(최종 견적금액, 원) / status(진행상태: 진행·완료·네고·보류)
const SAMPLE_QUOTES = [
  { client: "내추럴리치", category: "색조", amount: 11410000, status: "완료" },
  { client: "클린레이지", category: "헤어케어", amount: 33190000, status: "보류" },
  { client: "화이트로즈코스메틱", category: "헤어케어", amount: 17620000, status: "진행" },
  { client: "미소화장품", category: "헤어케어", amount: 62720000, status: "완료" },
  { client: "스킨아뜰리에", category: "헤어케어", amount: 33320000, status: "보류" },
  { client: "러블리코스메틱", category: "스킨케어", amount: 87800000, status: "진행" },
  { client: "글로우앤코", category: "색조", amount: 7480000, status: "완료" },
  { client: "퓨리스트랩", category: "색조", amount: 5770000, status: "진행" },
  { client: "허벌센스", category: "스킨케어", amount: 27240000, status: "네고" },
  { client: "블룸코스메틱", category: "헤어케어", amount: 31220000, status: "진행" },
  { client: "러블리코스메틱", category: "스킨케어", amount: 58500000, status: "진행" },
  { client: "오로라코스메틱", category: "색조", amount: 36270000, status: "완료" },
  { client: "스킨스토리", category: "헤어케어", amount: 28350000, status: "진행" },
  { client: "데일리스킨", category: "스킨케어", amount: 23080000, status: "네고" },
  { client: "미소화장품", category: "헤어케어", amount: 43740000, status: "완료" },
  { client: "화이트로즈코스메틱", category: "헤어케어", amount: 20080000, status: "보류" },
  { client: "화이트로즈코스메틱", category: "색조", amount: 43080000, status: "완료" },
  { client: "정원뷰티", category: "헤어케어", amount: 17380000, status: "완료" },
  { client: "뷰티랩 코퍼레이션", category: "스킨케어", amount: 60850000, status: "진행" },
  { client: "클린레이지", category: "색조", amount: 23200000, status: "네고" },
  { client: "모던뷰티랩", category: "스킨케어", amount: 51620000, status: "진행" },
  { client: "미소화장품", category: "색조", amount: 25850000, status: "진행" },
  { client: "모던뷰티랩", category: "색조", amount: 38870000, status: "보류" },
  { client: "그린내추럴", category: "헤어케어", amount: 55250000, status: "진행" },
  { client: "라뮤즈뷰티", category: "헤어케어", amount: 54770000, status: "완료" },
  { client: "스마일코스메틱", category: "헤어케어", amount: 47150000, status: "네고" },
  { client: "데일리스킨", category: "스킨케어", amount: 86790000, status: "완료" },
  { client: "라뮤즈뷰티", category: "색조", amount: 15440000, status: "완료" },
  { client: "코렌뷰티", category: "색조", amount: 11810000, status: "네고" },
  { client: "퓨리스트랩", category: "색조", amount: 34240000, status: "진행" },
  { client: "코스메디랩", category: "색조", amount: 48240000, status: "진행" },
  { client: "뷰티온", category: "스킨케어", amount: 18540000, status: "진행" },
  { client: "화이트로즈코스메틱", category: "스킨케어", amount: 61740000, status: "진행" },
  { client: "코렌뷰티", category: "헤어케어", amount: 13730000, status: "완료" },
  { client: "내추럴리치", category: "색조", amount: 52560000, status: "네고" },
  { client: "글로우앤코", category: "색조", amount: 32490000, status: "진행" },
  { client: "뷰티랩 코퍼레이션", category: "헤어케어", amount: 15030000, status: "보류" },
  { client: "블룸코스메틱", category: "색조", amount: 26770000, status: "네고" },
  { client: "클리어스킨연구소", category: "헤어케어", amount: 34430000, status: "네고" },
  { client: "코렌뷰티", category: "헤어케어", amount: 52450000, status: "진행" },
  { client: "내추럴리치", category: "스킨케어", amount: 52410000, status: "진행" },
  { client: "오로라코스메틱", category: "헤어케어", amount: 18010000, status: "완료" },
  { client: "스마일코스메틱", category: "헤어케어", amount: 69010000, status: "진행" },
  { client: "에코뷰티", category: "색조", amount: 29970000, status: "진행" },
  { client: "데일리스킨", category: "색조", amount: 30690000, status: "완료" },
  { client: "퓨리스트랩", category: "헤어케어", amount: 32230000, status: "진행" },
  { client: "퓨리스트랩", category: "색조", amount: 48540000, status: "완료" },
  { client: "정원뷰티", category: "색조", amount: 12230000, status: "보류" },
  { client: "뷰티랩 코퍼레이션", category: "색조", amount: 28230000, status: "보류" },
  { client: "스킨스토리", category: "색조", amount: 7010000, status: "완료" },
  { client: "뷰티랩 코퍼레이션", category: "색조", amount: 55410000, status: "완료" },
  { client: "내추럴리치", category: "색조", amount: 11650000, status: "완료" },
  { client: "퓨리스트랩", category: "헤어케어", amount: 23860000, status: "완료" },
  { client: "퓨리스트랩", category: "스킨케어", amount: 28310000, status: "완료" },
  { client: "봄날화장품", category: "헤어케어", amount: 69250000, status: "완료" },
  { client: "클리어스킨연구소", category: "스킨케어", amount: 70690000, status: "완료" },
  { client: "클리어스킨연구소", category: "헤어케어", amount: 43690000, status: "진행" },
  { client: "내추럴리치", category: "색조", amount: 22070000, status: "완료" },
  { client: "데일리스킨", category: "스킨케어", amount: 85240000, status: "진행" },
  { client: "오로라코스메틱", category: "색조", amount: 29760000, status: "완료" },
  { client: "미소화장품", category: "스킨케어", amount: 41020000, status: "네고" },
  { client: "스킨스토리", category: "스킨케어", amount: 73610000, status: "진행" },
  { client: "세렌디코스메틱", category: "스킨케어", amount: 39920000, status: "진행" },
  { client: "블룸코스메틱", category: "색조", amount: 49290000, status: "네고" },
  { client: "미소화장품", category: "색조", amount: 37100000, status: "완료" },
  { client: "봄날화장품", category: "헤어케어", amount: 57390000, status: "진행" },
  { client: "퓨리스트랩", category: "스킨케어", amount: 61140000, status: "완료" },
  { client: "오가닉머스트", category: "색조", amount: 49880000, status: "완료" },
  { client: "코렌뷰티", category: "헤어케어", amount: 34680000, status: "완료" },
  { client: "정원뷰티", category: "색조", amount: 45080000, status: "네고" },
  { client: "실키터치", category: "색조", amount: 32830000, status: "진행" },
  { client: "클린레이지", category: "색조", amount: 33030000, status: "진행" },
  { client: "스킨스토리", category: "헤어케어", amount: 52880000, status: "네고" },
  { client: "라뮤즈뷰티", category: "색조", amount: 17080000, status: "완료" },
  { client: "뷰티랩 코퍼레이션", category: "헤어케어", amount: 49750000, status: "네고" },
  { client: "블룸코스메틱", category: "색조", amount: 38960000, status: "완료" },
  { client: "내추럴리치", category: "헤어케어", amount: 40790000, status: "진행" },
  { client: "코스메디랩", category: "색조", amount: 8280000, status: "완료" },
  { client: "그린내추럴", category: "스킨케어", amount: 56430000, status: "네고" },
  { client: "라뮤즈뷰티", category: "스킨케어", amount: 64910000, status: "네고" },
  { client: "오로라코스메틱", category: "색조", amount: 21840000, status: "네고" },
  { client: "데일리스킨", category: "스킨케어", amount: 77380000, status: "진행" },
  { client: "블룸코스메틱", category: "헤어케어", amount: 6040000, status: "완료" },
  { client: "데일리스킨", category: "헤어케어", amount: 56020000, status: "완료" },
  { client: "스마일코스메틱", category: "색조", amount: 48030000, status: "완료" },
  { client: "정원뷰티", category: "색조", amount: 48160000, status: "네고" },
  { client: "코렌뷰티", category: "색조", amount: 4440000, status: "완료" },
  { client: "데일리스킨", category: "스킨케어", amount: 13530000, status: "진행" },
  { client: "스마일코스메틱", category: "헤어케어", amount: 31240000, status: "네고" },
  { client: "내추럴리치", category: "스킨케어", amount: 30840000, status: "진행" },
  { client: "라뮤즈뷰티", category: "스킨케어", amount: 12300000, status: "완료" },
  { client: "실키터치", category: "색조", amount: 13290000, status: "완료" },
  { client: "미소화장품", category: "색조", amount: 55530000, status: "진행" },
  { client: "코스메디랩", category: "헤어케어", amount: 64480000, status: "완료" },
  { client: "뷰티온", category: "스킨케어", amount: 61370000, status: "완료" },
  { client: "허벌센스", category: "색조", amount: 54620000, status: "완료" },
  { client: "코스메디랩", category: "색조", amount: 56490000, status: "완료" },
  { client: "모던뷰티랩", category: "스킨케어", amount: 35040000, status: "진행" },
  { client: "스킨아뜰리에", category: "헤어케어", amount: 66980000, status: "네고" },
  { client: "퓨리스트랩", category: "스킨케어", amount: 88050000, status: "네고" },
];
"""


# ---------------------------------------------------------------------------
# 히어로 배경 이미지 (원래 sensifilter-hero.webp, base64 인라인)
# ---------------------------------------------------------------------------

HERO_IMAGE_B64 = (
    "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"
    "e/zBQAAA="
)


# ---------------------------------------------------------------------------
# 앱 화면 (원래 퀵쿼트.html)
# ---------------------------------------------------------------------------

APP_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>퀵쿼트 | 화장품 ODM 견적 관리 도구</title>
<style>
  :root{
    --bg:#FAF6F2;
    --surface:#FFFFFF;
    --ink:#1F2333;
    --ink-soft:#5B5A66;
    --navy:#1E2A4A;
    --navy-dark:#141B33;
    --pink:#E8B4B8;
    --pink-soft:#F6E4E1;
    --beige:#EFE3D6;
    --line:#ECE6DF;
    --radius:16px;
    --shadow:0 8px 24px rgba(31,35,51,0.06);

    /* 견적 생성 화면에서 쓰는 색상을 공용 팔레트에 맞춰 매핑 */
    --primary:var(--navy-dark);
    --primary-dark:#0F1626;
    --secondary:var(--pink);
    --secondary-dark:#D89AA0;
    --blush:var(--pink-soft);
    --warn-bg:#FFF3D6;
    --warn-ink:#8A6E1D;
    --ok-bg:#E4F3E7;
    --ok-ink:#227A3D;
  }
  *{box-sizing:border-box;margin:0;padding:0;}
  body{
    font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI','Apple SD Gothic Neo','Malgun Gothic',Roboto,sans-serif;
    font-size:16px;
    background:var(--bg);
    color:var(--ink);
    line-height:1.6;
    -webkit-text-size-adjust:100%;
  }
  .container{max-width:1100px;margin:0 auto;padding:0 24px;}

  /* 견적 생성 화면이 활성화됐을 때만 고정 높이 레이아웃(내부 스크롤)을 적용 */
  body.builder-active{
    height:100vh;
    overflow:hidden;
    display:flex;
    flex-direction:column;
  }
  body.builder-active header{flex:0 0 auto;}
  body.builder-active footer{flex:0 0 auto;padding:6px 0;font-size:12px;}

  .view-hidden{display:none !important;}

  /* Header */
  header{
    position:sticky;top:0;z-index:50;
    background:rgba(250,246,242,0.9);
    backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line);
  }
  .nav{
    display:flex;align-items:center;justify-content:space-between;
    padding:16px 24px;max-width:1100px;margin:0 auto;
  }
  .logo{
    display:flex;align-items:center;gap:8px;
    font-size:20px;font-weight:800;color:var(--navy-dark);
  }
  .logo-badge{
    width:28px;height:28px;border-radius:8px;
    background:linear-gradient(135deg,var(--pink),var(--navy));
    display:inline-block;
  }
  .nav-links{display:flex;gap:28px;font-size:14px;color:var(--ink-soft);}
  .nav-links a{color:inherit;text-decoration:none;}
  .nav-links a:hover{color:var(--navy);}
  .nav-cta{
    background:var(--navy-dark);color:#fff;border:none;
    padding:10px 20px;border-radius:999px;font-size:14px;font-weight:600;
    cursor:pointer;white-space:nowrap;
  }
  .nav-cta:hover{background:var(--navy);}
  .back-link{font-size:14px;color:var(--ink-soft);text-decoration:none;white-space:nowrap;}
  .back-link:hover{color:var(--navy);}
  .menu-btn{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var(--navy-dark);}

  /* Hero */
  .hero{
    padding:0;
    background-image:
      linear-gradient(90deg, rgba(250,246,242,0.97) 0%, rgba(250,246,242,0.88) 32%, rgba(250,246,242,0.45) 62%, rgba(250,246,242,0.15) 100%),
      url('sensifilter-hero.webp');
    background-size:cover;
    background-position:center;
  }
  .hero-inner{
    padding:96px 24px;min-height:440px;
    display:flex;align-items:center;text-align:left;
  }
  .hero-text{max-width:520px;}
  .hero-eyebrow{
    display:inline-block;background:var(--pink-soft);color:var(--navy-dark);
    font-size:13px;font-weight:700;padding:6px 14px;border-radius:999px;margin-bottom:20px;
  }
  .hero h1{
    font-size:40px;font-weight:800;letter-spacing:-0.02em;color:var(--navy-dark);
    margin-bottom:16px;
  }
  .hero h1 span{color:var(--pink);}
  .hero p{
    font-size:16px;color:var(--ink-soft);max-width:480px;margin:0 0 32px;
  }
  .hero-actions{display:flex;gap:12px;justify-content:flex-start;flex-wrap:wrap;}
  .btn-primary{
    background:var(--navy-dark);color:#fff;border:none;
    padding:14px 28px;border-radius:999px;font-size:15px;font-weight:700;
    cursor:pointer;
  }
  .btn-primary:hover{background:var(--navy);}
  .btn-secondary{
    background:var(--surface);color:var(--navy-dark);border:1px solid var(--line);
    padding:14px 28px;border-radius:999px;font-size:15px;font-weight:700;
    cursor:pointer;
  }
  .btn-secondary:hover{border-color:var(--pink);}

  /* Feature cards */
  section{padding:48px 0;}
  .section-title{text-align:center;margin-bottom:32px;}
  .section-title h2{font-size:24px;font-weight:800;color:var(--navy-dark);margin-bottom:8px;}
  .section-title p{font-size:14px;color:var(--ink-soft);}

  .feature-grid{
    display:grid;grid-template-columns:repeat(3,1fr);gap:20px;
  }
  .feature-card{
    background:var(--surface);border-radius:var(--radius);padding:28px 24px;
    box-shadow:var(--shadow);border:1px solid var(--line);
  }
  .feature-icon{
    width:44px;height:44px;border-radius:12px;
    display:flex;align-items:center;justify-content:center;
    font-size:20px;margin-bottom:16px;
  }
  .feature-icon.pink{background:var(--pink-soft);}
  .feature-icon.beige{background:var(--beige);}
  .feature-icon.navy{background:#E7EAF2;}
  .feature-card h3{font-size:16px;font-weight:700;margin-bottom:8px;color:var(--navy-dark);}
  .feature-card p{font-size:13.5px;color:var(--ink-soft);}

  /* History preview */
  .history-panel{
    background:var(--surface);border-radius:var(--radius);
    border:1px solid var(--line);box-shadow:var(--shadow);
    overflow:hidden;
  }
  .history-header{
    display:flex;justify-content:space-between;align-items:center;
    padding:20px 24px;border-bottom:1px solid var(--line);
  }
  .history-header h3{font-size:16px;font-weight:700;color:var(--navy-dark);}
  .history-header a{font-size:13px;color:var(--navy);text-decoration:none;font-weight:600;}
  .history-header-actions{display:flex;align-items:center;gap:12px;}
  .filter-select{
    padding:7px 10px;border:1px solid var(--line);border-radius:8px;
    font-size:13px;color:var(--navy-dark);background:#fff;cursor:pointer;
  }
  .filter-select:focus{outline:none;border-color:var(--pink);}
  .history-item{
    display:flex;align-items:center;justify-content:space-between;
    padding:16px 24px;border-bottom:1px solid var(--line);
    font-size:14px;
  }
  .history-item:last-child{border-bottom:none;}
  .history-left{display:flex;align-items:center;gap:14px;}
  .client-avatar{
    width:36px;height:36px;border-radius:50%;
    display:flex;align-items:center;justify-content:center;
    font-size:13px;font-weight:700;color:#fff;flex-shrink:0;
  }
  .client-name{font-weight:700;color:var(--ink);}
  .client-meta{font-size:12.5px;color:var(--ink-soft);}
  .history-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:flex-end;}
  .amount{font-weight:700;color:var(--navy-dark);}
  .badge{
    font-size:12px;font-weight:700;padding:4px 10px;border-radius:999px;
  }
  .badge.done{background:#E4F3E7;color:#227A3D;}
  .badge.progress{background:var(--pink-soft);color:#B0505A;}
  .badge.draft{background:var(--beige);color:#8A6E3D;}
  .badge.hold{background:#EFEBF3;color:#6B5B95;}
  .badge.nego{background:#FFF3D6;color:#8A6E1D;}

  footer{
    text-align:center;padding:32px 0;color:var(--ink-soft);font-size:13px;
  }

  /* ===== 견적 생성 화면 ===== */
  .builder-container{
    max-width:1100px;margin:0 auto;padding:18px 24px 14px;
    width:100%;flex:1 1 auto;min-height:0;
    display:flex;flex-direction:column;
  }

  h1.page-title{font-size:26px;font-weight:800;color:var(--primary-dark);margin-bottom:4px;letter-spacing:-0.3px;}
  .page-sub{font-size:14px;color:var(--ink-soft);margin-bottom:14px;}

  .grid{
    display:grid;grid-template-columns:380px 1fr;gap:16px;align-items:stretch;
    flex:1 1 auto;min-height:0;
  }

  .panel{
    background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
    box-shadow:var(--shadow);padding:20px 22px;
    height:100%;min-height:0;
    display:flex;flex-direction:column;
    overflow-y:auto;
  }
  .panel h2{font-size:16px;font-weight:800;color:var(--primary-dark);margin-bottom:12px;flex:0 0 auto;}

  .field{margin-bottom:12px;}
  .field label{display:block;font-size:14px;font-weight:700;color:var(--ink);margin-bottom:6px;}
  .field .hint{font-size:12.5px;color:var(--ink-soft);margin-top:4px;}
  .field input, .field select{
    width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:10px;
    font-size:16px;background:#fff;color:var(--ink);
  }
  .field input:focus, .field select:focus{outline:none;border-color:var(--secondary);}
  .row-2{display:grid;grid-template-columns:1fr 1fr;gap:12px;}

  .btn-block-primary{
    width:100%;background:var(--secondary);color:#fff;border:none;
    padding:12px 0;border-radius:999px;font-size:16px;font-weight:700;cursor:pointer;
  }
  .btn-block-primary:hover{background:var(--secondary-dark);}
  .btn-block-secondary{
    width:100%;background:var(--surface);color:var(--primary-dark);border:1px solid var(--line);
    padding:11px 0;border-radius:999px;font-size:15px;font-weight:700;cursor:pointer;margin-top:8px;
  }
  .btn-block-secondary:hover{border-color:var(--secondary);}

  .empty-state{
    flex:1 1 auto;min-height:0;
    display:flex;flex-direction:column;align-items:center;justify-content:center;
    text-align:center;padding:20px;color:var(--ink-soft);font-size:14px;
  }
  .empty-state .icon{font-size:32px;margin-bottom:10px;}

  #builderView table{width:100%;border-collapse:collapse;font-size:14px;}
  #builderView th, #builderView td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--line);}
  #builderView th{color:var(--ink-soft);font-weight:700;font-size:12.5px;}
  #builderView td.num, #builderView th.num{text-align:right;}
  #builderView tr.total td{font-weight:800;color:var(--primary-dark);border-top:2px solid var(--primary-dark);border-bottom:none;}

  .status-flag{display:inline-block;font-size:13px;font-weight:700;padding:5px 12px;border-radius:999px;margin-bottom:12px;flex:0 0 auto;}
  .status-flag.warn{background:var(--warn-bg);color:var(--warn-ink);}
  .status-flag.ok{background:var(--ok-bg);color:var(--ok-ink);}

  .compare-title{font-size:13.5px;font-weight:700;color:var(--primary-dark);margin:16px 0 8px;}

  .delivery-info{
    margin-top:12px;padding:10px 14px;background:var(--blush);border-radius:10px;
    font-size:13.5px;font-weight:600;color:var(--primary-dark);
  }

  .quote-meta{margin-bottom:14px;}
  .quote-meta .quote-title-row{
    display:flex;align-items:baseline;justify-content:space-between;
    margin-bottom:10px;
  }
  .quote-meta .quote-title{font-size:20px;font-weight:800;color:var(--primary-dark);}
  .quote-meta .quote-no{font-size:12.5px;color:var(--ink-soft);font-weight:600;}
  .quote-meta .quote-meta-grid{
    display:grid;grid-template-columns:1fr 1fr;gap:5px 20px;
    font-size:13px;color:var(--ink);
  }
  .quote-meta .quote-meta-grid strong{
    color:var(--ink-soft);font-weight:700;margin-right:6px;
    display:inline-block;min-width:78px;
  }

  #resultPanel{display:none;flex:1 1 auto;min-height:0;overflow-y:auto;}

  @media (max-width:820px){
    body.builder-active{height:auto;overflow:visible;overflow-y:auto;}
    .builder-container{overflow:visible;}
    .grid{grid-template-columns:1fr;flex:none;}
    .row-2{grid-template-columns:1fr;}
    .panel{height:auto;overflow-y:visible;max-height:none;}
    #resultPanel{overflow-y:visible;}
  }

  @media print{
    body *{visibility:hidden;}
    #printArea, #printArea *{visibility:visible;}
    #printArea{
      position:absolute;top:0;left:0;width:100%;padding:24px;
    }
  }

  @media (max-width:760px){
    .nav-links{display:none;}
    .menu-btn{display:block;}
    .hero{
      background-image:
        linear-gradient(180deg, rgba(250,246,242,0.97) 0%, rgba(250,246,242,0.9) 55%, rgba(250,246,242,0.75) 100%),
        url('sensifilter-hero.webp');
    }
    .hero-inner{min-height:320px;padding:48px 24px;text-align:center;justify-content:center;}
    .hero-text{max-width:100%;}
    .hero p{margin-left:auto;margin-right:auto;}
    .hero-actions{justify-content:center;}
    .hero h1{font-size:28px;}
    .hero p{font-size:14px;}
    .feature-grid{grid-template-columns:1fr;}
    .history-item{flex-wrap:wrap;gap:8px;}
    .history-right{width:100%;justify-content:space-between;}
  }
</style>
</head>
<body>

<header>
  <div class="nav">
    <div class="logo"><span class="logo-badge"></span>퀵쿼트</div>
    <nav class="nav-links" id="navLinks">
      <a href="#features">기능</a>
      <a href="#history">견적 이력</a>
      <a href="#">문의</a>
    </nav>
    <div style="display:flex;align-items:center;gap:14px;">
      <a class="back-link view-hidden" id="backLink" href="#" onclick="showHome();return false;">← 홈으로</a>
      <button class="nav-cta" id="navCta" onclick="openNewQuote()">새 견적 만들기</button>
      <button class="menu-btn" onclick="toggleMenu()">☰</button>
    </div>
  </div>
</header>

<!-- ===== 홈 화면 ===== -->
<div id="homeView">

  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-text">
        <span class="hero-eyebrow">화장품 ODM 영업사원을 위한 견적 도구</span>
        <h1>몇 번의 입력으로<br>완성되는 <span>견적서</span></h1>
        <p>고객사 요청사항만 입력하면 표준 견적서가 자동으로 만들어지고, 고객사별 견적 이력을 한 번에 찾아볼 수 있습니다.</p>
        <div class="hero-actions">
          <button class="btn-primary" onclick="openNewQuote()">새 견적 만들기</button>
          <button class="btn-secondary" onclick="scrollToHistory()">견적 이력 보기</button>
        </div>
      </div>
    </div>
  </section>

  <main class="container">

    <section id="features">
      <div class="section-title">
        <h2>핵심 기능</h2>
        <p>영업사원의 반복 업무를 줄여주는 세 가지 기능</p>
      </div>
      <div class="feature-grid">
        <div class="feature-card">
          <div class="feature-icon pink">📄</div>
          <h3>자동 견적 생성</h3>
          <p>고객사, 제품 유형, 용량, 수량만 입력하면 표준 양식의 견적서가 즉시 완성됩니다.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon beige">🗂️</div>
          <h3>고객사별 이력 관리</h3>
          <p>과거 견적을 고객사별로 모아두고, 버전 변경 사항을 한눈에 비교할 수 있습니다.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon navy">🧮</div>
          <h3>원가 구조 계산</h3>
          <p>원료비·포장비·생산비·마진을 자동으로 구분해 견적 근거를 명확하게 보여줍니다.</p>
        </div>
      </div>
    </section>

    <section id="history">
      <div class="section-title">
        <h2>최근 견적 이력</h2>
        <p>모든 고객사의 견적 진행 상황을 한 화면에서 확인하세요</p>
      </div>
      <div class="history-panel" id="historyPanel">
        <div class="history-header">
          <h3>최근 견적 <span id="historyCount">5</span>건</h3>
          <div class="history-header-actions">
            <select id="categoryFilter" class="filter-select" onchange="onFilterChange()">
              <option value="">전체보기</option>
              <option value="스킨케어">스킨케어</option>
              <option value="색조">색조</option>
              <option value="헤어케어">헤어케어</option>
            </select>
            <select id="statusFilter" class="filter-select" onchange="onFilterChange()">
              <option value="">전체보기</option>
              <option value="진행">진행</option>
              <option value="완료">완료</option>
              <option value="네고">네고</option>
              <option value="보류">보류</option>
            </select>
            <a href="#" id="toggleHistoryLink" onclick="toggleHistory();return false;">더보기 →</a>
          </div>
        </div>

        <div id="historyList"></div>
      </div>
    </section>

  </main>

</div>

<!-- ===== 견적 생성 화면 ===== -->
<main class="builder-container view-hidden" id="builderView">
  <h1 class="page-title">새 견적 만들기</h1>
  <p class="page-sub">항목을 입력하면 수량 구간과 마진을 반영한 견적 단가, 예상납기까지 자동으로 계산합니다.</p>

  <div class="grid">

    <!-- 입력 폼 -->
    <div class="panel">
      <h2>견적 정보 입력</h2>
      <form id="quoteForm">
        <div class="field">
          <label for="client">고객사명</label>
          <input list="clientList" id="client" placeholder="예: 스마일코스메틱" required>
          <datalist id="clientList">
            <option value="스마일코스메틱"></option>
            <option value="뷰티랩 코퍼레이션"></option>
            <option value="그린내추럴"></option>
          </datalist>
        </div>

        <div class="field">
          <label for="category">제품 카테고리</label>
          <select id="category" required>
            <option value="">선택하세요</option>
            <option value="스킨케어">스킨케어</option>
            <option value="색조">색조</option>
            <option value="헤어케어">헤어케어</option>
          </select>
        </div>

        <div class="row-2">
          <div class="field">
            <label for="formulation">제형 타입</label>
            <select id="formulation" required>
              <option value="크림/로션">크림/로션</option>
              <option value="에센스/세럼">에센스/세럼</option>
              <option value="앰플">앰플</option>
              <option value="젤/워터">젤/워터</option>
              <option value="파운데이션/쿠션">파운데이션/쿠션</option>
              <option value="립/아이제품">립/아이제품</option>
              <option value="샴푸/트리트먼트">샴푸/트리트먼트</option>
              <option value="기타">기타</option>
            </select>
          </div>
          <div class="field">
            <label for="containerType">용기 타입</label>
            <select id="containerType" required>
              <option value="튜브">튜브</option>
              <option value="펌프용기">펌프용기</option>
              <option value="에어리스">에어리스</option>
              <option value="유리병">유리병</option>
              <option value="기타">기타</option>
            </select>
          </div>
        </div>

        <div class="row-2">
          <div class="field">
            <label for="volume">용량 (g/ml)</label>
            <input type="number" id="volume" min="1" placeholder="50" required>
          </div>
          <div class="field">
            <label for="qty">예상 수량 (개)</label>
            <input type="number" id="qty" min="1" placeholder="3000" required>
          </div>
        </div>

        <div class="row-2">
          <div class="field">
            <label for="margin">목표 마진율 (%)</label>
            <input type="number" id="margin" placeholder="기본 30%">
          </div>
          <div class="field">
            <label for="orderType">발주 유형</label>
            <select id="orderType">
              <option value="재주문">재주문 (기존 개발 완료)</option>
              <option value="신규">신규 개발</option>
            </select>
          </div>
        </div>

        <div class="row-2">
          <div class="field">
            <label for="repName">담당자명</label>
            <input type="text" id="repName" placeholder="예: 김영업">
          </div>
          <div class="field">
            <label for="repPhone">담당자 연락처</label>
            <input type="tel" id="repPhone" placeholder="010-1234-5678">
          </div>
        </div>

        <div class="field">
          <label for="paymentTerms">결제조건</label>
          <select id="paymentTerms">
            <option value="선금 30% / 잔금 70% (출고 전)">선금 30% / 잔금 70% (출고 전)</option>
            <option value="전액 선불">전액 선불</option>
            <option value="월말 일괄결제">월말 일괄결제</option>
            <option value="협의 후 결정">협의 후 결정</option>
          </select>
        </div>

        <div class="row-2">
          <div class="field">
            <label for="vatType">부가세</label>
            <select id="vatType">
              <option value="exclusive">별도 (VAT 별도)</option>
              <option value="inclusive">포함 (VAT 포함)</option>
            </select>
          </div>
          <div class="field">
            <label for="validDays">견적 유효기간 (일)</label>
            <input type="number" id="validDays" min="1" placeholder="14">
          </div>
        </div>

        <div class="field">
          <label for="brief">고객 요청사항 (선택)</label>
          <input type="file" id="brief">
        </div>

        <button type="submit" class="btn-block-primary">견적서 생성</button>
        <button type="button" class="btn-block-secondary" onclick="resetForm()">초기화</button>
      </form>
    </div>

    <!-- 결과 미리보기 -->
    <div class="panel" id="previewPanel">
      <h2>견적서 미리보기</h2>

      <div class="empty-state" id="emptyState">
        <div class="icon">🧾</div>
        왼쪽에 정보를 입력하고<br>"견적서 생성"을 누르면 결과가 여기에 표시됩니다.
      </div>

      <div id="resultPanel">
        <span class="status-flag" id="flagBadge"></span>

        <div id="printArea">
          <div class="quote-meta" id="quoteMeta"></div>
          <table>
            <thead>
              <tr>
                <th>항목</th>
                <th class="num">단가</th>
                <th class="num">수량</th>
                <th class="num">금액</th>
              </tr>
            </thead>
            <tbody id="quoteBody"></tbody>
          </table>

          <div class="delivery-info" id="deliveryInfo"></div>
        </div>

        <div class="compare-title">최근 견적 이력 비교 (동일 고객사 최근 3건)</div>
        <table id="compareTable">
          <thead>
            <tr><th>날짜</th><th class="num">단가</th><th class="num">차이</th></tr>
          </thead>
          <tbody id="compareBody"></tbody>
        </table>

        <button class="btn-block-secondary" style="margin-top:20px;" onclick="window.print()">PDF로 다운로드 (인쇄)</button>
      </div>
    </div>

  </div>
</main>

<footer>© 2026 퀵쿼트 · 화장품 ODM 영업사원을 위한 견적 관리 도구</footer>

<script src="sample-data.js"></script>
<script>
  /* ===== 화면 전환 (홈 ↔ 견적 생성) ===== */
  function showHome(){
    document.getElementById('homeView').classList.remove('view-hidden');
    document.getElementById('builderView').classList.add('view-hidden');
    document.body.classList.remove('builder-active');
    document.getElementById('navLinks').style.display = '';
    document.getElementById('navCta').style.display = '';
    document.getElementById('backLink').classList.add('view-hidden');
    window.scrollTo(0, 0);
  }

  function showBuilder(){
    document.getElementById('homeView').classList.add('view-hidden');
    document.getElementById('builderView').classList.remove('view-hidden');
    document.body.classList.add('builder-active');
    document.getElementById('navLinks').style.display = 'none';
    document.getElementById('navCta').style.display = 'none';
    document.getElementById('backLink').classList.remove('view-hidden');
    resetForm();
    window.scrollTo(0, 0);
  }

  function openNewQuote(){
    showBuilder();
  }
  function scrollToHistory(){
    document.getElementById('history').scrollIntoView({behavior:'smooth'});
  }
  function toggleMenu(){
    alert('모바일 메뉴 (다음 단계에서 구현).');
  }

  /* ===== 홈 화면: 최근 견적 이력 ===== */
  const AVATAR_COLORS = ["#E8B4B8","#1E2A4A","#B08968","#7C6A9C","#C97C6D","#6B8F71","#C9A66B","#8E5B5B"];
  const CATEGORY_STYLE = {
    "스킨케어": { bg:"var(--pink-soft)", color:"var(--navy-dark)" },
    "색조":     { bg:"var(--beige)",     color:"#8A6E3D" },
    "헤어케어": { bg:"#E7EAF2",          color:"var(--navy-dark)" }
  };
  const STATUS_CLASS = {
    "진행": "progress",
    "완료": "done",
    "네고": "nego",
    "보류": "hold"
  };

  function avatarColor(name){
    let hash = 0;
    for (let i = 0; i < name.length; i++){ hash = name.charCodeAt(i) + ((hash << 5) - hash); }
    return AVATAR_COLORS[Math.abs(hash) % AVATAR_COLORS.length];
  }

  function getFilteredQuotes(){
    const category = document.getElementById('categoryFilter').value;
    const status = document.getElementById('statusFilter').value;
    return SAMPLE_QUOTES.filter(q =>
      (!category || q.category === category) && (!status || q.status === status)
    );
  }

  function renderHistory(){
    const data = getFilteredQuotes();
    const count = historyExpanded ? data.length : Math.min(5, data.length);
    const items = data.slice(0, count);
    const list = document.getElementById('historyList');

    list.innerHTML = items.length ? items.map(q => {
      const style = CATEGORY_STYLE[q.category] || { bg:"var(--beige)", color:"var(--navy-dark)" };
      const statusClass = STATUS_CLASS[q.status] || "draft";
      return `
        <div class="history-item">
          <div class="history-left">
            <div class="client-avatar" style="background:${avatarColor(q.client)};">${q.client.slice(0,2)}</div>
            <div>
              <div class="client-name">${q.client}</div>
              <div class="client-meta">${q.category}</div>
            </div>
          </div>
          <div class="history-right">
            <span class="amount">₩ ${q.amount.toLocaleString()}</span>
            <span class="badge" style="background:${style.bg};color:${style.color};">${q.category}</span>
            <span class="badge ${statusClass}">${q.status}</span>
          </div>
        </div>`;
    }).join('') : `<div class="history-item" style="justify-content:center;color:var(--ink-soft);">조건에 맞는 견적 이력이 없습니다.</div>`;

    document.getElementById('historyCount').textContent = items.length;
    document.getElementById('toggleHistoryLink').style.display = data.length > 5 ? 'inline' : 'none';
  }

  let historyExpanded = false;
  function toggleHistory(){
    historyExpanded = !historyExpanded;
    document.getElementById('toggleHistoryLink').textContent = historyExpanded ? '접기 ↑' : '더보기 →';
    const panel = document.getElementById('historyPanel');
    panel.style.maxHeight = historyExpanded ? '560px' : 'none';
    panel.style.overflowY = historyExpanded ? 'auto' : 'visible';
    renderHistory();
  }

  function onFilterChange(){
    historyExpanded = false;
    document.getElementById('toggleHistoryLink').textContent = '더보기 →';
    const panel = document.getElementById('historyPanel');
    panel.style.maxHeight = 'none';
    panel.style.overflowY = 'visible';
    renderHistory();
  }

  renderHistory();

  /* ===== 견적 생성 화면 ===== */
  // 원료단가표 (모의 데이터, g·ml당 원료단가)
  const PRICE_TABLE = {
    "스킨케어": { material: 150 },
    "색조":     { material: 300 },
    "헤어케어": { material: 80 }
  };

  // 제형 타입별 원가 배수 (제형이 복잡할수록 원료·공정비 상승)
  const FORMULATION_FACTOR = {
    "크림/로션": 1.0,
    "에센스/세럼": 1.15,
    "앰플": 1.3,
    "젤/워터": 0.9,
    "파운데이션/쿠션": 1.4,
    "립/아이제품": 1.25,
    "샴푸/트리트먼트": 0.85,
    "기타": 1.0
  };

  // 용기 타입별 개당 단가 (모의 데이터)
  const CONTAINER_COST = {
    "튜브": 400,
    "펌프용기": 600,
    "에어리스": 900,
    "유리병": 700,
    "기타": 500
  };

  // 신규 개발 시 1회성 개발비(금형·규격 개발), 재주문은 면제
  const DEV_FEE = 3000000;

  // 수량 구간별 단가율 (소량일수록 단가 상승)
  function qtyTierRate(qty){
    if (qty < 1000) return 1.3;
    if (qty <= 5000) return 1.0;
    return 0.85;
  }

  // 수량 구간별 예상 리드타임 (영업일 기준, 소량일수록 짧고 대량일수록 김)
  function estimateLeadDays(qty){
    if (qty < 1000) return 20;
    if (qty <= 5000) return 30;
    return 45;
  }

  function formatDate(d){
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }

  // 견적번호 발급 (당일 기준 순번 발급, 예: QT-20260707-001)
  function issueQuoteNumber(){
    const dateKey = formatDate(new Date()).replace(/-/g, '');
    const storageKey = 'qq_quote_seq_' + dateKey;
    const seq = parseInt(localStorage.getItem(storageKey) || '0', 10) + 1;
    localStorage.setItem(storageKey, String(seq));
    return `QT-${dateKey}-${String(seq).padStart(3, '0')}`;
  }

  // 고객사별 과거 견적 이력 (모의 데이터, 최근 3건 단가)
  const HISTORY = {
    "스마일코스메틱":   [{date:"2026-06-02", unit:24500},{date:"2026-05-10", unit:23800},{date:"2026-04-02", unit:24100}],
    "뷰티랩 코퍼레이션": [{date:"2026-06-20", unit:41000},{date:"2026-05-28", unit:39500},{date:"2026-04-15", unit:40200}],
    "그린내추럴":       [{date:"2026-06-11", unit:15200},{date:"2026-05-01", unit:14800},{date:"2026-03-22", unit:15000}]
  };

  const form = document.getElementById('quoteForm');
  const emptyState = document.getElementById('emptyState');
  const resultPanel = document.getElementById('resultPanel');
  const quoteBody = document.getElementById('quoteBody');
  const quoteMeta = document.getElementById('quoteMeta');
  const deliveryInfo = document.getElementById('deliveryInfo');
  const compareBody = document.getElementById('compareBody');
  const flagBadge = document.getElementById('flagBadge');

  form.addEventListener('submit', function(e){
    e.preventDefault();

    const client = document.getElementById('client').value.trim();
    const category = document.getElementById('category').value;
    const formulation = document.getElementById('formulation').value;
    const containerType = document.getElementById('containerType').value;
    const volume = parseFloat(document.getElementById('volume').value);
    const qty = parseInt(document.getElementById('qty').value, 10);
    const marginInput = document.getElementById('margin').value;
    const marginRate = marginInput ? parseFloat(marginInput) / 100 : 0.30;
    const orderType = document.getElementById('orderType').value;
    const repName = document.getElementById('repName').value.trim();
    const repPhone = document.getElementById('repPhone').value.trim();
    const paymentTerms = document.getElementById('paymentTerms').value;
    const vatType = document.getElementById('vatType').value;
    const validDaysInput = document.getElementById('validDays').value;
    const validDays = validDaysInput ? parseInt(validDaysInput, 10) : 14;

    const priceInfo = PRICE_TABLE[category];
    if (!priceInfo) return;

    // Process: 원가 계산 -> 수량 구간 적용 -> 마진 적용 -> 총액 산출 (내부 계산용, 고객 견적서에는 단가만 노출)
    const materialCost = priceInfo.material * volume * (FORMULATION_FACTOR[formulation] || 1.0);
    const containerCost = CONTAINER_COST[containerType] || 500;
    const tier = qtyTierRate(qty);
    const unitCost = (materialCost + containerCost) * tier;
    const unitPrice = Math.round(unitCost * (1 + marginRate));
    const totalPrice = unitPrice * qty;
    const devFee = orderType === '신규' ? DEV_FEE : 0;

    const quoteNo = issueQuoteNumber();
    const issueDate = new Date();
    const validUntil = new Date();
    validUntil.setDate(validUntil.getDate() + validDays);

    // 견적서 상단 정보 (견적번호 · 고객사 · 담당자 연락처 · 결제조건 · 유효기간)
    quoteMeta.innerHTML = `
      <div class="quote-title-row">
        <span class="quote-title">견적서</span>
        <span class="quote-no">견적번호 ${quoteNo}</span>
      </div>
      <div class="quote-meta-grid">
        <div><strong>고객사</strong>${client || '-'}</div>
        <div><strong>발행일</strong>${formatDate(issueDate)}</div>
        <div><strong>담당자</strong>${repName || '-'}${repPhone ? ' (' + repPhone + ')' : ''}</div>
        <div><strong>결제조건</strong>${paymentTerms}</div>
        <div><strong>견적 유효기간</strong>${formatDate(issueDate)} ~ ${formatDate(validUntil)} (${validDays}일)</div>
      </div>
    `;

    // 견적서 표 렌더링 (고객 전달용 - 단가/수량/금액만 표기, 원가·마진 비공개)
    const supplyAmount = totalPrice + devFee;
    const vatAmount = Math.round(supplyAmount * 0.1);
    const grandTotal = vatType === 'exclusive' ? supplyAmount + vatAmount : supplyAmount;

    quoteBody.innerHTML = `
      <tr>
        <td>${category} ${formulation} (용량 ${volume}g/ml, ${containerType})</td>
        <td class="num">${unitPrice.toLocaleString()}원</td>
        <td class="num">${qty.toLocaleString()}</td>
        <td class="num">${totalPrice.toLocaleString()}원</td>
      </tr>
      ${devFee ? `
      <tr>
        <td>초기 개발비 (금형·규격 개발, 1회성)</td>
        <td class="num"></td>
        <td class="num"></td>
        <td class="num">${devFee.toLocaleString()}원</td>
      </tr>` : ''}
      ${vatType === 'exclusive' ? `
      <tr>
        <td>공급가액</td>
        <td class="num"></td>
        <td class="num"></td>
        <td class="num">${supplyAmount.toLocaleString()}원</td>
      </tr>
      <tr>
        <td>부가세 (10%)</td>
        <td class="num"></td>
        <td class="num"></td>
        <td class="num">${vatAmount.toLocaleString()}원</td>
      </tr>` : ''}
      <tr class="total">
        <td>합계 (VAT 포함)</td>
        <td class="num"></td>
        <td class="num"></td>
        <td class="num">${grandTotal.toLocaleString()}원</td>
      </tr>
    `;

    // 예상납기 계산 및 표시
    const leadDays = estimateLeadDays(qty);
    const deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + leadDays);
    deliveryInfo.textContent = `📦 예상납기: 발주 확정일로부터 영업일 기준 약 ${leadDays}일 (${formatDate(deliveryDate)} 전후 출고 예정)`;

    // Process: 과거 견적 3건과 비교 -> ±10% 이상 차이 시 플래그
    const history = HISTORY[client];
    if (history && history.length){
      const avg = history.reduce((s,h)=>s+h.unit,0) / history.length;
      const diffPct = ((unitPrice - avg) / avg) * 100;

      compareBody.innerHTML = history.map(h => {
        const d = ((unitPrice - h.unit) / h.unit * 100).toFixed(1);
        return `<tr><td>${h.date}</td><td class="num">${h.unit.toLocaleString()}원</td><td class="num">${d > 0 ? '+' : ''}${d}%</td></tr>`;
      }).join('');

      if (Math.abs(diffPct) >= 10){
        flagBadge.className = 'status-flag warn';
        flagBadge.textContent = `⚠️ 단가 변동 주의 (과거 평균 대비 ${diffPct > 0 ? '+' : ''}${diffPct.toFixed(1)}%)`;
      } else {
        flagBadge.className = 'status-flag ok';
        flagBadge.textContent = `과거 평균 대비 ${diffPct > 0 ? '+' : ''}${diffPct.toFixed(1)}% (정상 범위)`;
      }
    } else {
      compareBody.innerHTML = `<tr><td colspan="3" style="color:var(--ink-soft);">이 고객사의 과거 견적 이력이 없습니다.</td></tr>`;
      flagBadge.className = 'status-flag ok';
      flagBadge.textContent = '신규 고객사 (비교 이력 없음)';
    }

    emptyState.style.display = 'none';
    resultPanel.style.display = 'block';
  });

  function resetForm(){
    form.reset();
    emptyState.style.display = 'flex';
    resultPanel.style.display = 'none';
  }

  // 옛 quote-builder.html 링크(#builder)로 들어온 경우 견적 생성 화면을 바로 표시
  if (window.location.hash === '#builder'){
    showBuilder();
  }
</script>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

@st.cache_data
def build_app_html() -> str:
    """모든 정적 리소스(HTML/CSS/JS/이미지)가 app.py 안에 인라인되어 있으므로
    외부 파일(assets 폴더, .html/.js/.webp) 없이 배포 환경에서도 항상 렌더링된다."""
    html = APP_HTML_TEMPLATE
    html = html.replace(
        '<script src="sample-data.js"></script>',
        f"<script>\n{SAMPLE_DATA_JS}\n</script>",
    )
    html = html.replace(
        "url('sensifilter-hero.webp')",
        f"url('data:image/webp;base64,{HERO_IMAGE_B64}')",
    )
    return html


components.html(build_app_html(), height=1700, scrolling=True)
