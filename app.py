import streamlite as st

pages = [
    st.Page(page="pages/page01.py", title="Home", icon="🏡")
    st.Page(page="pages/page02.py", title="Visualisasi Data", icon="📈")
    st.Page(page="pages/page02.py", title="Settings", icon="⚙️")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()