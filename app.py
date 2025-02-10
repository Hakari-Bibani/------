import streamlit as st
import base64

def main():
    st.title("HTML, CSS, and SVG Viewer")

    st.sidebar.header("Code Input")
    html_code = st.sidebar.text_area("HTML", height=200)
    css_code = st.sidebar.text_area("CSS", height=200)
    svg_code = st.sidebar.text_area("SVG (Paste directly or Base64)", height=100)
    mode = st.sidebar.selectbox("SVG Mode", ["Direct Paste", "Base64 Encoded"])


    # Combine HTML and CSS
    combined_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        {css_code}
        </style>
    </head>
    <body>
        {html_code}
    """
    # Handle SVG
    if svg_code:
        if mode == "Direct Paste":
            combined_html += svg_code
        elif mode == "Base64 Encoded":
            try:
                # Validate Base64 (basic check)
                base64.b64decode(svg_code)
                combined_html += f'<img src="data:image/svg+xml;base64,{svg_code}" alt="Embedded SVG">'
            except Exception as e:
                st.error(f"Invalid Base64 encoded SVG: {e}")
                return # Stop if Base64 is invalid

    combined_html += """
    </body>
    </html>
    """

    st.components.v1.html(combined_html, height=600, scrolling=True)

if __name__ == "__main__":
    main()
