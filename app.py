# app.py
import streamlit as st
import base64

def render_html_css_svg(html_code, css_code, svg_code, svg_mode):
    """Combines HTML, CSS, and SVG and returns a complete HTML string."""

    combined_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Rendered Output</title>
        <style>
        {css_code}
        </style>
    </head>
    <body>
        {html_code}
    """

    if svg_code:
        if svg_mode == "Direct Paste":
            combined_html += svg_code
        elif svg_mode == "Base64 Encoded":
            try:
                # Basic Base64 validation
                base64.b64decode(svg_code)
                combined_html += f'<img src="data:image/svg+xml;base64,{svg_code}" alt="Embedded SVG">'
            except Exception as e:
                st.error(f"Invalid Base64 encoded SVG: {e}")
                return None  # Return None on error to prevent rendering

    combined_html += """
    </body>
    </html>
    """
    return combined_html

def main():
    st.set_page_config(layout="wide") # Use wide layout for better display
    st.title("Universal HTML, CSS, and SVG Renderer")

    st.sidebar.header("Code Input")
    html_code = st.sidebar.text_area("HTML", height=300, key="html")
    css_code = st.sidebar.text_area("CSS", height=300, key="css")
    svg_code = st.sidebar.text_area("SVG (Paste directly or Base64)", height=150, key="svg")
    svg_mode = st.sidebar.selectbox("SVG Mode", ["Direct Paste", "Base64 Encoded"], key="svg_mode")

    # Button to trigger rendering
    if st.sidebar.button("Render"):
        combined_html = render_html_css_svg(html_code, css_code, svg_code, svg_mode)
        if combined_html:  # Check if combined_html is not None (no errors)
            st.components.v1.html(combined_html, height=800, scrolling=True)


if __name__ == "__main__":
    main()
